#!/usr/bin/env python3
"""Regenerate promo ads as brand-matched slide films with paced voiceover.

Replaces outdated screen-recording backgrounds with the current parchment / gold
look used by the live site and tutorial lessons.
"""

from __future__ import annotations

import asyncio
import re
import subprocess
import tempfile
from pathlib import Path

import edge_tts
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "docs" / "assets" / "promo"
CAMPAIGN_DIR = OUT_DIR / "campaign"
FONT_DIR = ROOT / "docs" / "assets" / "fonts"

VOICE = "en-US-JennyNeural"
VOICE_RATE = "-10%"
SLIDE_TAIL_PAD = 0.7
MIN_MEAN_VOLUME_DB = -40.0
W, H = 1280, 720

INK = (14, 17, 22)
PAPER_TOP = (247, 239, 223)
PAPER_DEEP = (224, 213, 188)
GOLD = (201, 162, 39)
GOLD_LIGHT = (226, 193, 90)
GOLD_DARK = (154, 123, 26)

FONT_DISP = str(FONT_DIR / "fraunces.ttf")
FONT_BODY = str(FONT_DIR / "figtree.ttf")
FONT_DISP_FALLBACK = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONT_BODY_FALLBACK = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


PROMOS = [
    {
        "id": "promo-ad-1-start-here",
        "out_dir": OUT_DIR,
        "file": "promo-ad-1-start-here.mp4",
        "title": "Start Here",
        "slides": [
            {
                "title": "New to coding?",
                "bullets": ["Open Start Here", "Follow one clear checklist", "Mark steps done as you go"],
                "vo": "New to coding? Open Start Here. Follow one clear checklist. Mark each step done as you go.",
            },
            {
                "title": "Learn in your browser",
                "bullets": ["No install needed to begin", "Python, C sharp, or A I paths", "Free and self-paced"],
                "vo": "You can learn in your browser first. No install is needed to begin. Choose Python, C sharp, or A I — free and self-paced.",
            },
        ],
    },
    {
        "id": "promo-ad-2-courses-donate",
        "out_dir": OUT_DIR,
        "file": "promo-ad-2-courses-donate.mp4",
        "title": "Courses & support",
        "slides": [
            {
                "title": "Pick a beginner path",
                "bullets": ["Browse Courses", "Open Python, C sharp, or A I", "Lessons, quizzes, and projects"],
                "vo": "Pick a beginner path. Browse Courses, then open Python, C sharp, or A I. Each path has lessons, quizzes, and projects.",
            },
            {
                "title": "Keep the course free",
                "bullets": ["Learning stays free", "Optional donation on Support", "Helps host and improve the site"],
                "vo": "Learning stays free. If you want to help, Support has an optional donation. That helps host and improve the site.",
            },
        ],
    },
    {
        "id": "promo-45s-system-tour",
        "out_dir": OUT_DIR,
        "file": "promo-45s-system-tour-vo.mp4",
        "alias_file": "promo-45s-system-tour.mp4",
        "audio_file": "promo-45s-voiceover.m4a",
        "transcript_file": "promo-45s-transcript.txt",
        "title": "System tour",
        "slides": [
            {
                "title": "Learn from zero",
                "bullets": ["Beginner-friendly path", "Track progress step by step", "Build real projects"],
                "vo": "Start your programming journey from zero. Track your progress step by step as you build real projects.",
            },
            {
                "title": "Choose your course",
                "bullets": ["Python, C sharp, or A I", "Clear modules", "Lessons and quizzes"],
                "vo": "Choose a beginner-friendly path — Python, C sharp, or A I. Follow clear modules with lessons and quizzes.",
            },
            {
                "title": "Learn your way",
                "bullets": ["Free account syncs progress", "Guest mode anytime", "No experience needed"],
                "vo": "Create a free account to sync progress when you can. Or keep learning as a guest anytime.",
            },
            {
                "title": "Programming Foundations",
                "bullets": ["Stays free to learn", "Optional donation welcome", "Start here today"],
                "vo": "This course stays free. If you want to help keep it online, you can support us with a donation. Programming Foundations. Start learning today — no experience needed.",
            },
        ],
    },
]

