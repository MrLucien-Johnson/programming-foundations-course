#!/usr/bin/env python3
"""Generate beginner tutorial MP4s (slides + Jenny voiceover) for Programming Foundations."""

from __future__ import annotations

import asyncio
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "assets" / "tutorials"
VOICE = "en-US-JennyNeural"
W, H = 1280, 720
INK = (14, 17, 22)
PAPER = (243, 239, 230)
GOLD = (201, 162, 39)
GOLD_LIGHT = (226, 193, 90)
MUTED = (90, 95, 107)
WHITE = (255, 255, 255)

FONT_REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
FONT_DISP = "/usr/share/fonts/truetype/noto/NotoSansDisplay-Bold.ttf"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


def wrap(draw: ImageDraw.ImageDraw, text: str, fnt: ImageFont.ImageFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]


def render_slide(title: str, lines: list[str], footer: str, out_path: Path) -> None:
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Top brand bar
    draw.rectangle([0, 0, W, 12], fill=GOLD)
    draw.rectangle([0, H - 56, W, H], fill=INK)
    # Soft side accent
    draw.rectangle([0, 12, 18, H - 56], fill=GOLD_LIGHT)

    brand = font(FONT_BOLD, 22)
    title_f = font(FONT_DISP, 46)
    body_f = font(FONT_REG, 28)
    foot_f = font(FONT_REG, 18)

    draw.text((48, 36), "Programming Foundations", fill=INK, font=brand)
    draw.text((48, 78), "Tutorial", fill=GOLD, font=font(FONT_BOLD, 18))

    y = 130
    for tline in wrap(draw, title, title_f, W - 120):
        draw.text((48, y), tline, fill=INK, font=title_f)
        y += 58

    y += 18
    for bullet in lines:
        for bline in wrap(draw, f"•  {bullet}", body_f, W - 140):
            draw.text((56, y), bline, fill=MUTED if bline.startswith("•") is False else INK, font=body_f)
            # Force ink for bullets
            draw.text((56, y), bline, fill=INK, font=body_f)
            y += 40
        y += 10

    draw.text((48, H - 38), footer, fill=GOLD_LIGHT, font=foot_f)
    img.save(out_path, "PNG")


async def synth(text: str, out_mp3: Path) -> float:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(out_mp3))
    # Probe duration via ffprobe
    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "quiet",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(out_mp3),
        ],
        text=True,
    ).strip()
    return max(float(probe), 1.2)


def still_to_video(png: Path, seconds: float, out_mp4: Path) -> None:
    # Pad a touch so VO never clips
    duration = seconds + 0.35
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(png),
            "-f",
            "lavfi",
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=44100",
            "-t",
            f"{duration:.3f}",
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-shortest",
            "-r",
            "30",
            str(out_mp4),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def mux(video: Path, audio: Path, out: Path) -> None:
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(video),
            "-i",
            str(audio),
            "-c:v",
            "copy",
            "-c:a",
            "aac",
            "-shortest",
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def concat(parts: list[Path], out: Path) -> None:
    listing = out.with_suffix(".txt")
    listing.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(listing),
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-movflags",
            "+faststart",
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    listing.unlink(missing_ok=True)


