---
title: Multiplayer 101 - Easy as pie!
slug: jogamedev/multiplayer-101
url: https://sbox.game/learn/jogamedev/multiplayer-101
author: jogamedev
author_slug: jogamedev
topic: Capable
content_type: Text
tags: [multiplayer, network, synchronize]
rating: 2
views: 95
upvotes: 1
downvotes: 0
updated: 'Updated

  2 Days Ago'
summary: A super-simple guide to make a multiplayer game quickly!
scraped_at: '2026-06-04T10:02:31Z'
---

# Multiplayer 101 - Easy as pie!

> A super-simple guide to make a multiplayer game quickly!

## Making a Multiplayer game has never been so easy!

You really only need to answer two questions:  
  
1. What needs to be synchronized between clients?  
2. Who *owns* each object that needs to be synchronized?  
  
Ownership just means *which client determines the ground truth about an object (where it is, what it's stats are, etc).*  
Let's imagine a tank battle game.  Answering these questions would look like:

- Synchronized: The player's tank, it's projectiles and ammo pickups.
- Ownership: Each player *owns* their own tank and projectiles. The host owns ammo pickups and how they spawn.

Here's how to choose what gets synchronized:  
  
By default, everything is set to `NetworkMode.Snapshot` which means:

> The host will send this game object as part of the initial scene snapshot when a client joins the game

This is the default because many things do *not* need to be constantly sent over the network (level geometry for example).  
  
However, each players' character *does* need to be sent over the network (synchronized). So for that you'll need   
  
`NetworkMode.Object`

> The game object will be sent to other clients as its own networked object which can have synchronized properties and RPCs

You can read more about NetworkModes in the official docs: <https://sbox.game/dev/doc/networking/networked-objects>

The only other concept you need to know to get started is how to send Networked Messages and Sync Properties e.g. "How to make stuff happen on every client's computer".  
  
For example, say your tank rolls over a button that opens a vault door.  The tank is synchronized, but the vault doesn't have to be, you could just send the OpenVaultDoor() message to all clients.  Here's how that works: (it's laughably simple!)  
  
All you have to do is add an RPC attribute to the function that you want invoked on all clients like so:

```
[Rpc.Broadcast]
public void OpenVaultDoor()
{
	// Open the door
}
```

Rpc.Broadcast invokes the function for *everyone.* While Rpc.Owner invokes the function for only the owner of the networked object (PickupAmmo() in our imaginary tank game would be a good example to use Rpc.Owner on if the host owns all the ammo spawns) and Rpc.Host invokes the function only on the host.  
  
Read more about RPC Messages in the official docs: <https://sbox.game/dev/doc/networking/rpc-messages>

Remember, the owner of an object is not necessarily the host of the lobby.  "Client 2" is the Owner of their own Player Controller.

You can also sync component's properties:

```
public class Tank : Component
{
  [Sync] public int Kills { get; set; }
}
```

Read more about Syncing properties here: <https://sbox.game/dev/doc/networking/sync-properties>  
  
Lastly, you'll want to add a Network Helper component that determines:  
1. What each player spawns in as (a Tank, a Fish, whatever)  
2. Where they spawn.  
  
You can just do "Add Component" -> "Network Helper" and drag in your Player Controller prefab and spawn point (an Empty Game Object in your hierarchy).  
  
Read more about the Network Helper here: <https://sbox.game/dev/doc/networking/network-helper>  
  
This is **all you need** to get started.  Multiplayer in S&box is incredibly simple so long as you answer those first two questions correctly.  
   
  
To see these concepts in action, checkout my video tutorial here:
