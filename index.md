---
layout: default
title: "YouTube Transcript API: get transcripts of any video, playlist or channel"
description: "Get YouTube transcripts without the YouTube Data API. Examples and guides for Python, JavaScript, curl, MCP and n8n. Works from AWS and cloud servers. Pay per transcript, failures free."
---

<div class="hero">
  <h1>Get the transcript of any YouTube video, playlist or channel</h1>
  <p class="lead">Clean text, timestamps, RAG-ready chunks, Markdown, SRT and VTT. No YouTube API key, no Google Cloud project, and no proxies to run. Works from AWS and other cloud servers.</p>
  <a class="cta" href="https://apify.com/codepulsehq/youtube-transcript-api">Try it on Apify</a>
  <a class="cta secondary" href="https://github.com/CodePulseHQ/youtube-transcript-api">Examples on GitHub</a>
</div>

$3.90 per 1,000 transcripts. Videos without captions and failed requests are free, and Apify's free plan includes $5 of monthly credit. Made by [CodePulse](https://codepulsehq.com); these pages document our hosted Actor.

## Quick start

```bash
export APIFY_TOKEN=...   # free Apify account: Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"], "includeSegments": false}'
```

You get the transcript `text`, plus title, channel, description, thumbnail, view count, the caption language, and whether the captions were auto-generated. A video that can't be fetched comes back as a row with `success: false` and a plain-English reason, and is not charged.

## Guides {#guides}

<div class="cards">
  <div class="card"><h3><a href="docs/summarise-youtube-channel-with-llm.md">Summarise a whole YouTube channel with an LLM</a></h3><p>Fetch transcripts for a channel, summarise each video with an LLM and ask questions across all of them.</p></div>
  <div class="card"><h3><a href="docs/get-youtube-transcripts-in-python.md">How to get YouTube transcripts in Python</a></h3><p>Get YouTube transcripts in Python with a few lines of code, for videos, playlists and whole channels, without getting blocked on cloud servers.</p></div>
  <div class="card"><h3><a href="docs/get-youtube-transcript-without-api-key.md">Without the YouTube Data API</a></h3><p>Why the official API can't do it, and the one-request alternative.</p></div>
  <div class="card"><h3><a href="docs/fix-requestblocked-ipblocked-on-aws.md">Fix RequestBlocked / IpBlocked</a></h3><p>Why scripts fail on AWS and cloud servers, and five fixes.</p></div>
  <div class="card"><h3><a href="docs/youtube-transcripts-for-rag.md">Transcripts for RAG</a></h3><p>Chunks with start and end times, so answers cite the exact second.</p></div>
  <div class="card"><h3><a href="docs/youtube-transcript-mcp-server.md">MCP server for AI agents</a></h3><p>Let Claude or Cursor fetch transcripts with a two-line config.</p></div>
  <div class="card"><h3><a href="docs/bulk-download-channel-or-playlist-transcripts.md">Bulk channel and playlist downloads</a></h3><p>Every video in a channel or playlist in one run, with a spend cap.</p></div>
  <div class="card"><h3><a href="docs/youtube-subtitles-srt-vtt.md">SRT and VTT subtitles</a></h3><p>Captions as subtitle files, without downloading the video.</p></div>
  <div class="card"><h3><a href="docs/compare-youtube-transcript-options.md">Compare the options</a></h3><p>Library, yt-dlp, official API and hosted services side by side.</p></div>
</div>

## Frequently asked questions

**Do I need a YouTube API key?** No.

**Does it work from AWS, Vercel and other cloud servers?** Yes. YouTube blocks most datacenter IP addresses, which is why plain scripts fail there. The Actor handles that for you. See the [fix guide](docs/fix-requestblocked-ipblocked-on-aws.md).

**Can it get a whole channel or playlist?** Yes. Pass a channel or playlist link and set `maxVideosPerSource` (up to 2,000).

**What if a video has no captions?** You get a `success: false` row with `error_code: "no_captions"` and you are not charged. The Actor reads captions YouTube already has; it does not transcribe audio.

**What does it cost?** $3.90 per 1,000 transcripts, so 10,000 is about $39. Failed videos are free.

**Is it legal?** It reads captions that YouTube shows publicly. How you use the text is up to you: respect creators' copyright and YouTube's terms. This is not legal advice.

## More from CodePulse

- [SEC EDGAR API](https://apify.com/codepulsehq/sec-edgar-api): 10-K text as Markdown, financials, insider trades and 13F holdings.
- [US Federal Opportunities API](https://apify.com/codepulsehq/us-federal-opportunities-api): SAM.gov contracts, Grants.gov grants and award winners.
- [Domain Intelligence API](https://apify.com/codepulsehq/domain-intelligence-api): WHOIS expiry, DNS, SSL, SPF/DKIM/DMARC and tech stack.
- [Speech to Text API](https://apify.com/codepulsehq/speech-to-text-api): transcribe audio and video that has no captions, from $0.24 an hour.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Do I need a YouTube API key to get a transcript?", "acceptedAnswer": {"@type": "Answer", "text": "No. Send the video link to the Actor and read the transcript back. No Google Cloud project, API key or OAuth is needed."}},
    {"@type": "Question", "name": "Does it work from AWS and other cloud servers?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. YouTube blocks most datacenter IP addresses, which is why plain scripts fail there. The Actor handles that, so transcripts keep coming back from the cloud."}},
    {"@type": "Question", "name": "Can it get the transcripts of a whole YouTube channel or playlist?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Pass a channel or playlist link and set maxVideosPerSource, up to 2,000."}},
    {"@type": "Question", "name": "What happens if a video has no captions?", "acceptedAnswer": {"@type": "Answer", "text": "You get a row with success false and error code no_captions, and you are not charged. The Actor reads captions YouTube already has; it does not transcribe audio."}},
    {"@type": "Question", "name": "How much does it cost?", "acceptedAnswer": {"@type": "Answer", "text": "$3.90 per 1,000 transcripts, so 10,000 transcripts is about $39. Failed videos and videos without captions are free."}}
  ]
}
</script>
