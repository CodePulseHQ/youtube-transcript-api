# YouTube Transcript API: examples for Python, JavaScript, curl, MCP and n8n

Get the transcript of any public YouTube video, playlist or channel, as clean text, timestamps, AI-ready chunks, Markdown, SRT or WebVTT. **No YouTube Data API key, no Google Cloud project, no proxies to run.**

This repository contains runnable examples and how-to guides for the **[YouTube Transcript API Actor on Apify](https://apify.com/codepulsehq/youtube-transcript-api)**, made by [CodePulse](https://codepulsehq.com). The examples call that hosted Actor, so you need a free [Apify](https://apify.com) account and API token. The code in this repo is MIT licensed; the Actor itself is a paid, hosted service ($3.90 per 1,000 transcripts, failed videos free).

## Quick start

```bash
export APIFY_TOKEN=...   # Apify Console > Settings > API & Integrations

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"], "includeSegments": false}'
```

You get back the transcript `text`, plus `title`, `channel`, `description`, `thumbnail_url`, `view_count`, the caption `language`, and whether the captions were `auto_generated`. Videos that can't be fetched return a row with `success: false`, an `error_code` and a plain-English `error`, and are not charged.

## Guides

| Question | Guide |
|---|---|
| How do I get a YouTube transcript without the YouTube Data API? | [docs/get-youtube-transcript-without-api-key.md](docs/get-youtube-transcript-without-api-key.md) |
| My script gets `RequestBlocked` / `IpBlocked` on AWS or a cloud server | [docs/fix-requestblocked-ipblocked-on-aws.md](docs/fix-requestblocked-ipblocked-on-aws.md) |
| How do I get transcripts for a RAG chatbot, with timestamps I can cite? | [docs/youtube-transcripts-for-rag.md](docs/youtube-transcripts-for-rag.md) |
| Is there a YouTube transcript MCP server for Claude / Cursor? | [docs/youtube-transcript-mcp-server.md](docs/youtube-transcript-mcp-server.md) |
| How do I bulk download transcripts for a channel or playlist? | [docs/bulk-download-channel-or-playlist-transcripts.md](docs/bulk-download-channel-or-playlist-transcripts.md) |
| How do I download YouTube subtitles as SRT or VTT? | [docs/youtube-subtitles-srt-vtt.md](docs/youtube-subtitles-srt-vtt.md) |
| How do the options compare (library, yt-dlp, official API, hosted)? | [docs/compare-youtube-transcript-options.md](docs/compare-youtube-transcript-options.md) |

## Examples

| File | What it does |
|---|---|
| [`examples/curl/get-transcript.sh`](examples/curl/get-transcript.sh) | One request, transcript back |
| [`examples/python/get_transcript.py`](examples/python/get_transcript.py) | Transcript with timestamped lines |
| [`examples/python/channel_to_markdown.py`](examples/python/channel_to_markdown.py) | Save a channel's latest videos as Markdown files |
| [`examples/python/rag_chunks.py`](examples/python/rag_chunks.py) | JSONL chunks for a vector database, each with a link to the exact second |
| [`examples/javascript/get-transcript.mjs`](examples/javascript/get-transcript.mjs) | Node.js version |
| [`examples/mcp/claude-desktop.json`](examples/mcp/claude-desktop.json) | MCP config so an AI agent can fetch transcripts itself |

Every Python and JavaScript example sets a spend cap on the run, so a typo can never become a big bill.

## Use it in no-code tools

In **n8n**, use an *HTTP Request* node: method `POST`, URL `https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items`, header `Authorization: Bearer YOUR_APIFY_TOKEN`, JSON body `{"videos": ["{{ $json.videoUrl }}"], "includeSegments": false}`. The transcript comes back in `text`. **Make** and **Zapier** have an Apify connector: add an Apify step, pick the *YouTube Transcript API* Actor and map the video link into its input. Details: [n8n, Make and Zapier page](https://apify.com/codepulsehq/youtube-transcript-api/examples/youtube-transcripts-for-n8n-make-zapier).

## Frequently asked questions

**Do I need a YouTube API key?** No.

**Does it work from AWS, Vercel and other cloud servers?** Yes. YouTube blocks most datacenter IPs, which is why plain scripts fail there; the Actor handles that for you. See the [fix guide](docs/fix-requestblocked-ipblocked-on-aws.md).

**Can it get a whole channel or playlist?** Yes. Pass a channel or playlist link and set `maxVideosPerSource` (up to 2,000).

**What if a video has no captions?** You get a `success: false` row with `error_code: "no_captions"` and you are not charged. The Actor reads captions YouTube already has; it does not transcribe audio.

**What does it cost?** $3.90 per 1,000 transcripts, so 10,000 is about $39. Failed videos are free, and Apify's free plan includes $5 of monthly credit.

**Is it legal?** It reads captions that YouTube shows publicly. How you use the text is up to you: respect creators' copyright and YouTube's terms. This is not legal advice.

## Input options

| Option | Description |
|---|---|
| `videos` | Video, playlist or channel links, or plain video IDs |
| `maxVideosPerSource` | Max videos per playlist or channel (default 50, up to 2,000) |
| `language` | Caption language code, e.g. `en`, `es`, `de` (falls back to the first available track) |
| `includeSegments` | Include a timestamped list of caption lines |
| `chunkSize` | Also return chunks of about this many characters, with start and end times |
| `outputFormats` | Extra formats: `markdown`, `srt`, `vtt` |

Full documentation, pricing and a try-it-now form are on the [Actor's Apify page](https://apify.com/codepulsehq/youtube-transcript-api).

## Feedback

Found a problem or want an example added? Open an issue here, or use the **Issues** tab on the Actor's Apify page and include the link that failed.