TUTORIALS = [
    {
        "id": "01-get-started-download",
        "title": "Get started — browser & download",
        "when": "start-here, help, courses",
        "footer": "tutorials.html · Start Here",
        "pathMatch": "",
        "hubAnchor": "get-started",
        "slides": [
            {
                "title": "Learn in your browser first",
                "bullets": [
                    "No install needed to start Module 1 online",
                    "Open Start Here, then pick Python, C#, or AI",
                    "Mark steps done as you go — progress stays in this browser",
                ],
                "vo": "Learn in your browser first. You do not need to install anything to start Module 1 online. Open Start Here, pick Python, C sharp, or A I, and mark steps done as you go.",
            },
            {
                "title": "When you want files on your computer",
                "bullets": [
                    "Use the GitHub Code → Download ZIP button",
                    "Or clone the repo if you already use Git",
                    "Find the ZIP in your Downloads folder and unzip it",
                ],
                "vo": "When you want files on your computer, use GitHub’s Code menu and choose Download ZIP. Find the file in Downloads, then unzip it. Git is optional — beginners can use the ZIP.",
            },
            {
                "title": "Open the right folder",
                "bullets": [
                    "Python path: python-beginner-workbook",
                    "C# path: csharp-beginner-workbook",
                    "Start with each track’s Module 1 setup guide",
                ],
                "vo": "Open the right folder for your course. Python lives in python-beginner-workbook. C sharp lives in csharp-beginner-workbook. Always start with Module 1 setup.",
            },
            {
                "title": "Quick tip",
                "bullets": [
                    "Stuck on downloads? Check Help → Downloads",
                    "You can keep learning online while tools install",
                    "Guest mode works offline in this browser after pages load",
                ],
                "vo": "Quick tip: if a download goes missing, check the Help page. You can keep learning online while installers run in the background.",
            },
        ],
    },
    {
        "id": "02-python-setup",
        "title": "Python — download, install, first script",
        "when": "python-course, module-01-setup",
        "footer": "tutorials.html · Python Module 1",
        "pathMatch": "python-beginner-workbook/module-01-setup",
        "hubAnchor": "python-setup",
        "slides": [
            {
                "title": "Install Python",
                "bullets": [
                    "Go to python.org/downloads",
                    "Windows: tick Add Python to PATH, then Install Now",
                    "macOS/Linux: run the installer or use python3",
                ],
                "vo": "Install Python from python.org slash downloads. On Windows, tick Add Python to PATH before you install. On Mac or Linux, use the installer or python 3.",
            },
            {
                "title": "Verify it worked",
                "bullets": [
                    "Open Terminal or Command Prompt",
                    "Run: python --version  (or python3 --version)",
                    "You should see a version like Python 3.11 or newer",
                ],
                "vo": "Verify it worked. Open a terminal and run python dash dash version, or python 3 dash dash version. You should see a version number.",
            },
            {
                "title": "Install a code editor",
                "bullets": [
                    "Cursor (cursor.sh) or Visual Studio Code",
                    "Add the Python extension",
                    "Open the python-beginner-workbook folder",
                ],
                "vo": "Install a code editor such as Cursor or Visual Studio Code. Add the Python extension, then open your python-beginner-workbook folder.",
            },
            {
                "title": "Your first script",
                "bullets": [
                    "Create hello.py with print(\"Hello!\")",
                    "Run: python hello.py",
                    "Customize the message — that’s your first real program",
                ],
                "vo": "Create hello.py with a print hello message, then run python hello.py. Change the text — that is your first real program.",
            },
            {
                "title": "Python tips",
                "bullets": [
                    "PATH errors on Windows → reinstall with Add to PATH",
                    "Use the editor’s integrated terminal",
                    "Follow Module 1 exercises, then take the quiz",
                ],
                "vo": "If Windows cannot find Python, reinstall and tick Add to PATH. Use the editor terminal, finish Module 1 exercises, then take the quiz.",
            },
        ],
    },
    {
        "id": "03-csharp-setup",
        "title": "C# — install .NET and first project",
        "when": "csharp-course, module-01-setup",
        "footer": "tutorials.html · C# Module 1",
        "pathMatch": "csharp-beginner-workbook/module-01-setup",
        "hubAnchor": "csharp-setup",
        "slides": [
            {
                "title": "Install the .NET SDK",
                "bullets": [
                    "Go to dotnet.microsoft.com/download",
                    "Download the latest .NET SDK (8 or newer)",
                    "Run the installer, then Finish",
                ],
                "vo": "Install the dot net S D K from dotnet.microsoft.com slash download. Get the latest S D K, run the installer, then finish.",
            },
            {
                "title": "Verify with the terminal",
                "bullets": [
                    "Open Terminal or Command Prompt",
                    "Run: dotnet --version",
                    "A version like 8.0.x means you are ready",
                ],
                "vo": "Open a terminal and run dotnet dash dash version. A number like 8 point 0 means you are ready.",
            },
            {
                "title": "Editor + C# tools",
                "bullets": [
                    "Install Cursor or Visual Studio Code",
                    "Add the C# Dev Kit extension",
                    "Open csharp-beginner-workbook in the editor",
                ],
                "vo": "Install Cursor or Visual Studio Code, add the C sharp Dev Kit extension, and open the csharp-beginner-workbook folder.",
            },
            {
                "title": "Create and run a console app",
                "bullets": [
                    "dotnet new console -n HelloWorld",
                    "cd HelloWorld",
                    "dotnet run — then edit Program.cs",
                ],
                "vo": "Create a console app with dotnet new console, move into the folder, and run dotnet run. Edit Program.cs to make it yours.",
            },
            {
                "title": "C# tips",
                "bullets": [
                    "C# is the language; .NET is the toolbox",
                    "Always open the project folder, not a single file",
                    "Do Module 1 exercises, then the quiz",
                ],
                "vo": "Remember: C sharp is the language and dot net is the toolbox. Open the whole project folder, finish Module 1, then take the quiz.",
            },
        ],
    },
    {
        "id": "04-tips-tricks",
        "title": "Tips & tricks for this site",
        "when": "help, start-here, account",
        "footer": "tutorials.html · Help",
        "pathMatch": "",
        "hubAnchor": "tips",
        "slides": [
            {
                "title": "Follow Start Here in order",
                "bullets": [
                    "Open Module 1 online before installing tools",
                    "Pick one course and stay with it",
                    "Use Mark done so your path updates",
                ],
                "vo": "Follow Start Here in order. Open Module 1 online before installing tools, pick one course, and use Mark done so your path updates.",
            },
            {
                "title": "Lessons, quizzes, and progress",
                "bullets": [
                    "Read the lesson, then take the module quiz",
                    "Continue banners bring you back where you left off",
                    "Certificates unlock when every module is complete",
                ],
                "vo": "Read each lesson, then take the module quiz. Continue banners bring you back where you left off, and certificates unlock when every module is complete.",
            },
            {
                "title": "Guest mode vs free account",
                "bullets": [
                    "Guest progress stays in this browser",
                    "An account can sync when the cloud API is up",
                    "Keep guest progress as a backup on free hosting",
                ],
                "vo": "Guest progress stays in this browser. A free account can sync when the cloud is up. Keep guest progress as a backup on free hosting.",
            },
            {
                "title": "Practice habits that stick",
                "bullets": [
                    "Type the examples — don’t only read them",
                    "Break big tasks into tiny checkpoints",
                    "When stuck, re-read the tip boxes, then ask Help",
                ],
                "vo": "Type the examples instead of only reading them. Break big tasks into tiny checkpoints. When stuck, re-read the tip boxes, then open Help.",
            },
            {
                "title": "You are ready",
                "bullets": [
                    "Start Here → Courses → Module 1",
                    "Watch the Python or C# install video when coding locally",
                    "Support the project on the Support page if you can",
                ],
                "vo": "You are ready. Go Start Here, choose a course, and open Module 1. Watch the Python or C sharp install video when you code locally. Enjoy learning.",
            },
        ],
    },
    {
        "id": "05-ai-foundations",
        "title": "AI Module 1 — foundations overview",
        "when": "ai-course, 01-ai-foundations",
        "footer": "tutorials.html · AI Beginner Module 1",
        "pathMatch": "languages/ai/beginner/modules/01-ai-foundations",
        "hubAnchor": "ai-foundations",
        "slides": [
            {
                "title": "What this AI course is",
                "bullets": [
                    "Learn to use AI like an engineer — not magic",
                    "No coding install required to start Module 1",
                    "Focus: clear goals, constraints, and tests",
                ],
                "vo": "This A I course teaches you to use language models like an engineer, not like magic. You do not need a coding install to start Module 1. Focus on clear goals, constraints, and tests.",
            },
            {
                "title": "What LLMs are good at",
                "bullets": [
                    "Drafting, summarising, transforming text",
                    "Following structured formats when you specify them",
                    "Speeding up iteration when you check the output",
                ],
                "vo": "Language models are good at drafting, summarising, and transforming text. They follow structured formats when you specify them, and they speed up iteration when you check the output.",
            },
            {
                "title": "What they get wrong",
                "bullets": [
                    "They guess patterns — they do not “know” truth",
                    "They can invent facts (hallucinations)",
                    "Vague prompts produce vague, brittle results",
                ],
                "vo": "They guess patterns; they do not know truth. They can invent facts, called hallucinations. Vague prompts produce vague, brittle results.",
            },
            {
                "title": "The engineering loop",
                "bullets": [
                    "Spec → prompt → evaluate → iterate",
                    "Write goal, inputs, outputs, and failure modes",
                    "Keep a small eval set and rerun after changes",
                ],
                "vo": "Use the engineering loop: spec, prompt, evaluate, iterate. Write the goal, inputs, outputs, and failure modes. Keep a small evaluation set and rerun it after every change.",
            },
            {
                "title": "Your Module 1 next step",
                "bullets": [
                    "Open AI Foundations in the course viewer",
                    "Copy the beginner starter pack templates",
                    "Write a one-page summariser spec + 10 eval cases",
                ],
                "vo": "Open A I Foundations in the course viewer, copy the beginner starter pack templates, and write a one-page summariser spec with ten evaluation cases.",
            },
        ],
    },
    {
        "id": "06-python-basics",
        "title": "Python Module 2 — variables & input",
        "when": "python-course, module-02-basics",
        "footer": "tutorials.html · Python Module 2",
        "pathMatch": "python-beginner-workbook/module-02-basics",
        "hubAnchor": "python-basics",
        "slides": [
            {
                "title": "After your first script",
                "bullets": [
                    "Module 2 makes programs interactive and useful",
                    "You will store values, ask for input, and calculate",
                    "These skills power forms, carts, and calculators",
                ],
                "vo": "After your first script, Module 2 makes programs interactive and useful. You will store values, ask for input, and calculate. These skills power forms, carts, and calculators.",
            },
            {
                "title": "Variables are labeled boxes",
                "bullets": [
                    "Name = value, for example customer_name = \"Sarah\"",
                    "Python chooses the type for you",
                    "Update a variable anytime by assigning again",
                ],
                "vo": "Variables are labeled boxes. Write a name equals a value, for example customer underscore name equals Sarah. Python chooses the type for you, and you can update a variable anytime.",
            },
            {
                "title": "Talk to the user",
                "bullets": [
                    "Use input(\"Your name: \") to ask a question",
                    "Store the answer in a variable",
                    "Combine text with f-strings: f\"Hello, {name}\"",
                ],
                "vo": "Talk to the user with input. Store the answer in a variable, then combine text with f-strings, like hello name.",
            },
            {
                "title": "Do useful math",
                "bullets": [
                    "Convert text numbers with float() or int()",
                    "Calculate price, tax, or wages",
                    "Print clear results with f-strings",
                ],
                "vo": "Do useful math. Convert text numbers with float or int, calculate price, tax, or wages, and print clear results with f-strings.",
            },
            {
                "title": "Practice path",
                "bullets": [
                    "Type the examples — do not only read them",
                    "Build the greeting and price calculator exercises",
                    "Take the Module 2 quiz when you feel ready",
                ],
                "vo": "Type the examples instead of only reading them. Build the greeting and price calculator exercises, then take the Module 2 quiz when you feel ready.",
            },
        ],
    },
    {
        "id": "07-csharp-basics",
        "title": "C# Module 2 — variables & input",
        "when": "csharp-course, module-02-basics",
        "footer": "tutorials.html · C# Module 2",
        "pathMatch": "csharp-beginner-workbook/module-02-basics",
        "hubAnchor": "csharp-basics",
        "slides": [
            {
                "title": "After your first console app",
                "bullets": [
                    "Module 2 adds variables, input, and calculations",
                    "C# uses clear types like string, int, and double",
                    "You will build greeting and calculator programs",
                ],
                "vo": "After your first console app, Module 2 adds variables, input, and calculations. C sharp uses clear types like string, int, and double. You will build greeting and calculator programs.",
            },
            {
                "title": "Declare with a type",
                "bullets": [
                    "string customerName = \"Sarah\";",
                    "int quantity = 3;  double price = 9.99;",
                    "Names describe the data you store",
                ],
                "vo": "Declare variables with a type. For example, string customer name equals Sarah, int quantity equals 3, double price equals 9.99. Choose names that describe the data.",
            },
            {
                "title": "Read input safely",
                "bullets": [
                    "Console.ReadLine() returns text",
                    "Parse numbers with int.Parse or double.Parse",
                    "Use string interpolation: $\"Hello, {name}\"",
                ],
                "vo": "Read input with Console.ReadLine, which returns text. Parse numbers with int.Parse or double.Parse, and format output with string interpolation.",
            },
            {
                "title": "Calculate real values",
                "bullets": [
                    "Tax, totals, and wages use ordinary math operators",
                    "Keep units clear in variable names",
                    "Print results the user can understand",
                ],
                "vo": "Calculate real values for tax, totals, and wages with ordinary math operators. Keep units clear in variable names, and print results the user can understand.",
            },
            {
                "title": "Practice path",
                "bullets": [
                    "Follow Module 2 examples in your project",
                    "Complete the exercises, then check solutions",
                    "Take the Module 2 quiz to lock in the skills",
                ],
                "vo": "Follow the Module 2 examples in your project, complete the exercises, check the solutions, and take the Module 2 quiz to lock in the skills.",
            },
        ],
    },
    {
        "id": "08-ai-prompting-basics",
        "title": "AI Module 2 — prompting basics",
        "when": "ai-course, 02-prompting-basics",
        "footer": "tutorials.html · AI Beginner Module 2",
        "pathMatch": "languages/ai/beginner/modules/02-prompting-basics",
        "hubAnchor": "ai-prompting",
        "slides": [
            {
                "title": "From vague to specific",
                "bullets": [
                    "A good prompt states role, goal, and format",
                    "Add constraints: length, tone, what not to do",
                    "Give one short example when helpful",
                ],
                "vo": "Move from vague to specific. A good prompt states role, goal, and format. Add constraints like length, tone, and what not to do, and give one short example when helpful.",
            },
            {
                "title": "Structure beats clever wording",
                "bullets": [
                    "Use headings: Goal, Inputs, Output format",
                    "Ask for checkable outputs (lists, JSON fields)",
                    "Prefer clear instructions over buzzwords",
                ],
                "vo": "Structure beats clever wording. Use headings for goal, inputs, and output format. Ask for checkable outputs, and prefer clear instructions over buzzwords.",
            },
            {
                "title": "Test before you trust",
                "bullets": [
                    "Try good, bad, and ambiguous inputs",
                    "Note failures: missing steps, invented facts",
                    "Tighten the prompt, then retest",
                ],
                "vo": "Test before you trust. Try good, bad, and ambiguous inputs. Note failures like missing steps or invented facts, tighten the prompt, then retest.",
            },
            {
                "title": "Your Module 2 next step",
                "bullets": [
                    "Open Prompting Basics in the course viewer",
                    "Rewrite one vague request into a structured prompt",
                    "Save before/after notes in your starter pack",
                ],
                "vo": "Open Prompting Basics in the course viewer. Rewrite one vague request into a structured prompt, and save before and after notes in your starter pack.",
            },
        ],
    },
]


