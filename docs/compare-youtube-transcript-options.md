---
layout: default
title: "YouTube transcript API comparison: library vs yt-dlp vs official API vs hosted"
description: "How the open-source libraries, yt-dlp, the official YouTube Data API and hosted services compare on cost, cloud reliability, playlists and output formats."
---

# Comparing ways to get YouTube transcripts

Written by the team that makes the Actor linked below, so weigh it accordingly. The comparison is about the approach, not about naming competitors.

| | Open-source library (`youtube-transcript-api`) | `yt-dlp` | Official YouTube Data API | Hosted service / Actor |
|---|---|---|---|---|
| Cost | Free, plus your servers and proxies | Free, plus your servers and proxies | Free quota | Per transcript. This Actor: $3.90 per 1,000 |
| Transcripts of other people's videos | Yes | Yes | **No**, only videos you own or manage | Yes |
| Works from cloud servers | Often blocked without residential proxies | Often blocked without residential proxies | Yes | Yes, handled for you |
| Playlists and channels | You write the loop | Yes, flat-playlist listing | Listing yes, transcripts no | Yes, one run |
| Output formats | Text and timestamps | VTT / SRT / JSON files | Caption files (owner only) | Text, timestamps, chunks, Markdown, SRT, VTT |
| What you maintain | Proxies, retries, fixes when YouTube changes | Same | OAuth, quotas | Nothing |
| Best for | Laptops, prototypes, a few videos | Archiving and one-off downloads | Your own channel | Servers, apps, automations, scale |

## Cost at volume (this Actor)

| Transcripts | Cost |
|---|---|
| 1,000 | $3.90 |
| 10,000 | $39 |
| 100,000 | $390 |

Videos without captions and failed requests are not charged, and a per-run spend cap is supported.

## Honest limits of every approach

- All of them read **existing captions**. A video without captions has nothing to return. None of them transcribe audio.
- Auto-generated captions can contain errors and have no punctuation guarantees.
- Private, age-restricted or deleted videos can't be fetched.

[Try the Actor](https://apify.com/codepulsehq/youtube-transcript-api)
