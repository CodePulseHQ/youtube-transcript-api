# How to get a YouTube transcript without the YouTube Data API

**Short answer:** you don't need the YouTube Data API for public videos. Send the video link to a transcript service (or fetch the caption track yourself) and read the text back. No Google Cloud project, API key or OAuth needed.

## Why the official API doesn't work for this

The YouTube Data API has `captions.list` and `captions.download`, but they are meant for videos you own or manage. They require OAuth and permission from the video owner, so you can't use them to read the transcript of someone else's video. That is why most people end up with a library, `yt-dlp`, or a hosted service.

## Option 1: one request to a hosted Actor (no setup)

```bash
export APIFY_TOKEN=...   # free Apify account: Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"], "includeSegments": false}'
```

You get the transcript text, title, channel, description, thumbnail and view count. Videos without captions come back as a row with `success: false` and a reason, and are not charged. More examples: [Python](../examples/python/get_transcript.py), [JavaScript](../examples/javascript/get-transcript.mjs).

Try it in the browser: [Get the transcript of any YouTube video](https://apify.com/codepulsehq/youtube-transcript-api/examples/get-youtube-video-transcript).

## Option 2: do it yourself

- `pip install youtube-transcript-api`, then `YouTubeTranscriptApi().fetch("VIDEO_ID")`. Free and simple, works well on a laptop. On cloud servers expect blocks: see [Fix RequestBlocked / IpBlocked](fix-requestblocked-ipblocked-on-aws.md).
- `yt-dlp --skip-download --write-auto-subs --write-subs --sub-format vtt URL` saves the subtitle file without downloading the video.

## Which one should I use?

| Situation | Use |
|---|---|
| A few videos on your own machine | the open-source library or yt-dlp |
| A server, a scheduled job, an app, or thousands of videos | a hosted service, so you don't maintain proxies |
| Your own channel's captions | the official API |
