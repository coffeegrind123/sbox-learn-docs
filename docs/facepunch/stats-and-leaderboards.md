---
title: How do I use the Stats System?
slug: facepunch/stats-and-leaderboards
url: https://sbox.game/learn/facepunch/stats-and-leaderboards
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Coding
content_type: Text
tags: [code, data, info, leaderboard]
rating: 2
views: 288
upvotes: 2
downvotes: 0
updated: 'Updated

  10 Days Ago'
summary: A brief insight on how to make use of s&box's stats service.
scraped_at: '2026-06-28T08:55:43Z'
---

# How do I use the Stats System?

> A brief insight on how to make use of s&box's stats service.

# Stats

Stats are how your game records numbers that persist on the backend - enemies killed, laps done, best times. You submit values while playing, s&box ingests them, and you can read them back per-player or as globally. They're also the source leaderboards are built from.

## Define your stats

Stats are automatically created when you set them via code, so you don't have to set them up manually.

## Submit values

There are two calls, depending on the kind of number:

`Stats.Increment( "enemies-killed", 1 )` - adds to a running total. Use it for things that accumulate.  
`Stats.SetValue( "best-time", 42.3f )` - writes a specific value. Use it for a record or current level.

Both take an optional data dictionary as a final argument if you want to attach a small blob of JSON to the submission.

```
Stats.SetValue("best-time", 42.3f, new Dictionary<string, object> { ["ReplayJson"] = json });
```

Note: stats only count for the local player, so you'll have to use a RPC to make sure it's on the correct player.  
  
Refer to [Ghost Replays via Movie Maker + Stats](https://sbox.game/learn/facepunch/replays-leaderboards) for a really useful way of using stats data.

## Read your stats

Refresh the local player, then read a value. A PlayerStat carries more than the raw number:

```
await Stats.LocalPlayer.Refresh();
var stat = Stats.LocalPlayer.Get( "enemies-killed" );
```

From that you get, among others:

`stat.Sum` - total across all submissions.  
`stat.Max` - best single run.  
`stat.Min, stat.Avg, stat.LastValue` - exactly what they sound like.

There's also `Stats.LocalPlayer.TryGet( "best-time", out var best )` if the stat might not exist yet.

## Read global stats

Stats.Global works the same way but is summed across everyone who plays:

```
await Stats.Global.Refresh();
var killed = Stats.Global.Get( "enemies-killed" );
```

It adds population-wide fields like `killed.Players` (how many people contributed) and `killed.Avg.`

## Map-scoped stats

For per-map values there's a Stats.Map shortcut that keys everything to the current map package automatically:

```
Stats.Map.SetValue( "laps", 1 );
var laps = Stats.Map.GetLocal( "laps" );
```
