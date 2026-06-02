---
title: 'Starting From Zero: Creating Your First Map'
slug: subzerostudios/creating-your-first-map
url: https://sbox.game/learn/subzerostudios/creating-your-first-map
author: SubZero Studios
author_slug: subzerostudios
topic: Capable
content_type: Text
tags: [beginner, design, editor, game]
rating: 3
views: 74
upvotes: 5
downvotes: 0
updated: Updated 4 hours ago
summary: Everything you need to know creating your first map in S&box!
scraped_at: '2026-06-02T10:28:02Z'
---

# Starting From Zero: Creating Your First Map

> Everything you need to know creating your first map in S&box!

# **This Tutorial is 60% Done. We are getting feedback for the Current layout so excuse us while we have it public and unfinished :)** **We're dealing with Website issues regarding editing a Tutorial with over 100 Images as well (LOL) PLEASE FIX THIS FACEPUNCH.**

## Love, SubZero

# **This Tutorial is meant to cover the fundamentals of Level design for s&box. Please note that there are faster workflows / different ways for designing in the editor but I want to keep it simple for anyone who's new to this so they understand the basics. After this you should have a better idea on how to bring your own ideas to life inside the editor!**

## **We will be releasing more specific Tutorials on Workflow Techniques, Creating Certain Scenes and how to go about it, In depth Tutorials on certain Mapping Tools, etc along with Programming Tutorials. If you have** ANY **suggestions on educational content we should make please let us know :)**

# Need Support? Join our Discord!

## We don't just make Content for s&box, We also host a whole Community filled with many Talented Level Designers, Modelers, and Developers within the s&box ecosystem that Help each other Learn, Provide Feedback to, and Hangout with!

