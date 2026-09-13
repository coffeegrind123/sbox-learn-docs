---
title: Making eyes look-at a target (Citizens)
slug: facepunch/citizen-look-at-targeting
url: https://sbox.game/learn/facepunch/citizen-look-at-targeting
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Gameplay
content_type: Text
tags: [at, citizen, eyes, look]
rating: 2
views: 60
upvotes: 1
downvotes: 0
updated: 'Updated

  3 days ago'
summary: get your player eyes and/or head to look at anything
scraped_at: '2026-09-13T11:16:42Z'
---

# Making eyes look-at a target (Citizens)

> get your player eyes and/or head to look at anything

So, your game or your movie has a citizen player character, and you'd like their eyes to look at something. Maybe another object, a player, a camera, static or in motion. Well, you can!

# Spawn a player

Right click in the hierarchy > create > Player Controller.[![](https://cdn.sbox.game/upload/b/aca7a89d/3940/412d/bb16/95bed9c9f2b7.png)](https://cdn.sbox.game/upload/b/aca7a89d/3940/412d/bb16/95bed9c9f2b7.png)

# Add a "Citizen Animation Helper" Component

After selecting your new player's "Body" in the hierarchy, add a new component to it, "Citizen Animation Helper" from the "Citizen" category.

[![](https://cdn.sbox.game/upload/b/b33f238c/727f/4d8b/a180/8226d09a0f96.png)](https://cdn.sbox.game/upload/b/b33f238c/727f/4d8b/a180/8226d09a0f96.png)

# Set up the component

In the general settings we need to point our 'target' to the player who's eyes we want to control.[![](https://cdn.sbox.game/upload/b/1fdfce2c/44d1/4f6f/b330/f77a8d193e62.png)](https://cdn.sbox.game/upload/b/1fdfce2c/44d1/4f6f/b330/f77a8d193e62.png)

Select the "Model Renderer (skinned)" that applies to your character:[![](https://cdn.sbox.game/upload/b/ebf1fba2/f3f1/419a/9feb/05619e459d53.png)](https://cdn.sbox.game/upload/b/ebf1fba2/f3f1/419a/9feb/05619e459d53.png)

# Create Bone Targets

To point to where the eyes are for the citizen, we need bone targets enabled. You can do this by ticking the box in the Model Renderer component above your Citizen Animation Helper Component.  
[![](https://cdn.sbox.game/upload/b/6ddda17c/0358/4fb9/a4ee/e12df56c5b1b.png)](https://cdn.sbox.game/upload/b/6ddda17c/0358/4fb9/a4ee/e12df56c5b1b.png)

# Set the Eye Source

Now we have the bones, it gives us all these joint names in the hierarchy. Drag the "head" into the "Eye Source" box in the Citizen Animation Helper Component.

[![](https://cdn.sbox.game/upload/b/0d568e50/8f65/41e1/8f75/0731c43da89e.png)](https://cdn.sbox.game/upload/b/0d568e50/8f65/41e1/8f75/0731c43da89e.png)

[![](https://cdn.sbox.game/upload/b/6d357b02/dbb0/47be/ae2c/d647df3974c6.png)](https://cdn.sbox.game/upload/b/6d357b02/dbb0/47be/ae2c/d647df3974c6.png)

# Add the look-at constraint

At the top of the component, click the "+" symbol and add "look at"

[![](https://cdn.sbox.game/upload/b/9c68b1b2/f14e/4c4d/923b/54107554f5db.png)](https://cdn.sbox.game/upload/b/9c68b1b2/f14e/4c4d/923b/54107554f5db.png)

# Choose the look-at target

Drag what your player should look at from the hierarchy to this box.

[![](https://cdn.sbox.game/upload/b/246b12d7/3feb/4de9/ba89/27141694c357.png)](https://cdn.sbox.game/upload/b/246b12d7/3feb/4de9/ba89/27141694c357.png)  
And boom, your players eyes should now look at the target (the camera, for example).  
  
[![](https://cdn.sbox.game/upload/b/44688a26/4783/4e4d/b0cf/39371a2ee739.gif)](https://cdn.sbox.game/upload/b/44688a26/4783/4e4d/b0cf/39371a2ee739.gif)

# Fine-tune the looking

You can control the weight of the eyes, head and body using the sliders, how much it should attempt to look at the target.   
  
For example, you may want the eyes to always be looking, but not the rest of the head. Or a mix, not breaking the players neck to look at the target, setting the head weight to 0.5.   
  
[![](https://cdn.sbox.game/upload/b/655ae0dd/2cde/4282/a6bf/997cf2fbab43.png)](https://cdn.sbox.game/upload/b/655ae0dd/2cde/4282/a6bf/997cf2fbab43.png)