CAMPAIGNS = [
    {
        "id": "01-from-zero",
        "title": "From zero",
        "slides": [
            {
                "title": "No coding background?",
                "bullets": ["That is okay", "Start with Module 1", "Learn in your browser"],
                "vo": "No coding background? That is okay. Start with Module 1 in your browser.",
            },
            {
                "title": "A calm first path",
                "bullets": ["Short lessons", "Practice and quizzes", "Build confidence step by step"],
                "vo": "You get short lessons, practice, and quizzes. Build confidence one step at a time.",
            },
        ],
    },
    {
        "id": "02-guided-path",
        "title": "Guided path",
        "slides": [
            {
                "title": "Not sure what to do next?",
                "bullets": ["Open Start Here", "Follow the checklist", "Mark each step done"],
                "vo": "Not sure what to do next? Open Start Here. Follow the checklist and mark each step done.",
            },
            {
                "title": "Clear next steps",
                "bullets": ["Less overwhelm", "One path forward", "Resume where you left off"],
                "vo": "Clear next steps mean less overwhelm. One path forward — and you can resume where you left off.",
            },
        ],
    },
    {
        "id": "03-choose-course",
        "title": "Choose a course",
        "slides": [
            {
                "title": "Pick what fits you",
                "bullets": ["Python for an easy start", "C sharp for Windows and dot net", "A I for prompt skills"],
                "vo": "Pick what fits you. Python for an easy start. C sharp for Windows and dot net. A I for prompt skills.",
            },
            {
                "title": "Then follow the modules",
                "bullets": ["Lessons teach the idea", "Quizzes check understanding", "Projects make it real"],
                "vo": "Then follow the modules. Lessons teach the idea. Quizzes check understanding. Projects make it real.",
            },
        ],
    },
    {
        "id": "04-real-skills",
        "title": "Real skills",
        "slides": [
            {
                "title": "Build things you can show",
                "bullets": ["Guided modules", "Hands-on exercises", "Portfolio-ready projects"],
                "vo": "Build things you can show. Guided modules, hands-on exercises, and portfolio-ready projects.",
            },
            {
                "title": "Skills that transfer",
                "bullets": ["Jobs and freelance work", "School and career change", "Practice that sticks"],
                "vo": "These are skills that transfer — for jobs, freelance work, school, or a career change.",
            },
        ],
    },
    {
        "id": "05-prove-it",
        "title": "Prove it",
        "slides": [
            {
                "title": "Finish modules with proof",
                "bullets": ["Complete lessons and quizzes", "Track your progress", "Earn completion certificates"],
                "vo": "Finish modules with proof. Complete lessons and quizzes, track your progress, and earn completion certificates.",
            },
            {
                "title": "Show your work",
                "bullets": ["Share with employers", "Share with clients", "Keep a record for yourself"],
                "vo": "Show your work to employers or clients — and keep a record for yourself.",
            },
        ],
    },
    {
        "id": "06-free-flexible",
        "title": "Free & flexible",
        "slides": [
            {
                "title": "Learn without a paywall",
                "bullets": ["Course stays free", "Study at your pace", "Guest mode or free account"],
                "vo": "Learn without a paywall. The course stays free. Study at your pace as a guest or with a free account.",
            },
            {
                "title": "Support if you can",
                "bullets": ["Optional donation", "Helps keep the site online", "Start learning today"],
                "vo": "Support is optional. If you can donate, it helps keep the site online. Start learning today.",
            },
        ],
    },
]


def font(path: str, size: int, fallback: str) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size=size)
    except OSError:
        return ImageFont.truetype(fallback, size=size)


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


