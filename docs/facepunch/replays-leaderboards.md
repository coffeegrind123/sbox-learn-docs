---
title: Ghost Replays via Movie Maker + Stats Data
slug: facepunch/replays-leaderboards
url: https://sbox.game/learn/facepunch/replays-leaderboards
author: Facepunch
author_slug: facepunch
topic: Capable
content_type: Text
tags: [code, data, ghost, maker]
rating: 4
views: 704
upvotes: 7
downvotes: 0
updated: 'Updated

  12 Days Ago'
summary: How to leverage storing information in stats to make a ghost replay system
  powered by Movie Maker.
scraped_at: '2026-06-28T08:55:43Z'
---

# Ghost Replays via Movie Maker + Stats Data

> How to leverage storing information in stats to make a ghost replay system powered by Movie Maker.

# Ghost Replays via Movie Maker + Stats

## What we're doing

We want to make a *ghost*: a replay of how a player moved, that other people can watch back. Movie Maker can record any object's motion over time into a `MovieClip`. We record the player while they run, save that clip, and attach it to a leaderboard stat. Anyone can then pull the clip back off the leaderboard and play it.

## The flow:

- Start recording the player object's movement
- Stop the recording when finished
- Save the clip out (serialize it)
- Send a stat with the clip attached
- Fetch the clip from the leaderboard and play it on a ghost

## Start recording

Point a recorder at the player object. Its transform is captured automatically every fixed update.

```
using Sandbox.MovieMaker;

var options = new MovieRecorderOptions()
    .WithCaptureGameObject( player, trackName: "Player" );

var recorder = new MovieRecorder( Scene, options );

recorder.Start();
```

## Stop recording

When the run finishes, stop and pull the recording out as a clip.

```
recorder.Stop();

MovieClip clip = recorder.ToClip();
```

## Save the clip out

Serialize the clip to a JSON string so it can travel with a stat.

```
var clipJson = Json.Serialize( clip.ToResource() );
```

## Send a stat

Submit the score (e.g. lap time) and attach the clip as data. The recording is now part of that leaderboard entry.

```
using Sandbox.Services;

Stats.SetValue( "laptime-my-map", time, new Dictionary<string, object>
{
    ["ClipJson"] = clipJson
} );
```

## Fetch and play it back

Read the leaderboard, download the attached data from the entry's `DataUrl`, and rebuild the clip.

```
var board = Leaderboards.GetFromStat( "laptime-my-map" );
board.SetSortAscending();
board.SetAggregationMin();
board.MaxEntries = 10;
await board.Refresh();

var entry = board.Entries.First(); 
if ( string.IsNullOrEmpty( entry.DataUrl ) )
    return;

var data     = await Http.RequestStringAsync( entry.DataUrl );
var clipJson = Json.Deserialize<Dictionary<string, object>>( data )["ClipJson"].ToString();
var resource = Json.Deserialize<EmbeddedMovieResource>( clipJson );
```

Play it on a ghost GameObject, not a real player. Rebind the recording's root track to the ghost.

```
var ghost  = ghostPrefab.Clone();
var player = ghost.AddComponent<MoviePlayer>();

var clip = resource.Compiled;
var track = clip.GetReference<GameObject>( "Player" );

player.Binder.Add( track, ghost ); 
player.Play( clip );
player.IsLooping = true;
```

## Notes

- Attached stat `data` is meant for small JSON. Keep recordings short - a rolling `BufferDuration` on the recorder caps clip length.
- `entry.DataUrl` is null when that entry submitted no data — always guard it.
- Without the `Binder.Add` retarget, playback animates the original object instead of the ghost.