def fmt_vtt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, milli = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{milli:03d}"


def write_vtt(cues: list[tuple[float, float, str]], out_path: Path) -> None:
    lines = ["WEBVTT", ""]
    for i, (start, end, text) in enumerate(cues, start=1):
        lines.append(str(i))
        lines.append(f"{fmt_vtt_time(start)} --> {fmt_vtt_time(end)}")
        # Keep captions readable: wrap long lines lightly
        lines.append(text.strip())
        lines.append("")
    out_path.write_text("\n".join(lines), encoding="utf-8")


async def build_one(tutorial: dict, work: Path) -> dict:
    tid = tutorial["id"]
    tdir = work / tid
    tdir.mkdir(parents=True, exist_ok=True)
    parts: list[Path] = []
    cues: list[tuple[float, float, str]] = []
    cursor = 0.0
    pad = 0.35
    transcript_lines = [
        f"Programming Foundations — Tutorial: {tutorial['title']}",
        f"ID: {tid}",
        f"Suggested placement: {tutorial['when']}",
        "",
        "────────────────────────────────────────",
        "FULL VOICEOVER (also provided as captions / on-page transcript)",
        "────────────────────────────────────────",
        "",
    ]
    full_vo = []
    for i, slide in enumerate(tutorial["slides"], start=1):
        png = tdir / f"slide-{i:02d}.png"
        mp3 = tdir / f"slide-{i:02d}.mp3"
        silent = tdir / f"slide-{i:02d}-silent.mp4"
        voiced = tdir / f"slide-{i:02d}.mp4"
        render_slide(slide["title"], slide["bullets"], tutorial["footer"], png)
        dur = await synth(slide["vo"], mp3)
        still_to_video(png, dur, silent)
        mux(silent, mp3, voiced)
        parts.append(voiced)
        slide_len = dur + pad
        cues.append((cursor, cursor + max(dur, 0.8), f"{slide['title']}: {slide['vo']}"))
        cursor += slide_len
        full_vo.append(slide["vo"])
        transcript_lines.append(f"[Slide {i}] {slide['title']}")
        transcript_lines.append(slide["vo"])
        transcript_lines.append("")

    transcript_lines.extend(
        [
            "────────────────────────────────────────",
            "COMBINED READ-ALOUD",
            "────────────────────────────────────────",
            "",
            " ".join(full_vo),
            "",
            "Voice: en-US JennyNeural (edge-tts)",
            "Captions: matching .vtt file (for deaf / hard-of-hearing users)",
            "Site: https://mrlucien-johnson.github.io/programming-foundations-course/tutorials.html",
        ]
    )

    out_mp4 = OUT_DIR / f"tutorial-{tid}.mp4"
    out_txt = OUT_DIR / f"tutorial-{tid}-transcript.txt"
    out_vtt = OUT_DIR / f"tutorial-{tid}.vtt"
    concat(parts, out_mp4)
    out_txt.write_text("\n".join(transcript_lines) + "\n", encoding="utf-8")
    write_vtt(cues, out_vtt)

    out_m4a = OUT_DIR / f"tutorial-{tid}-voiceover.m4a"
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(out_mp4),
            "-vn",
            "-c:a",
            "aac",
            str(out_m4a),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "quiet",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(out_mp4),
        ],
        text=True,
    ).strip()
    return {
        "id": tid,
        "title": tutorial["title"],
        "when": tutorial["when"],
        "pathMatch": tutorial.get("pathMatch", ""),
        "hubAnchor": tutorial.get("hubAnchor", tid.split("-", 1)[-1]),
        "file": out_mp4.name,
        "transcript": out_txt.name,
        "captions": out_vtt.name,
        "audio": out_m4a.name,
        "durationSec": round(float(probe), 1),
        "combinedTranscript": " ".join(full_vo),
    }


