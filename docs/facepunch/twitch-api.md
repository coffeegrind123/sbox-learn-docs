---
title: Introduction to the Streamer Api
slug: facepunch/twitch-api
url: https://sbox.game/learn/facepunch/twitch-api
author: Facepunch
author_slug: facepunch
topic: Capable
content_type: Text
tags: [gameplay, service, streamer, streaming]
rating: 4
views: 819
upvotes: 9
downvotes: 0
updated: 'Updated

  19 Days Ago'
summary: How to make a game that Twitch viewers can interact with
scraped_at: '2026-06-26T09:31:04Z'
---

# Introduction to the Streamer Api

> How to make a game that Twitch viewers can interact with

# Reacting to your Twitch chat in s&box

We added a streaming API to s&box so your game can read your Twitch chat and turn it into gameplay. This is a quick tour of what the API can do, with code.

## The shape of it

There are only two things to learn:

- **You listen to events** by implementing the `Streamer.IEvents` interface on a Component or Panel. Viewer joined, viewer left, viewer said something, someone subscribed, someone raided you. That sort of thing.
- **You read the current state** off the static `Streamer` class. Are we live, who's in chat, what's the title, how many viewers.

That's the whole API.

## **Getting connected**

You don't write any connection code. You don't ask for a channel name or a token. It just connects to *your* channel when you go live. Two things make that happen:

- **Mark your game as streamer game** - in your game's project settings.
- **The streamer links their Twitch account in game** - after that the client connects to their chat automatically.

From the game side you never see any of this. You just check:

```
if ( Streamer.IsActive )
{
    // we're connected to a service and reading chat
}
```

## **Listening to chat**

Implement `Streamer.IEvents` on any `Component`. The engine dispatches these to the active scene.

Every method has a default empty implementation, so only override the ones you care about.

```
public class MyStreamThing : Component, Streamer.IEvents
{
    void Streamer.IEvents.OnStreamMessage( Streamer.ChatMessage message )
    {
        Log.Info( $"{message.Viewer.DisplayName}: {message.Message}" );
    }
}
```

## **The events**

These are the events you can implement from Streamer.IEvents

```
void OnStreamJoin( Viewer viewer ); 
void OnStreamLeave( Viewer viewer );
void OnStreamMessage( ChatMessage message );
void OnStreamSubscribe( SubscribeMessage message ); 
void OnStreamGiftSubscribe( GiftSubscribeMessage message );  
void OnStreamGiftSubscriptions( GiftSubscriptionsMessage message ); 
void OnStreamRaid( RaidMessage message );
```

Something to note is that leaves aren't super reliable**.** Twitch doesn't reliably tell us when someone leaves, but we do our best. Joins aren't perfect either.  
  
The best thing you can do is design a game where users opt into something in the chat by typing something like addme, and then adding them to a game. Chat messages are reliable.  
  
This isn't to say that you shouldn't use the Viewer list, because it does work.. it's just a warning that it isn't always perfect.

## 

## **Turning chat into actions**

Read the message, do a thing. Easy, simple.

```
void Streamer.IEvents.OnStreamMessage( Streamer.ChatMessage message )
{
    var viewer = message.Viewer;

    switch ( message.Message )
    {
        case "spawn": SpawnAvatar( viewer ); break;
        case "go":    MoveForward( viewer );  break;
        case "poop":  Poop( viewer );         break;
    }
}
```

`ChatMessage` gives you everything about that one message:

```
message.Viewer          // who sent it (see below)
message.Message         // the text
message.Channel         // which channel
message.Bits            // bits cheered, or 0
message.IsFirstMessage  // their first ever message in this chat
message.Time            // when it arrived
```

`IsFirstMessage` is nice for a welcome.. confetti for a first timer, that kind of thing.

## **The Viewer**

A `Viewer` is one person in your chat. The same object sticks around for as long as they're in chat, so you can use it as dictionary indexes etc.

```
viewer.Username      // login name, lowercase — but they can change it
viewer.StreamerId    // stable numeric id — use THIS to persist anything
viewer.DisplayName   // what to show on screen
viewer.Color         // their chat colour (nullable)
viewer.Badges        // raw badge strings

viewer.IsBroadcaster // it's you
viewer.IsModerator
viewer.IsSubscriber
viewer.IsVip
```

Use `StreamerId`, not `Username`, as a key for anything you save to disk because people rename themselves.

The badge helpers are handy for gating commands to mods:

```
if ( message.Message == "reset" && message.Viewer.IsModerator )
    ResetEverything();
```

## **Per-viewer data**

Every viewer has a `Data` bag you can stash gameplay state in.  You can store any object on it.

```
// give them a point
viewer.Data.Set( "score", viewer.Data.Get( "score", 0 ) + 1 );
```

**This bag is temporary.** It lives as long as the viewer is in the roster. If they leave and come back, it's a fresh viewer with an empty bag. 

## **Reading the stream**

The static `Streamer` class is the current state of your broadcast.

```
Streamer.IsActive       // connected to a service?
Streamer.Service        // StreamService.Twitch

Streamer.Viewers        // everyone currently in chat (IReadOnlyList<Viewer>)
Streamer.ViewerCount    // concurrent viewer count on the stream

Streamer.Title          // stream title
Streamer.Game           // category / game
Streamer.StartedAt      // when you went live (DateTimeOffset)
Streamer.Tags           // stream tags
Streamer.IsMature       // mature flag

Streamer.Username       // your name
Streamer.UserId         // your id
```

So an uptime readout is just:

```
var uptime = DateTime.UtcNow - Streamer.StartedAt
```

`Streamer.Viewers` is a **best-effort list of active chatters, not lurkers** .. silent viewers don't show up. It's a snapshot.. don't hold onto it across frames, just read it again when you need it.

A couple of things you can set, not just read:

```
Streamer.Language = "en";   // set the stream language
Streamer.Delay = 0;         // set stream delay
```
