---
layout: default
title: "How to get YouTube transcripts in Python (without getting blocked)"
description: "Get YouTube transcripts in Python with a few lines of code, for videos, playlists and whole channels, without getting blocked on cloud servers."
---

You want the transcript of a YouTube video as text. Maybe for a summary, a search index, or training data for an LLM. The obvious route is a small library, and it works on your laptop. Then you move it to a server and it stops, because YouTube blocks most datacenter IP addresses after a request or two.

This post shows the short way: call a hosted API from Python, get text back, and let someone else deal with the blocking.

## The quick version

Install the Apify client and set a token (a free Apify account is enough; the token is under Settings, API & Integrations):

```bash
pip install apify-client
export APIFY_TOKEN=your_token_here
```

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])

run = client.actor("codepulsehq/youtube-transcript-api").call(
    run_input={"videos": ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"], "includeSegments": False}
)

for row in client.dataset(run.default_dataset_id).iterate_items():
    if row["success"]:
        print(row["title"], "-", row["channel"])
        print(row["text"][:300])
    else:
        print("failed:", row["error_code"], row["error"])
```

Each row has the title, channel, duration, language, whether the captions were auto-generated, and the full `text`. Failures come back as rows with an `error_code` instead of crashing the run, and you are not charged for them.

## Whole channels and playlists

`videos` takes a mix of video links, playlist links, channel links or handles. Set `maxVideosPerSource` so a huge channel can't run up a big bill:

```python
run_input = {
    "videos": ["https://www.youtube.com/@SomeChannel"],
    "maxVideosPerSource": 25,   # newest first
    "language": "en",
    "includeSegments": False,   # skip per-line timestamps if you only need text
}
```

## Subtitles and timestamps

Need timestamps or subtitle files? Leave `includeSegments` on to get each caption line with its start time and duration. Ask for `"outputFormats": ["srt", "vtt", "markdown"]` to get ready-made files in the row.

## Why not just use a library?

Libraries that scrape YouTube directly are free and fine for a few videos from your own machine. They tend to fail at scale because requests from cloud IP ranges get blocked. A hosted service uses residential proxies and retries for you. That's the part you're paying for: about $3.90 per 1,000 transcripts here, and failed ones are free.

## Repeat videos are cheaper to fetch

The Actor keeps a copy of each transcript in a storage in your own Apify account (30 days), so asking for the same video again is instant and uses no proxy. Turn it off with `"useCache": false` if you always want a fresh copy.

## Next steps

- Feed `text` to an LLM for summaries: see [Summarise a whole YouTube channel with an LLM](https://codepulsehq.github.io/youtube-transcript-api/docs/summarise-youtube-channel-with-llm.html).
- Full input options and output fields: <https://apify.com/codepulsehq/youtube-transcript-api>
- More examples (curl, JavaScript, MCP): <https://codepulsehq.github.io/youtube-transcript-api/>

*Not affiliated with YouTube. Respect the creators' rights and YouTube's terms when you use transcripts.*
