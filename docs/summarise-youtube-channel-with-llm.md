---
layout: default
title: "Summarise every video on a YouTube channel with an LLM (Python)"
description: "Fetch transcripts for a channel, summarise each video with an LLM and ask questions across all of them. Python example."
---

# Summarise every video on a YouTube channel with an LLM (Python)

A channel posts 200 videos and you want to know what it actually says about a topic. Watching is out. Transcripts plus an LLM is the practical answer, and the pipeline is small: fetch transcripts, summarise each, then ask questions across them.

## Step 1: get the transcripts

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/youtube-transcript-api").call(run_input={
    "videos": ["https://www.youtube.com/@SomeChannel"],
    "maxVideosPerSource": 20,
    "includeSegments": False,
})
videos = [r for r in client.dataset(run.default_dataset_id).iterate_items() if r["success"]]
print(len(videos), "transcripts")
```

## Step 2: summarise each one

Use whichever LLM you prefer. This example uses the Anthropic SDK, with a character cap so very long videos don't blow the context:

```python
import anthropic

llm = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY

def summarise(v):
    msg = llm.messages.create(
        model="claude-haiku-5-5",
        max_tokens=400,
        messages=[{"role": "user", "content":
            f"Summarise this video transcript in 5 bullet points.\n\nTitle: {v['title']}\n\n{v['text'][:60000]}"}],
    )
    return msg.content[0].text

summaries = {v["url"]: summarise(v) for v in videos}
```

## Step 3: ask questions across all of them

Put the summaries in one prompt and ask. This works well for tens of videos. For hundreds, embed the transcripts instead: set `"chunkSize": 1000` in the Actor input to get each transcript pre-cut into chunks of about 1,000 characters, ready for a vector store.

```python
corpus = "\n\n".join(f"{u}\n{s}" for u, s in summaries.items())
q = "Which videos discuss pricing, and what do they recommend?"
answer = llm.messages.create(model="claude-haiku-5-5", max_tokens=600,
    messages=[{"role": "user", "content": f"{corpus}\n\nQuestion: {q}\nCite the URLs."}])
print(answer.content[0].text)
```

## Cost

Transcripts are about $3.90 per 1,000 videos, so 20 videos is under 8 cents. The LLM calls cost more than the transcripts, so cap `maxVideosPerSource` while you experiment.

## Tips

- Auto-generated captions have no punctuation and mangle names. Tell the model so in the prompt.
- Skip videos with `success: false`. Common reasons are no captions or a private video, and you aren't charged for them.
- Channel handles (`@name`) work as input. So do playlist links.

Actor page and full options: <https://apify.com/codepulsehq/youtube-transcript-api>
