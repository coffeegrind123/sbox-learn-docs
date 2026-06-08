---
title: Making a First Person Game
slug: facepunch/making-a-first-person-game
url: https://sbox.game/learn/facepunch/making-a-first-person-game
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Editor
content_type: Text
tags: [beginner, editor, game, guide]
rating: 3
views: 443
upvotes: 5
downvotes: 0
updated: 'Updated

  10 Days Ago'
summary: How to create a First Person game
scraped_at: '2026-06-08T11:00:46Z'
---

# Making a First Person Game

> How to create a First Person game

# Creating the Player Controller

If you are starting from a new project, you can choose to start with the Player Controller template:[![](https://cdn.sbox.game/upload/b/31a93f33/c821/4ed2/a9c0/ec3f9efd90df.png)](https://cdn.sbox.game/upload/b/31a93f33/c821/4ed2/a9c0/ec3f9efd90df.png)Or if you're already working with an existing project, you can create a new Player Controller like so:[![](https://cdn.sbox.game/upload/b/01c5bd12/5ace/47b2/ba33/6c56bdba8170.png)](https://cdn.sbox.game/upload/b/01c5bd12/5ace/47b2/ba33/6c56bdba8170.png)

# How does the Player Controller work?

The created object has a PlayerController component on the root object, which is a first and third person controller that works out-of-the-box without any code required.

It's physics-based, so at its core it's a special RigidBody. It has all the same properties as a regular RigidBody (like velocity, mass, ect) except we do some extra stuff to make it more controllable.[](https://cdn.sbox.game/upload/b/702a9301/8a06/4912/ab81/8ca30244c288.mp4)

# Input

The owner of the GameObject can control the Player using their mouse/keyboard or controller. If the object has no network owner then it will take input from the local player as if it's a single player game.  
  
You can change all sorts of input-related variables in the Input tab, and can even disable Input altogether by right clicking the Input tab and pressing "Remove".[![](https://cdn.sbox.game/upload/b/935b7546/7143/4fe7/8295/ebfc47b87e4a.png)](https://cdn.sbox.game/upload/b/935b7546/7143/4fe7/8295/ebfc47b87e4a.png)

# Camera

The Player Controller has a built-in camera controller (which can be disabled just like the Input tab).  
  
Here you can specify whether or not the camera should use a Third Person view. There's also a "Toggle Camera Mode Button", which can be set to None if you don't want the user to be able to switch between first and third person in-game.[![](https://cdn.sbox.game/upload/b/6862ef46/2c32/4b3b/88bc/63064cb38a09.png)](https://cdn.sbox.game/upload/b/6862ef46/2c32/4b3b/88bc/63064cb38a09.png)

# MoveModes

When you first create a Player Controller, it will start out with a few MoveMode components.  
  
A MoveMode defines a mode of transportation for your Player. Defaults include Walk, Swim, and Ladder. These kick-in and override one-another if your Player is meeting certain conditions (like whether or not they are in a water volume or is pressing up against a ladder)  
  
They have their own properties which are set directly on their components rather than being part of the Player Controller:[![](https://cdn.sbox.game/upload/b/ad7d8981/d45c/4e85/b27c/2d7fdc489994.png)](https://cdn.sbox.game/upload/b/ad7d8981/d45c/4e85/b27c/2d7fdc489994.png)You can even create your own custom MoveMode components using C# to control the Player Controller in whatever ways you want!
