---
layout: default
title: "Bulk download transcripts for a YouTube channel or playlist"
description: "Get the transcript of every video in a channel or playlist in one run, with a spend cap, plus the DIY route with yt-dlp."
---

# How to bulk download transcripts for a YouTube channel or playlist

## With the Actor (one run)

Paste a channel or playlist link and set how many videos you want. Newest videos come first:

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/@TED"], "maxVideosPerSource": 25, "includeSegments": false}'
```

- Accepted links: channel (`youtube.com/@name`, `/channel/UC...`), playlist (`youtube.com/playlist?list=...`), single videos, or plain video IDs. You can mix them.
- `maxVideosPerSource` is capped at 2,000. It stops a big channel from running up a surprise bill.
- Videos without captions come back as `success: false` rows with a reason and cost nothing.
- For long jobs use the asynchronous `/runs` endpoint (the `run-sync` endpoint returns within 5 minutes). The [Python example](../examples/python/channel_to_markdown.py) uses the client library, which waits as long as needed, and saves one Markdown file per video.

Ready-made pages: [whole channel](https://apify.com/codepulsehq/youtube-transcript-api/examples/download-youtube-channel-transcripts) and [whole playlist](https://apify.com/codepulsehq/youtube-transcript-api/examples/youtube-playlist-transcripts).

## Do it yourself

- List the videos: `yt-dlp --flat-playlist --print id "https://www.youtube.com/@TED/videos"` prints the IDs. Or use the YouTube Data API's `playlistItems.list` on the channel's uploads playlist.
- Then fetch each transcript with a library or `yt-dlp --skip-download --write-auto-subs`. Run from a server and you'll hit [IP blocks](fix-requestblocked-ipblocked-on-aws.md).
