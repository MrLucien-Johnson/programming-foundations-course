# Promo campaign pack

Short brand-matched slide ads with paced **muxed** voiceover (same parchment / gold style as tutorials).

**Policy:** every shipped `.mp4` must include audible audio. Silent picture tracks are not generated.

Rebuild with:

```bash
python3 scripts/promo/generate_promo_slides.py
python3 scripts/assert_videos_muxed.py
```

Play all on: https://mrlucien-johnson.github.io/programming-foundations-course/promo.html

| ID | Angle | Real-life hook |
|----|-------|----------------|
| `01-from-zero` | Absolute beginners | “I have no coding background” |
| `02-guided-path` | Start Here checklist | Clear next steps instead of overwhelm |
| `03-choose-course` | Python / C# / AI | Pick a path that matches your goals |
| `04-real-skills` | Modules + projects | Portfolio / job / freelance skills |
| `05-prove-it` | Certificates | Show completion to employers/clients |
| `06-free-flexible` | Free + sync + donate | Learn anywhere without a paywall |

## Files per angle

For each `NN-name`:

- `campaign-NN-name-vo.mp4` — muxed video + voiceover (primary)
- `campaign-NN-name.mp4` — same muxed file (alias for older links)
- `campaign-NN-name-voiceover.m4a` — audio only
- `NN-name-transcript.txt` — full script

Voice: warm US English (Jenny), slightly slowed for clarity. Audio is volume-checked on build.
