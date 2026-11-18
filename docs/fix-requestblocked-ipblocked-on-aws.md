---
layout: default
title: "Fix YouTube transcript RequestBlocked and IpBlocked on AWS and cloud servers"
description: "Why YouTube transcript scripts work locally but fail on AWS, Vercel or a VPS, and five ways to fix it, from caching to residential proxies to a hosted API."
---

# Fix: YouTube transcript script works locally but gets RequestBlocked / IpBlocked on AWS or a cloud server

**Symptoms**

- `youtube_transcript_api._errors.RequestBlocked` or `IpBlocked`
- "Sign in to confirm you're not a bot"
- A transcript that comes back empty, or only works for the first few videos
- It runs fine on your laptop and fails the moment you deploy to AWS, GCP, Azure, Vercel, Railway or a VPS

**Cause:** YouTube rate-limits and blocks IP addresses that belong to datacenters. Your home connection looks like a person. A cloud server looks like a bot, even when you send one request. In our own tests from a datacenter, a fresh IP got a few requests through and then every request was refused.

## Fixes, from cheapest to most reliable

1. **Cache everything.** A transcript never changes. Store results by video ID and never fetch the same video twice.
2. **Slow down and retry.** Space requests out and back off on errors. This helps with rate limits, but not with a blocked IP range.
3. **Use a residential proxy.** Route requests through residential IPs. With `youtube-transcript-api` (v1.x) pass a proxy config; check the library's README for the current syntax:

   ```python
   from youtube_transcript_api import YouTubeTranscriptApi
   from youtube_transcript_api.proxies import GenericProxyConfig

   api = YouTubeTranscriptApi(
       proxy_config=GenericProxyConfig(
           http_url="http://USER:PASS@proxy.example.com:8000",
           https_url="http://USER:PASS@proxy.example.com:8000",
       )
   )
   transcript = api.fetch("UF8uR6Z6KLc")
   ```

   With `yt-dlp`, add `--proxy http://USER:PASS@proxy.example.com:8000`. Cheap datacenter proxies are usually blocked too, so use residential ones. A transcript is small, roughly tens of kilobytes, so proxy cost per video is low.
4. **Run it from a home or office connection** (a small machine on a normal broadband line). Fine for low volume, but unreliable and not something to depend on.
5. **Use a hosted service** that already handles blocking, retries and proxies, so your code stays one HTTP call:

   ```bash
   curl -sS -X POST \
     "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
     -H "Content-Type: application/json" \
     -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"]}'
   ```

   Failed videos are not charged. See the [cloud-servers example](https://apify.com/codepulsehq/youtube-transcript-api/examples/youtube-transcripts-that-work-from-cloud-servers).

## How do I know which problem I have?

- Works for the first video, fails for the rest: IP reputation or rate limit. Fix 3 or 5.
- "No transcripts found" or `NoTranscriptFound`: the video has no captions in that language. That is not a block. Request another language, or accept that the video has none.
- `VideoUnavailable`: private, deleted or region-locked video.
