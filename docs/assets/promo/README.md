# Promo videos

Brand-matched slide films with paced **muxed** voiceover (parchment / gold look).

**Policy:** every shipped `.mp4` must include an audible audio track. Silent picture-only
exports are not allowed. Rebuilds refuse to write quiet or audio-less finals.

Rebuild:

```bash
pip install edge-tts Pillow
python3 scripts/promo/generate_promo_slides.py
python3 scripts/assert_videos_muxed.py
```

## Watch & download

**https://mrlucien-johnson.github.io/programming-foundations-course/promo.html**

## Files

| File | Contents |
|------|----------|
| `promo-ad-1-start-here.mp4` | Start Here path (muxed VO) |
| `promo-ad-2-courses-donate.mp4` | Courses + support (muxed VO) |
| `promo-45s-system-tour-vo.mp4` | Full tour with voiceover |
| `promo-45s-system-tour.mp4` | Same tour (muxed alias for older links) |
| `promo-45s-voiceover.m4a` | Tour audio only |
| `promo-45s-transcript.txt` | Tour script |

Audio is volume-checked on build so silent tracks cannot ship.
Voice: en-US JennyNeural (slightly slowed for clarity).

Live site: https://mrlucien-johnson.github.io/programming-foundations-course/
