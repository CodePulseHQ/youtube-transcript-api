"""Save the latest videos of a channel (or a playlist) as Markdown files.

    pip install apify-client
    export APIFY_TOKEN=...
    python channel_to_markdown.py https://www.youtube.com/@TED 10
"""
import os
import pathlib
import sys

from apify_client import ApifyClient

source = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/@TED"
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("codepulsehq/youtube-transcript-api").call(
    max_total_charge_usd=1,  # never spend more than $1 on this run
    logger=None,  # quiet: do not stream the Actor log
    run_input={
        "videos": [source],
        "maxVideosPerSource": limit,
        "outputFormats": ["markdown"],
        "includeSegments": False,
    }
)

out = pathlib.Path("transcripts")
out.mkdir(exist_ok=True)
saved = 0
for item in client.dataset(run.default_dataset_id).iterate_items():
    if not item["success"]:
        print("skipped", item["input"], "-", item["error_code"])
        continue
    (out / f"{item['video_id']}.md").write_text(item["markdown"], encoding="utf-8")
    saved += 1
print(f"saved {saved} transcripts to {out}/")
