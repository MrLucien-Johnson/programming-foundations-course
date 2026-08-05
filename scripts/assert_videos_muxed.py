#!/usr/bin/env python3
"""Fail if any shipped docs MP4 is missing an audible audio track.

Policy: every published .mp4 under docs/assets must be muxed with voiceover
(or other audible audio). Silent picture-only exports are not allowed.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_ASSETS = ROOT / "docs" / "assets"
MIN_MEAN_VOLUME_DB = -40.0


def mean_volume_db(path: Path) -> float:
    proc = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"],
        capture_output=True,
        text=True,
        check=False,
    )
    for line in (proc.stderr or "").splitlines():
        if "mean_volume:" in line:
            return float(line.split("mean_volume:")[1].split("dB")[0].strip())
    return -99.0


def has_audio_stream(path: Path) -> bool:
    data = json.loads(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "a",
                "-show_entries",
                "stream=codec_type",
                "-of",
                "json",
                str(path),
            ],
            text=True,
        )
    )
    return bool(data.get("streams"))


def main() -> int:
    mp4s = sorted(DOCS_ASSETS.rglob("*.mp4"))
    if not mp4s:
        print("ERROR: no MP4 files found under docs/assets", file=sys.stderr)
        return 1

    errors: list[str] = []
    for path in mp4s:
        rel = path.relative_to(ROOT)
        if not has_audio_stream(path):
            errors.append(f"{rel}: no audio stream (must be muxed)")
            continue
        volume = mean_volume_db(path)
        if volume < MIN_MEAN_VOLUME_DB:
            errors.append(f"{rel}: near-silent audio ({volume:.1f} dB)")

    print(f"Checked {len(mp4s)} MP4 files under docs/assets")
    if errors:
        print(f"errors: {len(errors)}")
        for line in errors:
            print("ERROR:", line)
        return 1

    print("All MP4s are muxed with audible audio.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
