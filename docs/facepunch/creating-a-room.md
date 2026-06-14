---
title: Creating Your First Room
slug: facepunch/creating-a-room
url: https://sbox.game/learn/facepunch/creating-a-room
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Mapping
content_type: Text
tags: [map, mapping]
rating: 3
views: 938
upvotes: 4
downvotes: 0
updated: 'Updated

  24 Days Ago'
summary: Build your first playable room in s&box using the Mapping tools.
scraped_at: '2026-06-14T09:37:52Z'
---

# Creating Your First Room

> Build your first playable room in s&box using the Mapping tools.

# Your First Room in s&box Mapping Tools

In this tutorial we’ll build a simple playable room using the Mapping tools. We will be using the Sandbox Game as it contains everything to get us started you can read how to set up your project Here - <https://sbox.game/learn/facepunch/map-project>

# Opening the Mapping Tools

Open the Mapping tools by either pressing **M** or using the top dropdown menu

# Creating a Primitive

Press Shift + B or select the Primitive Tool icon on the toolbar.[![](https://cdn.sbox.game/upload/b/68f2e0b9/1398/4ab1/9bc0/d631794927e6.png)](https://cdn.sbox.game/upload/b/68f2e0b9/1398/4ab1/9bc0/d631794927e6.png)  
You’ll see several primitive shapes available:

- Block
- Cylinder
- Sphere
- Stairs
- More

For this tutorial we’ll use the **Block** option.  
[![](https://cdn.sbox.game/upload/b/5a568cf9/a594/40d2/a3b5/b3610299cc5a.png)](https://cdn.sbox.game/upload/b/5a568cf9/a594/40d2/a3b5/b3610299cc5a.png)

## Grid

Before building, increase the grid size. This can be done with **[** and **]** (For smaller and bigger), It'll snap to powers of 2, Let's make it 128 which is a good size to start with and make sure grid snapping is enabled.

If you have Grid Snap off, holding **Ctrl** will snap it - The same works the other way around, with it on holding **Ctrl** disables it while held.

[![](https://cdn.sbox.game/upload/b/d43f9b60/c4a7/4ba3/a3f5/be40bf9f6416.png)](https://cdn.sbox.game/upload/b/d43f9b60/c4a7/4ba3/a3f5/be40bf9f6416.png)  
Let's now draw our block out, Click and Drag in the viewport. You'll get a preview of the size and shown the dimensions. Release will show you the block in 3d.[![](https://cdn.sbox.game/upload/b/257f7d54/7ebd/41bd/82aa/eac4485c0a97.png)](https://cdn.sbox.game/upload/b/257f7d54/7ebd/41bd/82aa/eac4485c0a97.png)

Using the handles you can change the size of each side.

Pressing **Enter** will create it.

You have successfully created your first block.

# Turning it into a Room

After creating the block the editor will automatically switch to object mode, this will let's you move, rotate ect. [![](https://cdn.sbox.game/upload/b/7f4521bf/ba66/473f/bb29/f674ec14c234.png)](https://cdn.sbox.game/upload/b/7f4521bf/ba66/473f/bb29/f674ec14c234.png)Let's make sure our block is selected and press **F** or Flip Faces.[![](https://cdn.sbox.game/upload/b/4af21c30/5d0a/4a26/859f/4c6147ca41a4.png)](https://cdn.sbox.game/upload/b/4af21c30/5d0a/4a26/859f/4c6147ca41a4.png)This will flip the direction of all the faces inwards creating a empty room.

[![](https://cdn.sbox.game/upload/b/bbbf447a/8d2e/4121/b8c5/d79a4ad48706.png)](https://cdn.sbox.game/upload/b/bbbf447a/8d2e/4121/b8c5/d79a4ad48706.png)

In s&box lighting doesn't get block by back faces (Unless it is solid) meaning that light will pass through walls that aren't 2 sided. Basically if you can see through it so can lights.

## Creating a Spawn Point

In the Sandbox game, Players spawn from a spawn point. We need to add some to tell the game where we should spawning.  
  
Right click the viewport and go down to **Create Empty** this will create an empty GameObject. We need to give it a component.  
[![](https://cdn.sbox.game/upload/b/34f59d42/9d29/4921/80a3/2add22584755.png)](https://cdn.sbox.game/upload/b/34f59d42/9d29/4921/80a3/2add22584755.png)In the Inspector with the GameObject select, Select **Add Component** and search for **Spawn Point.**[![](https://cdn.sbox.game/upload/b/6aae29d6/2788/45f3/ac83/de87e2de62c4.png)](https://cdn.sbox.game/upload/b/6aae29d6/2788/45f3/ac83/de87e2de62c4.png)Pressing play will now put you in game and at the location of the spawn point.  
[![](https://cdn.sbox.game/upload/b/0cf95870/9f1f/430a/a965/647c667d1d44.jpg)](https://cdn.sbox.game/upload/b/0cf95870/9f1f/430a/a965/647c667d1d44.jpg)
