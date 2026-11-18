// Get the transcript of a YouTube video.
//
//   npm install apify-client
//   export APIFY_TOKEN=...
//   node get-transcript.mjs https://www.youtube.com/watch?v=UF8uR6Z6KLc
import { ApifyClient } from 'apify-client';

const video = process.argv[2] ?? 'https://www.youtube.com/watch?v=UF8uR6Z6KLc';
const client = new ApifyClient({ token: process.env.APIFY_TOKEN });

const run = await client.actor('codepulsehq/youtube-transcript-api').call(
  { videos: [video], includeSegments: false },
  { maxTotalChargeUsd: 1, log: null }, // never spend more than $1; don't stream the Actor log
);

const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
  if (!item.success) {
    console.log(`Could not fetch ${item.input}: ${item.error}`);
    continue;
  }
  console.log(`${item.title} - ${item.channel}`);
  console.log(item.text.slice(0, 500), '...');
}