[**SubZero Studios Discord**](https://subzerostudios.dev/discord/join/85C5iG5w) ***(<- Join here)***

**Now Lets build a House which covers alot of fundamentals and gets you used to Key binds and where things are.**

# Section 1: Creating Your Map Project

Open up the s&box Dev Editor. In the top right you'll see a **New Project** button — click that. A template picker will pop up. Select **Map**, give your project a title, and hit **Create**.

[![](https://cdn.sbox.game/upload/b/60e66ba2/75a0/43c5/8791/52b61bfd3f83.png "Create a New Project")](https://cdn.sbox.game/upload/b/60e66ba2/75a0/43c5/8791/52b61bfd3f83.png)[![](https://cdn.sbox.game/upload/b/fc30fc0a/e31a/4f2b/b2c0/df014792a2e3.png "Select Map and Name your Map")](https://cdn.sbox.game/upload/b/fc30fc0a/e31a/4f2b/b2c0/df014792a2e3.png)

The ident field fills in automatically based on your title. You can leave it as is. Don't worry about the other settings — everything is already configured correctly for a map project. 

# Section 2: Getting to Know the Editor

When you first open your map you'll see several panels arranged around the main viewport. Here's a quick breakdown of what each one does. [![](https://cdn.sbox.game/upload/b/5ea4cdb1/dfa0/47ed/a33d/6a547481d832.png)](https://cdn.sbox.game/upload/b/5ea4cdb1/dfa0/47ed/a33d/6a547481d832.png)

## **Hierarchy**

**The Hierarchy lives in the top left. It lists every GameObject in your scene — think of it as your scene's table of contents. Right now it just shows the default Main Camera and Directional Light that every new Scene starts with.** [![](https://cdn.sbox.game/upload/b/105d150c/8ae7/4520/ad29/d63d6b2b6c38.png)](https://cdn.sbox.game/upload/b/105d150c/8ae7/4520/ad29/d63d6b2b6c38.png)

*Don't skip naming your objects. A Hierarchy full of objects called "GameObject", "GameObject (2)", "GameObject (3)" is a nightmare to work with once your map gets bigger. Name as you go, not at the end.*

## Scene Viewport

**This is where you build and navigate your map. The grid you see is your world floor. You can navigate by holding right click and using WASD to fly around. Go ahead and get a good Feeling of movements before we move on.**

[![](https://cdn.sbox.game/upload/b/54eec521/9616/4321/9cd1/b6e18dccf327.png)](https://cdn.sbox.game/upload/b/54eec521/9616/4321/9cd1/b6e18dccf327.png)

## Inspector

**The Inspector lives on the right side. When you select a GameObject it shows you all of its properties and components — position, rotation, scale, and anything else attached to it.** [![](https://cdn.sbox.game/upload/b/e92e03a0/5b68/4f7b/8be3/a2524bac55b6.png)](https://cdn.sbox.game/upload/b/e92e03a0/5b68/4f7b/8be3/a2524bac55b6.png)

## Asset Browser

**The Asset Browser sits at the bottom. This is where you find materials, models, and other assets to use in your map.** [![](https://cdn.sbox.game/upload/b/ca0dbcb5/7800/4643/be9b/79e5b442b891.png)](https://cdn.sbox.game/upload/b/ca0dbcb5/7800/4643/be9b/79e5b442b891.png)

Don't worry about memorizing all of this right now. You'll get comfortable with each panel naturally as we start building. 

# Section 3: Editor Settings

Before we start building it's worth taking a minute to set the editor up the way you want it. Go to **Edit → Preferences** to open Editor Settings.

[![](https://cdn.sbox.game/upload/b/a5b3d96f/a356/4fbc/a6a4/6a9330d379aa.png)](https://cdn.sbox.game/upload/b/a5b3d96f/a356/4fbc/a6a4/6a9330d379aa.png)

## Scene View

[![](https://cdn.sbox.game/upload/b/acfec5c9/5bc3/4474/85bd/2637805ee24e.png "Scene View ")](https://cdn.sbox.game/upload/b/acfec5c9/5bc3/4474/85bd/2637805ee24e.png)

Scene View controls how the viewport camera behaves. There are a lot of options in here, but only two actually matter while you're getting started:

- **Movement Speed** — How fast you fly around the viewport with WASD. This is the first thing to adjust if navigation felt too slow or too fast from earlier.
- **Sensitivity** — Your mouse look sensitivity inside the viewport. Adjust this if rotating the view feels off.

> **Info —** Everything else in here can stay at default for now. Set **Movement Speed** and **Sensitivity** to whatever feels comfortable and move on — we'll break down the rest of these settings in a dedicated tutorial if you ever need them.

## Editor Keybinds

[![](https://cdn.sbox.game/upload/b/32f55fe0/835f/4118/8179/b3d3f137ba13.png)](https://cdn.sbox.game/upload/b/32f55fe0/835f/4118/8179/b3d3f137ba13.png)

## **Here are the keybinds you'll use the most while building maps. We'll cover the full keybind reference in a separate tutorial.**

Please take the time to study this. It makes you work 10x faster and makes it a much more enjoyable process TRUST ME.

**General**

- Undo `Ctrl+Z` — Undoes the Action you did.
- Redo `Ctrl+Y` — When you spammed `Ctrl+Z` too many times.
- Save `Ctrl+S` — Make this one a Habit! s&box is prone to crash.
- Duplicate `Ctrl+D` — Awesome for making multiple objects that are the same
- Toggle Play `F5` — How to quickly Test your map (Needs a Spawn Point Component)
- Hide Selected `H` — VERY useful! Hides things so you can get to something.
- Hide/Show `Alt+H` — Toggles your hidden stuff back into view.
- Isolate Selection `Ctrl+H` — Hides EVERYTHING but what you picked. Perfect for focusing on one room.
- Unhide All `U` — Don't forget to do this one..

**Grid**

- Decrease Grid Size `[` — Shrinks the grid for fine, precise detail work.
- Increase Grid Size `]` — Grows the grid for blocking out big stuff fast.
- Toggle Grid Snap `G` — Keep this ON! Off-grid geometry will cause you more problems than anything.

**Mapping**

- Enter Mapping Mode `M` — Step one, every time.
- Primitive Tool `Shift+B` — Where you create your Geometry
- Object Selection `4` — Grab whole meshes to move them around.
- Face Tool `3` — Gives you the ability to select individual Faces on a mesh.
- Edge Tool `2` — Gives you the ability to select individual Edges on a mesh.
- Vertex Tool `1` — Gives you the ability to select individual Vertices/Corners on a mesh.
- Position `W` — Move your selection around.
- Rotate `E` — Spin it.
- Scale `R` — Make it bigger or smaller.
- Resize `Y` — Drag the bounding-box handles — perfect for blocks.
- Apply Material `Shift+T` — Places your active material onto the selected faces.
- Apply Hotspot `Alt+H` — Auto-fits the texture cleanly to each face for you.
- Select Loop `L` — Grabs a whole edge loop in one click. Huge time saver.
- Combine Faces `Backspace` — Merges flat neighboring faces into one.
- Thicken Faces `G` — turns a plane into a slab.
- Flip All Faces `F` — Flips stuff inside out.
- Frame Selection `Shift+A` — Snaps the camera right to your selection.

For the full keybind reference check out our Editor Keybinds tutorial. *[link here before publish]*

# Section 4:  Entering Mapping Mode

To start building you need to switch into Mapping mode. Click the mode dropdown in the top left of the viewport — it shows **Object Select** by default. Under **Tools** select **Mapping**, or just press **M** while clicked into the viewport.

[![](https://cdn.sbox.game/upload/b/d65b1f5a/82c8/4e27/8b9d/b4d4eaef767c.png)](https://cdn.sbox.game/upload/b/d65b1f5a/82c8/4e27/8b9d/b4d4eaef767c.png)  
Once you're in Mapping mode the toolbar appears on the left side of your viewport. Here's what each tool does and how to get to it fast.

[![](https://cdn.sbox.game/upload/b/71d3c544/1846/4979/8028/1f652c87352c.png)](https://cdn.sbox.game/upload/b/71d3c544/1846/4979/8028/1f652c87352c.png)

[![](https://cdn.sbox.game/upload/b/ce93ce3f/8b26/4e09/931f/464c504aff9c.png " Primitive Shift+B ﻿")](https://cdn.sbox.game/upload/b/ce93ce3f/8b26/4e09/931f/464c504aff9c.png)[![](https://cdn.sbox.game/upload/b/361e267e/4419/45e2/b68a/3a14b95e97f2.png "Object Select 4")](https://cdn.sbox.game/upload/b/361e267e/4419/45e2/b68a/3a14b95e97f2.png)[![](https://cdn.sbox.game/upload/b/c710487a/9d13/4b57/9b06/01f06ec191fe.png "Vertex 1")](https://cdn.sbox.game/upload/b/c710487a/9d13/4b57/9b06/01f06ec191fe.png)[![](https://cdn.sbox.game/upload/b/e21e95b5/2c1e/4bb6/88d6/086474470c4c.png "Edge 2")](https://cdn.sbox.game/upload/b/e21e95b5/2c1e/4bb6/88d6/086474470c4c.png)[![](https://cdn.sbox.game/upload/b/e1e09831/178d/45da/8dcb/1dc3f9d12003.png "Face 3")](https://cdn.sbox.game/upload/b/e1e09831/178d/45da/8dcb/1dc3f9d12003.png)[![](https://cdn.sbox.game/upload/b/78ad3564/1a02/4b81/9fac/c1bbff03e185.png "Vertex Paint 5")](https://cdn.sbox.game/upload/b/78ad3564/1a02/4b81/9fac/c1bbff03e185.png)[![](https://cdn.sbox.game/upload/b/276e3930/4d69/4ab5/94c1/3fe4ef3ed5e8.png "Displacement")](https://cdn.sbox.game/upload/b/276e3930/4d69/4ab5/94c1/3fe4ef3ed5e8.png)

- **Primitive** `Shift+B` — Where you create geometry. Every surface in your map starts here.
- **Object Select** `4` — Select and move whole meshes.
- **Vertex** `1` — Edit individual points on a mesh.
- **Edge** `2` — Edit the lines between vertices.
- **Face** `3` — Edit individual surfaces and apply materials.
- **Vertex Paint** `5` — Paint colors and blend masks onto surfaces.
- **Displacement** — Sculpt and push vertices like terrain.

Get used to hitting `Shift+B`, `4`, `3`, and `2` to switch tools, plus `W`, `E`, and `R` to Move, Rotate, and Scale — these cover most of what you do in this tutorial and every map after it. 

# Section 5: Building the Floor

**Before we place anything — a quick note on workflow. Geometry first, textures second, lighting third. Don't worry about how anything looks until the space feels right to walk through. Everything starts on dev textures and we clean it up later.**

*Always build on the grid. Use* `[` *to make it smaller for precision work and* `]` *to make it larger for laying out big surfaces. Geometry that's off grid causes seams, lighting issues and z-fighting. Build on the grid every time.*

Before you place anything make sure **Grid Snap** is turned on. You can see the grid size indicator in the top bar of the viewport — it shows **32** by default. Click the grid icon next to it to enable snapping, or press `G` to toggle it on.

*Grid snap is not on by default. If you place geometry without it your surfaces will be off grid and won't line up cleanly when you try to connect walls, floors and ceilings later. Turn it on before you place your first Quad and leave it on.*

## Placing the Floor Quad

Press `Shift+B` to open the Primitive Tool. It opens on Block by default — click the **Quad** icon in the Primitive Type selector to switch to it. [![](https://cdn.sbox.game/upload/b/f143a092/5a77/47fb/9af3/8c80db6ffe62.png)](https://cdn.sbox.game/upload/b/f143a092/5a77/47fb/9af3/8c80db6ffe62.png)

[![](https://cdn.sbox.game/upload/b/6bcd2997/110c/4ea7/872d/ef1264cfb294.png)](https://cdn.sbox.game/upload/b/6bcd2997/110c/4ea7/872d/ef1264cfb294.png)

***Quad vs Block — What's the difference?*** *A* ***Block*** *is a 3D box primitive — it creates six faces all at once, one for every side. Great for quick solid objects but gives you geometry you didn't ask for. A* ***Quad*** *is a flat 2D plane — a single face with zero thickness. When you build with Quads you place every surface on purpose, which means cleaner geometry, less waste, and more control over your map from the start.*

**Leave HasBackface off. The floor only needs to be visible from above — the player never sees the underside of it.**

***When should you use HasBackface?*** *Only turn it on for surfaces the player can see from both sides — a floating platform, a thin fence, a hanging sign. For any surface inside a closed room leave it off. Rendering faces the player can never see is wasted performance.*

Click and drag on the grid to draw out your floor. You'll see the dimensions update live as you drag — aim for **W:512 L:512**. Once you're happy with the size either click **Create** in the sidebar or hit **Enter** to commit it.   
  
[![](https://cdn.sbox.game/upload/b/9b3bbdf9/6b57/452d/a6ce/70862aecc715.png)](https://cdn.sbox.game/upload/b/9b3bbdf9/6b57/452d/a6ce/70862aecc715.png)

*If your Quad is standing up vertically instead of lying flat you dragged in the wrong direction. Hit* `Ctrl+Z` *and try again — drag horizontally across the grid floor.*

## Name Your Objects

Right click your object in the Hierarchy and select **Rename**, or press `F2`. Type your new name and hit **Enter** to confirm it.   
  
[![](https://cdn.sbox.game/upload/b/99d19636/a740/4ab4/984f/7f10de6e1b4a.png)](https://cdn.sbox.game/upload/b/99d19636/a740/4ab4/984f/7f10de6e1b4a.png)

*You must hit* ***Enter*** *to save the rename. Clicking away without pressing Enter will revert the name back to what it was.*

## 

# Organize Your Scene

# 

# **Save Your Map**

# Before we start adding walls, save your work. Press `Ctrl+S`. The first time you save, s&box will ask where to put the scene — drop it in your project's `assets/scenes` folder and give it a clear name like `My First Map`. After that, `Ctrl+S` saves instantly.

Get in the habit of saving constantly. Hit `Ctrl+S` after finishing each section. The editor is still in active development and can crash — don't lose an hour of work because you forgot to save.

# Section 6: Building the Walls

## Select the Floor Edges

***Edge Tool (*****`2`*****), select all four floor edges (double-click /*** **`L`** ***for the loop).***

[![](https://cdn.sbox.game/upload/b/34671814/800e/42b7/83ba/d995b46935d8.png)](https://cdn.sbox.game/upload/b/34671814/800e/42b7/83ba/d995b46935d8.png)[![](https://cdn.sbox.game/upload/b/0b109312/08da/4879/87d5/ca1d00cc15fb.png)](https://cdn.sbox.game/upload/b/0b109312/08da/4879/87d5/ca1d00cc15fb.png)

## Extrude the Walls Up

## 

***Extrude the selected edges upward to 144.. Note grid snap keeps it clean****.*[![](https://cdn.sbox.game/upload/b/7e03f41a/802a/4bc5/b898/e06019583b92.png)](https://cdn.sbox.game/upload/b/7e03f41a/802a/4bc5/b898/e06019583b92.png)

## Save Your Scene

***Quick reminder:*** **`Ctrl+S`** ***again — save often.***

# Section 7: Building the Ceiling & Doorway

## Closing the Ceiling

***Fill the top opening (Fill Hole*** **`P`** ***on the top edge loop, or a ceiling Quad). Now you have a ceiling!*** [![](https://cdn.sbox.game/upload/b/e10d7d3c/7ab4/466a/8357/8fbe96e62714.png)](https://cdn.sbox.game/upload/b/e10d7d3c/7ab4/466a/8357/8fbe96e62714.png)

# Now before we continues lets make it easier to see things. There's a few ways to do this.

## **Turn on Full bright mode.**

[![](https://cdn.sbox.game/upload/b/c7004ad9/93cb/4372/85c8/69607815abda.png "Click View Settings")](https://cdn.sbox.game/upload/b/c7004ad9/93cb/4372/85c8/69607815abda.png)[![](https://cdn.sbox.game/upload/b/613842f7/a2b9/44fc/82d7/5b84fb738733.png "Lit Mode is Default")](https://cdn.sbox.game/upload/b/613842f7/a2b9/44fc/82d7/5b84fb738733.png)

## Visualize Scene Object Debugger (My Favorite)

[![](https://cdn.sbox.game/upload/b/78d35519/82d8/45bf/ad76/094ef85c7ddd.png)](https://cdn.sbox.game/upload/b/78d35519/82d8/45bf/ad76/094ef85c7ddd.png)

## Cutting the Doorway

## Cut the doorway opening into an interior wall — pick a side, any side! 1. In the Face Tool (`3`), select the wall face. 2. Press `Ctrl+D` to duplicate the face — this keeps the doorway centered on the wall. 3. Switch to the Edge Tool (`2`) and select the doorway edge — press `L` or double-click to grab the whole edge. 4. Press `F` to bevel the edge. 5. Switch to the **Scale** move mode, drop the grid down to `4`, and drag it out until the door is **56 units wide**. 6. Switch to the **Scale** move mode, drop the grid down to `4`, and drag it out until the door is **56 units wide**. 7. Switch back to the Face Tool (`3`), select the doorway face, and press `Del` to open it up.

[![](https://cdn.sbox.game/upload/b/1c5e6236/45f3/4820/8c06/f6e5221e6d35.png)](https://cdn.sbox.game/upload/b/1c5e6236/45f3/4820/8c06/f6e5221e6d35.png)

[![](https://cdn.sbox.game/upload/b/efde3db5/ae35/450f/8dae/bb90cca0d545.png)](https://cdn.sbox.game/upload/b/efde3db5/ae35/450f/8dae/bb90cca0d545.png)[![](https://cdn.sbox.game/upload/b/e98c91b9/11d8/4619/9986/6e118ae9461a.png)](https://cdn.sbox.game/upload/b/e98c91b9/11d8/4619/9986/6e118ae9461a.png)

[![](https://cdn.sbox.game/upload/b/9412d062/6c9d/4f3e/8151/61abe49cd5d7.png)](https://cdn.sbox.game/upload/b/9412d062/6c9d/4f3e/8151/61abe49cd5d7.png)

[![](https://cdn.sbox.game/upload/b/5b0eaea9/3e06/437f/bfaa/2ef84b765253.png)](https://cdn.sbox.game/upload/b/5b0eaea9/3e06/437f/bfaa/2ef84b765253.png)

[![](https://cdn.sbox.game/upload/b/191c5fd7/a3ed/4ff2/a09a/271b36dd733b.png)](https://cdn.sbox.game/upload/b/191c5fd7/a3ed/4ff2/a09a/271b36dd733b.png)[![](https://cdn.sbox.game/upload/b/7a99b822/2fc6/43d9/98b6/96c2e851e3a6.png)](https://cdn.sbox.game/upload/b/7a99b822/2fc6/43d9/98b6/96c2e851e3a6.png)

# Section 8: Building the Exterior & Roof

## The house is solid on the inside — now we wrap it in an outer shell. The gap between the inside walls and the outer shell becomes your **wall thickness** (usually 8 units on residential buildings, 16 units on commercial).

## Wrap the House in an Exterior Shell

1. Set the grid size to **8**.
2. Press `Shift+B` and place a **Block** that's **8 units bigger** than the outside of your walls on every side, wrapping the whole house.
3. Line it up so there's a consistent **8-unit gap** between the interior walls and the outer shell all the way around — that gap is your wall thickness.
4. Switch to the Face Tool (`3`), select the **bottom face** of the shell and press `Del` — it sits on the ground and the player never sees it.

[![](https://cdn.sbox.game/upload/b/a7e38d83/ee49/4c7a/8af8/8653fbd47d5f.png)](https://cdn.sbox.game/upload/b/a7e38d83/ee49/4c7a/8af8/8653fbd47d5f.png)  
  
[![](https://cdn.sbox.game/upload/b/34a5b69d/f05a/435a/b776/980d9fbfc242.png)](https://cdn.sbox.game/upload/b/34a5b69d/f05a/435a/b776/980d9fbfc242.png)

## Cut the Exterior Doorway

**Now punch the doorway through the outer shell so it lines up with the interior opening you already cut.**

1. In the Face Tool (`3`), select the exterior front face. (Go inside the house in the editor to figure out which wall is which.)
2. Set the grid size to **4**.
3. Press `Shift+X` to open the Clip Tool and clip the doorway to match the interior frame cuts. Press `Space` after each cut to keep clipping without reopening the tool. You don't have to drag it all the way. Just match the edges up. Don't over think it.
4. Select the exterior doorway face and press `Del`. (If you haven't already removed the interior doorway face, do that now too.)
5. Switch to the Edge Tool (`2`), double-click the open edge loop on the **interior** opening and the **exterior** opening to select both, then press `B` to **bridge** them. That stitches the two walls together into a solid doorway jamb through the 8-unit thickness.
6. Bridging merges the two walls into a single mesh, so it shows back up in the Hierarchy as a generic `Block`. Rename it (`F2`) back to something clear like `House`.

[![](https://cdn.sbox.game/upload/b/c46a6158/2429/4cce/8015/a89274e7901f.png)](https://cdn.sbox.game/upload/b/c46a6158/2429/4cce/8015/a89274e7901f.png)  
[![](https://cdn.sbox.game/upload/b/bbd7e42a/7afd/47c8/b96d/4790f15991e3.png)](https://cdn.sbox.game/upload/b/bbd7e42a/7afd/47c8/b96d/4790f15991e3.png)  
[![](https://cdn.sbox.game/upload/b/66232ada/53cd/4a82/9b79/c4b59f65ecf5.png)](https://cdn.sbox.game/upload/b/66232ada/53cd/4a82/9b79/c4b59f65ecf5.png)  
[![](https://cdn.sbox.game/upload/b/7b6b3510/c0eb/4b75/987f/bfb386660ade.png)](https://cdn.sbox.game/upload/b/7b6b3510/c0eb/4b75/987f/bfb386660ade.png)  
[![](https://cdn.sbox.game/upload/b/e67f6fcf/fcdc/4860/9afd/33a764baf2eb.png)](https://cdn.sbox.game/upload/b/e67f6fcf/fcdc/4860/9afd/33a764baf2eb.png)

[![](https://cdn.sbox.game/upload/b/062dbc5b/eb07/48ab/b659/c8c94e283895.png)](https://cdn.sbox.game/upload/b/062dbc5b/eb07/48ab/b659/c8c94e283895.png)[![](https://cdn.sbox.game/upload/b/c17a4fb2/8952/4f08/8a2a/21091503279e.png)](https://cdn.sbox.game/upload/b/c17a4fb2/8952/4f08/8a2a/21091503279e.png)

[![](https://cdn.sbox.game/upload/b/fe18cd15/fc96/46dc/9ba7/154b81504259.png)](https://cdn.sbox.game/upload/b/fe18cd15/fc96/46dc/9ba7/154b81504259.png)

[![](https://cdn.sbox.game/upload/b/717d72e4/18ee/4809/ab89/278060ed8b9a.png)](https://cdn.sbox.game/upload/b/717d72e4/18ee/4809/ab89/278060ed8b9a.png)[![](https://cdn.sbox.game/upload/b/5ae10336/14d5/4022/91de/a4d458581362.png)](https://cdn.sbox.game/upload/b/5ae10336/14d5/4022/91de/a4d458581362.png)

[![](https://cdn.sbox.game/upload/b/ae707544/2678/4972/a149/2f06093abafb.png)](https://cdn.sbox.game/upload/b/ae707544/2678/4972/a149/2f06093abafb.png)

## Add Windows

**Windows work a lot like the doorway — just clipped instead of beveled. We'll cut both windows, open them up, bridge the reveals through the wall, then size them to a clean 64 × 8 × 72 (64 wide, 8 deep through the wall, 72 tall).**

**Cut the first window**

1. **In the Face Tool (****`3`****), select the wall faces where the window goes — both the inside and outside face. Hold** **`Shift`** **to grab both faces at once.**
2. **Set the grid size to 8.**
3. **Press** **`Shift+X`** **to open the Clip Tool, then cut the top of the window 8 units down from the top of the door height line. (Press** **`Space`** **between cuts to keep the tool open, same as the doorway.)**
4. **Cut the bottom of the window. Just eyeball it for now — you can adjust it later.**
5. **Cut the two sides. Honestly, make them however you want.**
6. **Press** **`Enter`** **to commit once the right-side window is cut out.**

[![](https://cdn.sbox.game/upload/b/2761b6d6/7fdc/43ed/8bd7/44d6d7ec99dc.png)](https://cdn.sbox.game/upload/b/2761b6d6/7fdc/43ed/8bd7/44d6d7ec99dc.png)  
[![](https://cdn.sbox.game/upload/b/4e205ce1/143a/4849/a8d5/ba159e29ddfb.png)](https://cdn.sbox.game/upload/b/4e205ce1/143a/4849/a8d5/ba159e29ddfb.png)

[![](https://cdn.sbox.game/upload/b/54a6da8f/1da0/498e/9147/c4530910ea8a.png)](https://cdn.sbox.game/upload/b/54a6da8f/1da0/498e/9147/c4530910ea8a.png)  
[![](https://cdn.sbox.game/upload/b/94db3387/a273/4448/bfd4/c6f8e79af614.png)](https://cdn.sbox.game/upload/b/94db3387/a273/4448/bfd4/c6f8e79af614.png)

[![](https://cdn.sbox.game/upload/b/57594c88/c9f0/43bf/9df0/ea3be8b4ee64.png)](https://cdn.sbox.game/upload/b/57594c88/c9f0/43bf/9df0/ea3be8b4ee64.png)  
  
  
[![](https://cdn.sbox.game/upload/b/2a0194fb/72c5/4c12/94a3/0906c9d84198.png)](https://cdn.sbox.game/upload/b/2a0194fb/72c5/4c12/94a3/0906c9d84198.png)

## **Cut the second window**

**Move to the left window and do the exact same thing.**

**Tip —** Quick trick on the left side:  `Alt+Shift+Double Left Click` on one Face selects **all faces** on that plane. Do it on the inside and outside, then clip them just like you did the right side. 

[![](https://cdn.sbox.game/upload/b/6db19b0f/1003/4d12/84ac/4a735dff4fe0.png)](https://cdn.sbox.game/upload/b/6db19b0f/1003/4d12/84ac/4a735dff4fe0.png)

[![](https://cdn.sbox.game/upload/b/0358e07f/3071/4f7f/a4fa/af045972985e.png)](https://cdn.sbox.game/upload/b/0358e07f/3071/4f7f/a4fa/af045972985e.png)

[![](https://cdn.sbox.game/upload/b/00640de9/c227/4115/b073/7fa79a10924a.png)](https://cdn.sbox.game/upload/b/00640de9/c227/4115/b073/7fa79a10924a.png)[![](https://cdn.sbox.game/upload/b/9733fcd4/72fd/47c3/aea8/7b9b66131eca.png)](https://cdn.sbox.game/upload/b/9733fcd4/72fd/47c3/aea8/7b9b66131eca.png)

## **Open and bridge the reveals**

1. **Select all 4 window faces (inside and outside, both windows) and press** **`Del`** **to open them up.**
2. **Switch to the Edge Tool (****`2`****), double-click the window edges inside and out, and press** **`B`** **to bridge them on both sides connecting both faces together to form the windows.**

[![](https://cdn.sbox.game/upload/b/e9357602/ace0/4b6d/a906/3ca4c2d85b1e.png)](https://cdn.sbox.game/upload/b/e9357602/ace0/4b6d/a906/3ca4c2d85b1e.png)[![](https://cdn.sbox.game/upload/b/ee809055/206e/4707/979b/4cb84f2eaa8d.png)](https://cdn.sbox.game/upload/b/ee809055/206e/4707/979b/4cb84f2eaa8d.png)

[![](https://cdn.sbox.game/upload/b/5ce03edf/beee/40c0/95b0/7d32461c32b1.png)](https://cdn.sbox.game/upload/b/5ce03edf/beee/40c0/95b0/7d32461c32b1.png)

## **Size the windows to 64 × 8 × 72**

1. **Still in the Edge Tool, select the edges shown and press** **`Backspace`** **to Dissolve them — do this on the inside and outside. This cleans up the mesh and makes the window easier to manipulate.**
2. **On the exterior right window, select the 4 edges and switch to the Scale move mode. Set the grid to 4 and scale until the window reads 64 wide.**

**Tip —** Hold `Shift` and drag with left-click held down to quickly multi-select a run of edges at once.

[![](https://cdn.sbox.game/upload/b/924f0491/54a3/461d/ac23/0fc6b9fc0f4e.png)](https://cdn.sbox.game/upload/b/924f0491/54a3/461d/ac23/0fc6b9fc0f4e.png)  
[![](https://cdn.sbox.game/upload/b/d4bff9d3/ade8/444b/b82f/56264a382fe3.png "The Right Side Exterior is missing the edges because how we cut it.")](https://cdn.sbox.game/upload/b/d4bff9d3/ade8/444b/b82f/56264a382fe3.png)  
**The Right Side Exterior is missing the 4 edges because how we cut it earlier. Oops.**

[![](https://cdn.sbox.game/upload/b/b7ff5fc7/96f7/4e07/b8a0/401d6524ae51.png)](https://cdn.sbox.game/upload/b/b7ff5fc7/96f7/4e07/b8a0/401d6524ae51.png)

# 

## Build the Roof

**A simple pitched roof, built straight off the top of the exterior shell.**

## **Cap and split the top**

# 1. **In the Face Tool (****`3`****), select the top face of the exterior shell.** 2. **Set the grid to 8, then hold** **`Shift`** **and move the face up 8 units to extrude a base slab for the roof.** 3. **Switch to the Edge Tool (****`2`****), select the front roof edge and the rear roof edge, then press** **`V`** **(Connect) to cut a ridge line straight down the middle of the roof.**

**Tip —** You can nudge a selection with the **arrow keys** instead of dragging the gizmo — handy for clean, grid-sized moves.

[![](https://cdn.sbox.game/upload/b/d5d2e212/0050/4c20/854a/008c568c6dcd.png)](https://cdn.sbox.game/upload/b/d5d2e212/0050/4c20/854a/008c568c6dcd.png)

[![](https://cdn.sbox.game/upload/b/cdcd9df8/1d8b/46fd/b22d/dd66130e604f.png)](https://cdn.sbox.game/upload/b/cdcd9df8/1d8b/46fd/b22d/dd66130e604f.png)[![](https://cdn.sbox.game/upload/b/b63bede4/7951/469f/a274/66b80bd363ee.png)](https://cdn.sbox.game/upload/b/b63bede4/7951/469f/a274/66b80bd363ee.png)

[![](https://cdn.sbox.game/upload/b/99296e1b/6aaa/4855/a378/89660e30892d.png)](https://cdn.sbox.game/upload/b/99296e1b/6aaa/4855/a378/89660e30892d.png)  
[![](https://cdn.sbox.game/upload/b/cf6416f5/cc9f/4a74/bbf9/ab1b6f79da6b.png)](https://cdn.sbox.game/upload/b/cf6416f5/cc9f/4a74/bbf9/ab1b6f79da6b.png)

## **Raise the ridge into a pitch**

1. ## **Switch to the Face Tool (****`3`****), select the two roof faces, then hold** **`Shift`** **and extrude them up 8 units.**
2. ## **Switch back to the Edge Tool (****`2`****), grab the front center edge and the rear center edge, and raise them up about 76 units. That gives you the pitch.**

[![](https://cdn.sbox.game/upload/b/943327d1/b1c8/43d0/ba8a/c82219fad4bf.png)](https://cdn.sbox.game/upload/b/943327d1/b1c8/43d0/ba8a/c82219fad4bf.png)  
[![](https://cdn.sbox.game/upload/b/9031be52/c278/42f2/b7ad/7f51e74c5c94.png)](https://cdn.sbox.game/upload/b/9031be52/c278/42f2/b7ad/7f51e74c5c94.png)

[![](https://cdn.sbox.game/upload/b/acfe325d/86c3/41f3/b080/f92a5dde06b1.png)](https://cdn.sbox.game/upload/b/acfe325d/86c3/41f3/b080/f92a5dde06b1.png)

## **Front and back overhangs**

1. ## **Switch to the Face Tool (****`3`****), select the two front slope faces, then hold** **`Shift`** **and extrude them out 16 units to create the overhang.**
2. ## **Repeat for the rear of the house.**

[![](https://cdn.sbox.game/upload/b/189346f2/5c88/4a43/ac65/e869f5e91853.png)](https://cdn.sbox.game/upload/b/189346f2/5c88/4a43/ac65/e869f5e91853.png)  
[![](https://cdn.sbox.game/upload/b/5bde6c79/e1b3/4c28/95df/73aa5a61b43d.png)](https://cdn.sbox.game/upload/b/5bde6c79/e1b3/4c28/95df/73aa5a61b43d.png)  
[![](https://cdn.sbox.game/upload/b/3d81e709/fdb5/45f4/8909/5da55cb7aab9.png)](https://cdn.sbox.game/upload/b/3d81e709/fdb5/45f4/8909/5da55cb7aab9.png)

## **Side overhangs**

**Info — In Hammer you'd rotate the work-plane axis to extrude the side overhangs. The Scene mapping tools don't have that yet, so here's a crap workaround for now.**

1. ## **In the Face Tool (****`3`****), select the roof's side faces — all 6 of them, as shown.**
2. ## **Switch to the Scale move mode and scale both sides out 24 units (3 grid snaps at grid 8).**
3. ## **Switch to the Move / Position move mode and move those faces down 8 units — drag the transform gizmo, or use the Down arrow key.**

[![](https://cdn.sbox.game/upload/b/7b0be20f/889b/4449/8330/b06d64eccb88.png)](https://cdn.sbox.game/upload/b/7b0be20f/889b/4449/8330/b06d64eccb88.png)[![](https://cdn.sbox.game/upload/b/7c48b6d8/6861/4667/b76a/537684f616c6.png)](https://cdn.sbox.game/upload/b/7c48b6d8/6861/4667/b76a/537684f616c6.png)

[![](https://cdn.sbox.game/upload/b/f02b1ffc/36e4/42ba/81f7/9e9454dbdbb0.png)](https://cdn.sbox.game/upload/b/f02b1ffc/36e4/42ba/81f7/9e9454dbdbb0.png)  
[![](https://cdn.sbox.game/upload/b/7aad86dc/6e14/4c47/8aec/391544463435.png)](https://cdn.sbox.game/upload/b/7aad86dc/6e14/4c47/8aec/391544463435.png)  
  
  
[![](https://cdn.sbox.game/upload/b/73817ef2/c4d2/4725/a880/7dc09f5a11ea.png)](https://cdn.sbox.game/upload/b/73817ef2/c4d2/4725/a880/7dc09f5a11ea.png)

Look at your Beautiful house you've built! 

[![](https://cdn.sbox.game/upload/b/d82dfb5b/4127/43e8/b474/278b9d624541.png)](https://cdn.sbox.game/upload/b/d82dfb5b/4127/43e8/b474/278b9d624541.png)

# Section 9: Building the Ground

# Now we give the house something to sit on. We start with a Quad and stretch it out around the house with the edge tools — same building blocks you already know. 1. Press `Shift+B`, select the **Quad** primitive, and draw out the ground. Size it to about the **width of the house** (~512) to start. 2. Switch to the Edge Tool (`2`), select the **two edges** on the ground mesh, switch to the **Scale** move mode, then hold `Shift` and scale the sides out about **520 units**. 3. Switch to the **Move / Position** move mode, select those **two edges**, and hold `Shift` to drag them out and fit the **length of the house** — about **528 units**. 4. Select the **two edges** running along the house and press `B` to **bridge** them, filling the ground in around the house. 5. Just like the doorway bridge, this leaves the ground as a generic `Block` in the Hierarchy. Right-click it and choose **Rename** (`F2`), and name it `Ground` before we move on to texturing.

[![](https://cdn.sbox.game/upload/b/4cadea9c/5d27/4b8a/829d/1cb0f07dc14f.png)](https://cdn.sbox.game/upload/b/4cadea9c/5d27/4b8a/829d/1cb0f07dc14f.png)  
[![](https://cdn.sbox.game/upload/b/7bc39d8c/f5fb/41a1/aa07/e155a725c9d8.png)](https://cdn.sbox.game/upload/b/7bc39d8c/f5fb/41a1/aa07/e155a725c9d8.png)  
[![](https://cdn.sbox.game/upload/b/3011a05a/3130/4e06/ba0b/c30a6811369d.png)](https://cdn.sbox.game/upload/b/3011a05a/3130/4e06/ba0b/c30a6811369d.png)  
[![](https://cdn.sbox.game/upload/b/b3e47751/26b2/438a/bd15/239177043624.png)](https://cdn.sbox.game/upload/b/b3e47751/26b2/438a/bd15/239177043624.png)  
[![](https://cdn.sbox.game/upload/b/9187d364/f5c1/4ae1/b3cf/6395d2cc9455.png)](https://cdn.sbox.game/upload/b/9187d364/f5c1/4ae1/b3cf/6395d2cc9455.png)

**Tip — Faster way to line things up: while you're holding** **`Shift`** **and extending, watch for a red circle that appears on nearby geometry — that's a vertex snap point. Keep left-click held and move your mouse onto it, and your transform snaps right to that vertex. Makes mesh manipulation way quicker!**

[![](https://cdn.sbox.game/upload/b/8a6ed0ca/4ab5/4673/a388/8e8bdba1b34f.png)](https://cdn.sbox.game/upload/b/8a6ed0ca/4ab5/4673/a388/8e8bdba1b34f.png)

[![](https://cdn.sbox.game/upload/b/33699dcf/2310/4c2e/bd09/ea94cd951cf9.png)](https://cdn.sbox.game/upload/b/33699dcf/2310/4c2e/bd09/ea94cd951cf9.png)  
[![](https://cdn.sbox.game/upload/b/2444e69f/4c49/4b8f/9ffb/8a85c52bc8ba.png)](https://cdn.sbox.game/upload/b/2444e69f/4c49/4b8f/9ffb/8a85c52bc8ba.png)  
[![](https://cdn.sbox.game/upload/b/cf98e1b0/ef8d/4d1b/8325/3d4af186a63f.png)](https://cdn.sbox.game/upload/b/cf98e1b0/ef8d/4d1b/8325/3d4af186a63f.png)  
  
[![](https://cdn.sbox.game/upload/b/6d46c934/22d7/45c1/bd22/dab468f26792.png)](https://cdn.sbox.game/upload/b/6d46c934/22d7/45c1/bd22/dab468f26792.png)  
  
[![](https://cdn.sbox.game/upload/b/2f520987/11f1/44b6/a8e9/d52f305724db.png)](https://cdn.sbox.game/upload/b/2f520987/11f1/44b6/a8e9/d52f305724db.png)

# Section 10: Texturing

Now we make it look like a house. The geometry's done, so this is the fun part — swapping the dev textures for real materials. We'll texture the **exterior** here, then do the interior next.

## Exterior Design

**Set up your material palette**

1. Enter the Face Tool (`3`). Down in the material palette (bottom-left), right-click the **`+`** and choose **Set Material**. That opens the asset picker, which has an **Asset Browser** tab and a **Cloud Browser** tab.
2. On the **Asset Browser** tab, select the **Everything** category. That surfaces all of s&box's default assets — plenty of materials, dev textures included.
3. Search **Dev** in the top-right search box, just so you know where the dev textures live for later. A bunch show up, but the window's stuck in list view.
4. Click the view button and pick **Large Icons** so you can actually see the thumbnails.
5. Now grab a few materials to work with. Keeping it basic, search for and add these:
   - `materials/grass/floor_grass_a.vmat_c`
   - `models/props/brick_single/brick_single_a.vmat_c`
   - `models/props/brick_single/brick_single_painted.vmat_c`
   - `materials/roofing/roof_bitumen_panels.vmat_c`
   - `materials/concrete/floor/concrete_polished_02_blend.vmat_c`
   - `materials/generic/wall_brick_b.vmat_c`
   - `materials/concrete/floor/floor_tile_blend_02.vmat_c`
   - `materials/dev/dev_nonmetal_rough00.vmat_c`

**Tip —** You can also drag materials straight in from the Asset Browser at the bottom of the editor — onto the palette, or right onto a face.

[![](https://cdn.sbox.game/upload/b/d45510ab/e7ba/4be0/a9d4/c754fd210b8c.png)](https://cdn.sbox.game/upload/b/d45510ab/e7ba/4be0/a9d4/c754fd210b8c.png)

[![](https://cdn.sbox.game/upload/b/81a0beff/9019/4b58/b1cf/8a92990cb8d7.png)](https://cdn.sbox.game/upload/b/81a0beff/9019/4b58/b1cf/8a92990cb8d7.png)

[![](https://cdn.sbox.game/upload/b/8c7b3ccc/1c87/42f8/b421/8928c5625968.png)](https://cdn.sbox.game/upload/b/8c7b3ccc/1c87/42f8/b421/8928c5625968.png)

[![](https://cdn.sbox.game/upload/b/83bb3f5d/85e7/4ea0/9138/e24e33206ebb.png)](https://cdn.sbox.game/upload/b/83bb3f5d/85e7/4ea0/9138/e24e33206ebb.png)[![](https://cdn.sbox.game/upload/b/cedaf817/e95f/4edb/a903/385e9a0edb5e.png)](https://cdn.sbox.game/upload/b/cedaf817/e95f/4edb/a903/385e9a0edb5e.png)

## **Texture the ground and front wall**

## First, turn off the **Visualize Scene Objects** debug view from earlier so you can actually see your materials.

1. ## Left-click your **grass** vmat in the palette to make it the active material.
2. ## Double-click a **Ground** face to select all of its faces, then press `Shift+T` to apply the grass.
3. ## For the front of the house, `Alt+Shift+Double-Left-Click` a face to grab all the front faces at once, then apply `materials/generic/wall_brick_b.vmat_c`.

[![](https://cdn.sbox.game/upload/b/079681c6/d032/42d1/8994/05d59b38f296.png)](https://cdn.sbox.game/upload/b/079681c6/d032/42d1/8994/05d59b38f296.png)  
  
[![](https://cdn.sbox.game/upload/b/d3aa2697/ea94/47f2/a668/6ec02017e3a9.png)](https://cdn.sbox.game/upload/b/d3aa2697/ea94/47f2/a668/6ec02017e3a9.png)  
  
[![](https://cdn.sbox.game/upload/b/f2dd7348/239e/4c33/9295/7a0875106836.png)](https://cdn.sbox.game/upload/b/f2dd7348/239e/4c33/9295/7a0875106836.png)  
  
  
  
[![](https://cdn.sbox.game/upload/b/83b199f5/82f5/45a8/a6e7/d5deb4a51e21.png)](https://cdn.sbox.game/upload/b/83b199f5/82f5/45a8/a6e7/d5deb4a51e21.png)

# **Align the brick to the grid**

**The brick comes in at the wrong scale. Under the Texture section, use Align → Align to Grid to snap it to a realistic size.**

**Info —** Align to Grid won't fix every material — they're not all authored at the same scale. It's just the first thing to try when a texture looks too big or too small.

[![](https://cdn.sbox.game/upload/b/c9162b84/c876/4d90/ae3e/b762115b546a.png)](https://cdn.sbox.game/upload/b/c9162b84/c876/4d90/ae3e/b762115b546a.png)

# **Copy the material to the rest of the walls**

## Here's a clean way to texture the other walls while keeping your alignment intact:

1. ## Left-click a face that already has the brick on it.
2. ## `Shift+Right-click` that face to copy its material **and** its settings.
3. ## `Ctrl+Right-click` another wall face to apply the same material with the same settings.
4. ## Keep `Ctrl+Right-clicking` the rest of the exterior walls.

[![](https://cdn.sbox.game/upload/b/2a554377/bc8e/4187/9f90/a0b64923cce9.png)](https://cdn.sbox.game/upload/b/2a554377/bc8e/4187/9f90/a0b64923cce9.png)

# 

## **Texture the roof**

1. ## Make `materials/roofing/roof_bitumen_panels.vmat_c` your active material.
2. ## `Alt+Shift+Double-Left-Click` both roof slants to grab all their faces, press `Shift+T`, then **Align to Grid** again.

[![](https://cdn.sbox.game/upload/b/86dfeebe/066c/457e/8b38/143c1e047f1b.png)](https://cdn.sbox.game/upload/b/86dfeebe/066c/457e/8b38/143c1e047f1b.png)  
  
[![](https://cdn.sbox.game/upload/b/ee1adaf1/7284/445a/aca2/86554ac980fc.png)](https://cdn.sbox.game/upload/b/ee1adaf1/7284/445a/aca2/86554ac980fc.png)

## **Add the metal roof trim**

We need a metal material — and here's another way to find one:

1. ## Click the **Asset Browser**, hit the **folder (Local)** icon, choose **Everything**, and search **Metal**.
2. ## All sorts of things show up, so filter to materials only: click the **filter** icon to the right of the search box and tick **Material** — now only vmats show.
3. ## Pick any metal you like (play around with materials as you go). We'll use `materials/dev/dev_metal_rough60.vmat_c` for the trim.
4. ## Drag it into your palette — or straight onto a face, your call.
5. ## `Alt+Shift+Double-Left-Click` the roof's side faces all the way around, plus the bottom — about **8 faces** total — and apply `dev_metal_rough60`.

[![](https://cdn.sbox.game/upload/b/963e7414/7ed8/40b5/aefc/babad31e59a4.png)](https://cdn.sbox.game/upload/b/963e7414/7ed8/40b5/aefc/babad31e59a4.png)  
  
[![](https://cdn.sbox.game/upload/b/bde5c385/261d/4887/a877/f7d3463a55d1.png)](https://cdn.sbox.game/upload/b/bde5c385/261d/4887/a877/f7d3463a55d1.png)  
  
[![](https://cdn.sbox.game/upload/b/7f7bc771/2c29/458e/95ef/7f407fe6f0e3.png)](https://cdn.sbox.game/upload/b/7f7bc771/2c29/458e/95ef/7f407fe6f0e3.png)

[![](https://cdn.sbox.game/upload/b/1de979e8/688c/451b/b5a9/990a565befca.png)](https://cdn.sbox.game/upload/b/1de979e8/688c/451b/b5a9/990a565befca.png)
