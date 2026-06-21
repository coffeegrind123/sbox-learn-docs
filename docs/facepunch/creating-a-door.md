---
title: Creating a Door
slug: facepunch/creating-a-door
url: https://sbox.game/learn/facepunch/creating-a-door
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Mapping
content_type: Text
tags: [door, map, mapping]
rating: 4
views: 1458
upvotes: 20
downvotes: 1
updated: 'Updated

  31 Days Ago'
summary: How to make a basic door.
scraped_at: '2026-06-21T09:53:31Z'
---

# Creating a Door

> How to make a basic door.

# Setting up the door

Doors can basically be anything as long as it has a collider, for this tutorial we [will use a door model](https://sbox.game/facepunch/door_single_dev).

## Setup

Once you have your scene set up and the door in place, we can add the door component.  
[![](https://cdn.sbox.game/upload/b/1fe6bf8e/0603/4217/ad0d/0d66d4ee7574.png)](https://cdn.sbox.game/upload/b/1fe6bf8e/0603/4217/ad0d/0d66d4ee7574.png)Select the door and look at the inspector, you'll see a list of components these are what make up the door. Normally its a Model Renderer and Model Collider if you are using a prop.

If you have a Prop Component make sure you tick the **Is Static** option or if you have a rigid body to either disable it, remove it or turn off **Motion Enabled.**

[![](https://cdn.sbox.game/upload/b/1a55681f/1942/4697/94e6/1f9c63c41475.png)](https://cdn.sbox.game/upload/b/1a55681f/1942/4697/94e6/1f9c63c41475.png)Let's add the Door component, scroll down and press the **Add Component** button and search for "Door" select it to add it.  
[![](https://cdn.sbox.game/upload/b/1e31996e/ce2a/4910/8a2a/00670c9f9e66.png)](https://cdn.sbox.game/upload/b/1e31996e/ce2a/4910/8a2a/00670c9f9e66.png)You should now have the Door component now. As you can see there are a lot of options for now we don't really need to touch anything it's good to go out of the box.[![](https://cdn.sbox.game/upload/b/8c1f4130/11a6/4518/a855/54e4a12773fd.png)](https://cdn.sbox.game/upload/b/8c1f4130/11a6/4518/a855/54e4a12773fd.png)In the viewport you should see the gizmo of the door animating.  
[![](https://cdn.sbox.game/upload/b/d55940da/86ce/43a7/8d08/9daa15a0fb08.png)](https://cdn.sbox.game/upload/b/d55940da/86ce/43a7/8d08/9daa15a0fb08.png)Press play and open the door.

## Sliding Door

If you want a sliding door, at the top of the component you'll see 2 buttons one for rotating the other for sliding. Simply change it to sliding, The gizmo will now change to show its a sliding door.  
[![](https://cdn.sbox.game/upload/b/7e10263b/a89e/431a/9755/78d87c2398fb.png)](https://cdn.sbox.game/upload/b/7e10263b/a89e/431a/9755/78d87c2398fb.png)You can change how far it moves with the **Slide Offset,** Here I have changed it to move to the left.  
[![](https://cdn.sbox.game/upload/b/d69b8ab4/d47e/402f/b8f9/ad20f43ad873.png)](https://cdn.sbox.game/upload/b/d69b8ab4/d47e/402f/b8f9/ad20f43ad873.png)Press play and try it out.  
[](https://cdn.sbox.game/upload/b/46d91dfb/3817/4625/a82d/809634b1ff11.mp4)
