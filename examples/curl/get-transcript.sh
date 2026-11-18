#!/usr/bin/env bash
# Get a YouTube transcript with one request. Needs an Apify API token (free account):
#   export APIFY_TOKEN=...   (Apify Console > Settings > API & Integrations)
set -euo pipefail
VIDEO="${1:-https://www.youtube.com/watch?v=UF8uR6Z6KLc}"

curl -sS -X POST \
  "https://api.apify.com/v2/acts/codepulsehq~youtube-transcript-api/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"videos\": [\"${VIDEO}\"], \"includeSegments\": false}"
