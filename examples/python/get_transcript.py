"""Get the transcript of a YouTube video.

    pip install apify-client
    export APIFY_TOKEN=...
    python get_transcript.py https://www.youtube.com/watch?v=UF8uR6Z6KLc
"""
import os
import sys

from apify_client import ApifyClient

video = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=UF8uR6Z6KLc"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/youtube-transcript-api").call(
    max_total_charge_usd=1,  # never spend more than $1 on this run
    logger=None,  # quiet: do not stream the Actor log
    run_input={"videos": [video], "includeSegments": True}
)

for item in client.dataset(run.default_dataset_id).iterate_items():
    if not item["success"]:
        print(f"Could not fetch {item['input']}: {item['error']}")
        continue
    print(item["title"], "-", item["channel"])
    print(item["text"][:500], "...")
    for line in item["segments"][:3]:
        print(f"  [{line['start']:.1f}s] {line['text']}")
