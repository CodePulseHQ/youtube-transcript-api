---
layout: default
title: "YouTube transcript MCP server for Claude, Cursor and AI agents"
description: "Let Claude, Cursor or any MCP client fetch YouTube transcripts itself, with a two-line config and no server to host."
---

# YouTube transcript MCP server for Claude, Cursor and other AI agents

Let your AI agent fetch the transcript of any YouTube video itself. Apify's MCP server exposes an Actor as a tool, so there's nothing to install or host.

## Set up

Add this to your MCP client's settings (Claude Desktop, Cursor, VS Code and others). The first time, it opens a browser to sign in to Apify:

```json
{
  "mcpServers": {
    "youtube-transcripts": {
      "url": "https://mcp.apify.com?tools=codepulsehq/youtube-transcript-api"
    }
  }
}
```

Prefer a token to a browser sign-in? Use [`examples/mcp/with-token.json`](../examples/mcp/with-token.json), which adds an `Authorization: Bearer` header.

## Try it

Ask your agent:

> Get the transcript of https://www.youtube.com/watch?v=UF8uR6Z6KLc and list the three main points.

> Summarise the last 5 videos on https://www.youtube.com/@TED.

The agent passes the link to the Actor and reads back the transcript. Playlists and channels work too, and failed videos are free.

## Good to know

- You need a free Apify account. Runs are pay per transcript ($3.90 per 1,000), and Apify's free plan includes $5 of monthly credit.
- It reads the captions YouTube already has. Videos without captions return a clear `no_captions` reason.
- The Apify MCP server also has a general tool for running any Actor, so the agent can combine transcripts with other data sources.

See also: [Apify's MCP server documentation](https://docs.apify.com/platform/integrations/mcp).
