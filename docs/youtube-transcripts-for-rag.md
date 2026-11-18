---
layout: default
title: "YouTube transcripts for RAG: chunking with timestamps you can cite"
description: "Turn YouTube videos into embedding-ready chunks with start and end times, and link every answer back to the exact second."
---

# YouTube transcripts for RAG: chunking with timestamps you can cite

To build a chatbot or search over YouTube videos you need three things: the transcript text, chunks small enough to embed, and a way to send the user back to the exact moment a chunk came from.

## 1. Get chunks with start and end times

Ask for chunks of about 1,000 characters. Each chunk keeps its `start` and `end` seconds:

```bash
curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"videos": ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"], "chunkSize": 1000, "includeSegments": false}'
```

```json
{
  "video_id": "UF8uR6Z6KLc",
  "title": "Steve Jobs' 2005 Stanford Commencement Address",
  "chunks": [
    { "index": 0, "start": 7.5, "end": 71.2, "text": "This program is brought to you by Stanford University..." }
  ]
}
```

## 2. Store metadata with each chunk

[`examples/python/rag_chunks.py`](../examples/python/rag_chunks.py) prints one JSON line per chunk, ready to load into any vector database:

```json
{"id": "UF8uR6Z6KLc-3", "text": "...", "metadata": {"title": "...", "channel": "...", "start": 203.1, "end": 262.4, "url": "https://www.youtube.com/watch?v=UF8uR6Z6KLc&t=203s"}}
```

Embed `text`. Keep `metadata` alongside the vector.

## 3. Cite the exact second

When a chunk is retrieved, show `metadata.url` (it ends in `&t=203s`) as the source link. The user lands at the right moment in the video.

## Tips

- **Chunk size:** 800 to 1,200 characters works well for most embedding models. Smaller chunks are more precise, larger chunks keep more context.
- **Whole-video prompts:** if you'd rather paste a transcript into an LLM prompt than embed it, use `"outputFormats": ["markdown"]`. You get Markdown with a timestamp link on every paragraph. See [YouTube transcripts as Markdown for LLMs](https://apify.com/codepulsehq/youtube-transcript-api/examples/youtube-transcripts-as-markdown-for-llms).
- **Auto-generated captions** have no punctuation guarantees and can contain recognition errors. The result includes `auto_generated` so you can treat those videos differently.
- **Cache** by video ID. A transcript never changes, so you only need to embed it once.

Ready-made page: [YouTube transcripts for AI and RAG](https://apify.com/codepulsehq/youtube-transcript-api/examples/youtube-transcripts-for-ai-rag).
