---
layout: default
title: "Download YouTube subtitles as SRT or VTT without downloading the video"
description: "Get YouTube captions as SRT or WebVTT files with an API call or yt-dlp, without downloading the video."
---

# Download YouTube subtitles as SRT or VTT without downloading the video

## With the Actor

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"], "outputFormats": ["srt", "vtt"], "includeSegments": false}'
```

The result has `srt` and `vtt` fields containing the subtitle files as text. Save them as `.srt` / `.vtt`. The video is never downloaded.

Ready-made page: [Download YouTube subtitles as SRT or WebVTT](https://apify.com/codepulsehq/youtube-transcript-api/examples/download-youtube-subtitles-srt-vtt).

## With yt-dlp

```bash
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs en --convert-subs srt "https://www.youtube.com/watch?v=UF8uR6Z6KLc"
```

(`--convert-subs` needs ffmpeg installed.)

## Notes

- Creator-written captions are preferred over auto-generated ones when both exist. The result's `auto_generated` field tells you which you got.
- You get the captions in the language you ask for (`"language": "en"`). If the video has no captions in that language, you get its first available track and the result tells you which.