async def main() -> None:
    # Allow regenerating a subset: python3 generate_tutorials.py 05-ai-foundations
    import sys

    only = set(sys.argv[1:])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    selected = [t for t in TUTORIALS if not only or t["id"] in only or any(t["id"].startswith(x) for x in only)]
    # Load previous manifest so subset rebuilds keep other entries.
    prev = {}
    manifest_path = OUT_DIR / "manifest.json"
    if manifest_path.exists():
        try:
            for item in json.loads(manifest_path.read_text(encoding="utf-8")):
                prev[item["id"]] = item
        except Exception:
            prev = {}

    with tempfile.TemporaryDirectory(prefix="pf-tut-") as tmp:
        work = Path(tmp)
        for tutorial in selected:
            print(f"Building {tutorial['id']}…")
            meta = await build_one(tutorial, work)
            prev[meta["id"]] = meta
            print(f"  → {meta['file']} ({meta['durationSec']}s)")

    # Stable order by id
    manifest = [prev[t["id"]] for t in TUTORIALS if t["id"] in prev]
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    readme = [
        "# Learner tutorial videos",
        "",
        "Slide + voiceover lessons aligned to learning-path modules.",
        "Each clip includes: MP4, WebVTT captions, plain-text transcript, and audio.",
        "Voice: en-US JennyNeural. Rebuild with:",
        "",
        "```bash",
        "pip install edge-tts Pillow",
        "python3 scripts/tutorials/generate_tutorials.py",
        "# or a subset:",
        "python3 scripts/tutorials/generate_tutorials.py 05-ai-foundations 06-python-basics",
        "```",
        "",
        "| ID | Title | ~Length | Learning path |",
        "|----|-------|---------|---------------|",
    ]
    for m in manifest:
        readme.append(
            f"| `{m['id']}` | {m['title']} | ~{m['durationSec']:.0f}s | {m['when']} |"
        )
    readme.extend(
        [
            "",
            "Deaf / hard-of-hearing: enable captions on the video player, or open the on-page transcript / `.txt` download.",
            "",
            "Play on site: `docs/tutorials.html`",
            "",
        ]
    )
    (OUT_DIR / "README.md").write_text("\n".join(readme) + "\n", encoding="utf-8")
    print("Done:", OUT_DIR)


if __name__ == "__main__":
    asyncio.run(main())