def parchment() -> Image.Image:
    img = Image.new("RGB", (W, H), PAPER_TOP)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / max(H - 1, 1)
        r = int(PAPER_TOP[0] * (1 - t) + PAPER_DEEP[0] * t)
        g = int(PAPER_TOP[1] * (1 - t) + PAPER_DEEP[1] * t)
        b = int(PAPER_TOP[2] * (1 - t) + PAPER_DEEP[2] * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    for y in range(120, H - 70, 28):
        draw.line([(56, y), (W - 48, y)], fill=(210, 190, 150))
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for radius, alpha in ((420, 55), (280, 40), (160, 28)):
        gd.ellipse([90 - radius, -100 - radius, 90 + radius, -100 + radius], fill=(226, 193, 90, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, 10, H], fill=GOLD)
    draw.rectangle([10, 0, 14, H], fill=GOLD_DARK)
    draw.rectangle([0, H - 56, W, H], fill=INK)
    return img


def render_slide(title: str, bullets: list[str], footer: str, out_path: Path) -> None:
    img = parchment()
    draw = ImageDraw.Draw(img)
    brand = font(FONT_DISP, 26, FONT_DISP_FALLBACK)
    kicker = font(FONT_BODY, 17, FONT_BODY_FALLBACK)
    title_f = font(FONT_DISP, 44, FONT_DISP_FALLBACK)
    body_f = font(FONT_BODY, 27, FONT_BODY_FALLBACK)
    foot_f = font(FONT_BODY, 17, FONT_BODY_FALLBACK)
    draw.text((48, 28), "Programming Foundations", fill=INK, font=brand)
    draw.text((48, 66), "COURSE TOUR", fill=GOLD_DARK, font=kicker)
    y = 108
    for tline in wrap(draw, title, title_f, W - 120):
        draw.text((48, y), tline, fill=INK, font=title_f)
        y += 52
    y += 16
    for bullet in bullets:
        for i, bline in enumerate(wrap(draw, bullet, body_f, W - 160)):
            prefix = "•  " if i == 0 else "   "
            draw.text((56, y), f"{prefix}{bline}", fill=INK, font=body_f)
            y += 38
        y += 8
    draw.text((48, H - 36), footer, fill=GOLD_LIGHT, font=foot_f)
    img.save(out_path, "PNG")


def mean_volume_db(media: Path) -> float:
    out = subprocess.check_output(
        ["ffmpeg", "-i", str(media), "-af", "volumedetect", "-f", "null", "-"],
        stderr=subprocess.STDOUT,
        text=True,
    )
    match = re.search(r"mean_volume:\s*([-\d.]+)\s*dB", out)
    if not match:
        raise RuntimeError(f"Could not measure volume for {media}")
    return float(match.group(1))


async def synth(text: str, out_mp3: Path) -> float:
    await edge_tts.Communicate(text, VOICE, rate=VOICE_RATE).save(str(out_mp3))
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


def still(png: Path, seconds: float, out_mp4: Path) -> None:
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(png),
            "-t",
            f"{max(seconds, 1.2):.3f}",
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-pix_fmt",
            "yuv420p",
            "-an",
            "-r",
            "30",
            str(out_mp4),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def pad_audio(src: Path, total: float, out: Path) -> None:
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-i",
            str(src),
            "-af",
            f"apad=whole_dur={total:.3f}",
            "-t",
            f"{total:.3f}",
            "-c:a",
            "aac",
            "-b:a",
            "128k",
            str(out),
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
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "copy",
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
            "-b:a",
            "128k",
            "-movflags",
            "+faststart",
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    listing.unlink(missing_ok=True)


def extract_audio(src: Path, out: Path) -> None:
    subprocess.check_call(
        ["ffmpeg", "-y", "-i", str(src), "-vn", "-c:a", "aac", "-b:a", "128k", str(out)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def assert_muxed_audible(path: Path) -> float:
    """Refuse to ship any final MP4 without an audible audio track."""
    probe = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-select_streams",
            "a",
            "-show_entries",
            "stream=codec_type",
            "-of",
            "csv=p=0",
            str(path),
        ],
        text=True,
    ).strip()
    if "audio" not in probe:
        raise RuntimeError(f"{path.name} has no audio stream — all shipped MP4s must be muxed.")
    volume = mean_volume_db(path)
    if volume < MIN_MEAN_VOLUME_DB:
        raise RuntimeError(f"Silent or near-silent audio in {path.name} ({volume:.1f} dB)")
    return volume


async def build_clip(slides: list[dict], footer: str, work: Path) -> tuple[Path, list[str], float]:
    parts: list[Path] = []
    vos: list[str] = []
    for i, slide in enumerate(slides, start=1):
        png = work / f"slide-{i:02d}.png"
        mp3 = work / f"slide-{i:02d}.mp3"
        padded = work / f"slide-{i:02d}.m4a"
        vid = work / f"slide-{i:02d}-v.mp4"
        voiced = work / f"slide-{i:02d}.mp4"
        render_slide(slide["title"], slide["bullets"], footer, png)
        dur = await synth(slide["vo"], mp3)
        hold = max(dur, 2.4 + 0.45 * len(slide["bullets"])) + SLIDE_TAIL_PAD
        pad_audio(mp3, hold, padded)
        still(png, hold, vid)
        mux(vid, padded, voiced)
        parts.append(voiced)
        vos.append(slide["vo"])
    out = work / "final.mp4"
    concat(parts, out)
    volume = assert_muxed_audible(out)
    return out, vos, volume


async def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    CAMPAIGN_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="pf-promo-") as tmp:
        root = Path(tmp)
        for promo in PROMOS:
            print(f"Building {promo['id']}…")
            work = root / promo["id"]
            work.mkdir()
            final, vos, volume = await build_clip(
                promo["slides"],
                f"promo.html · {promo['title']}",
                work,
            )
            dest = promo["out_dir"] / promo["file"]
            dest.write_bytes(final.read_bytes())
            assert_muxed_audible(dest)
            # Optional alias path must also be muxed (never write a silent picture track).
            if promo.get("alias_file"):
                alias = promo["out_dir"] / promo["alias_file"]
                alias.write_bytes(final.read_bytes())
                assert_muxed_audible(alias)
            if promo.get("audio_file"):
                extract_audio(dest, promo["out_dir"] / promo["audio_file"])
            if promo.get("transcript_file"):
                lines = [
                    "Programming Foundations — promo voiceover",
                    f"File: {promo['file']}",
                    f"Voice: {VOICE} @ {VOICE_RATE}",
                    "",
                    "────────────────────────────────────────",
                    "FULL VOICEOVER",
                    "────────────────────────────────────────",
                    "",
                    *vos,
                    "",
                    " ".join(vos),
                    "",
                ]
                (promo["out_dir"] / promo["transcript_file"]).write_text("\n".join(lines), encoding="utf-8")
            print(f"  → {dest.name} ({volume:.1f} dB)")

        for camp in CAMPAIGNS:
            print(f"Building campaign-{camp['id']}…")
            work = root / camp["id"]
            work.mkdir()
            final, vos, volume = await build_clip(
                camp["slides"],
                f"promo.html · {camp['title']}",
                work,
            )
            vo_path = CAMPAIGN_DIR / f"campaign-{camp['id']}-vo.mp4"
            primary_path = CAMPAIGN_DIR / f"campaign-{camp['id']}.mp4"
            audio_path = CAMPAIGN_DIR / f"campaign-{camp['id']}-voiceover.m4a"
            transcript_path = CAMPAIGN_DIR / f"{camp['id']}-transcript.txt"
            payload = final.read_bytes()
            vo_path.write_bytes(payload)
            primary_path.write_bytes(payload)
            assert_muxed_audible(vo_path)
            assert_muxed_audible(primary_path)
            extract_audio(vo_path, audio_path)
            transcript_path.write_text(
                "\n".join(
                    [
                        f"Programming Foundations — campaign {camp['id']}",
                        f"Voice: {VOICE} @ {VOICE_RATE}",
                        "",
                        *vos,
                        "",
                        " ".join(vos),
                        "",
                    ]
                ),
                encoding="utf-8",
            )
            print(f"  → {vo_path.name} + {primary_path.name} ({volume:.1f} dB)")

    print("Done:", OUT_DIR)


if __name__ == "__main__":
    asyncio.run(main())
