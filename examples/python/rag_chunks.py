"""Turn YouTube videos into JSONL chunks for a vector database, each with a link to the exact second.

    pip install apify-client
    export APIFY_TOKEN=...
    python rag_chunks.py https://www.youtube.com/watch?v=UF8uR6Z6KLc > chunks.jsonl

Each line:
  {"id": "UF8uR6Z6KLc-3", "text": "...", "metadata": {"title": ..., "url": "...&t=123s", ...}}
Embed `text`, store `metadata`, and when a chunk is retrieved show `metadata.url` as the citation.
"""
import json
import os
import sys

from apify_client import ApifyClient

videos = sys.argv[1:] or ["https://www.youtube.com/watch?v=UF8uR6Z6KLc"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/youtube-transcript-api").call(
    max_total_charge_usd=1,  # never spend more than $1 on this run
    logger=None,  # quiet: do not stream the Actor log
    run_input={"videos": videos, "chunkSize": 1000, "includeSegments": False}
)

for item in client.dataset(run.default_dataset_id).iterate_items():
    if not item["success"]:
        print(f"skipped {item['input']}: {item['error']}", file=sys.stderr)
        continue
    for chunk in item["chunks"]:
        print(
            json.dumps(
                {
                    "id": f"{item['video_id']}-{chunk['index']}",
                    "text": chunk["text"],
                    "metadata": {
                        "title": item["title"],
                        "channel": item["channel"],
                        "video_id": item["video_id"],
                        "start": chunk["start"],
                        "end": chunk["end"],
                        "url": f"{item['url']}&t={int(chunk['start'])}s",
                    },
                },
                ensure_ascii=False,
            )
        )
