---
title: Creating a Map Project
slug: facepunch/map-project
url: https://sbox.game/learn/facepunch/map-project
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Mapping
content_type: Text
tags: [game, map, mapping, project]
rating: 3
views: 137
upvotes: 4
downvotes: 0
updated: Updated yesterday
summary: This guide explains how to create a map project that targets a specific game.
scraped_at: '2026-05-23T08:22:57Z'
---

# Creating a Map Project

> This guide explains how to create a map project that targets a specific game.

# **Setting up a project**

This guide shows how to set up a map project so mappers can build maps for a specific game. In this example, we will target Sandbox. (<https://sbox.game/facepunch/sandbox>)

Open the editor and click **New Project**.

[![](https://cdn.sbox.game/upload/b/ea6c6c7e/0fad/46a3/a1c9/2c44530c7f92.png)](https://cdn.sbox.game/upload/b/ea6c6c7e/0fad/46a3/a1c9/2c44530c7f92.png)

In the template list, select **Map**.

Set your project **Title**, **Ident**, and **Location** path, then create the project.  
[![](https://cdn.sbox.game/upload/b/2a9b76aa/fdc4/46bb/830c/462f6b4bffb0.png)](https://cdn.sbox.game/upload/b/2a9b76aa/fdc4/46bb/830c/462f6b4bffb0.png)

After the editor loads, click the **cog** icon in the top-right to open **Project Settings**.  
[![](https://cdn.sbox.game/upload/b/37735e19/1bde/483c/b73e/427dd68f653b.png)](https://cdn.sbox.game/upload/b/37735e19/1bde/483c/b73e/427dd68f653b.png)

Find **Target Game** and click it. In the popup, select **Sandbox** (or any game you want to target), then click **OK**.[![](https://cdn.sbox.game/upload/b/49035f90/3b46/4a79/87c5/00b4485b3a0d.png)](https://cdn.sbox.game/upload/b/49035f90/3b46/4a79/87c5/00b4485b3a0d.png)

Back in **Project Settings**, confirm the target game is set, then click **Save**.

Confirm the restart prompt. The editor needs to restart to apply the parent package change.

[![](https://cdn.sbox.game/upload/b/d4ddbdb7/78dc/40fa/80e2/deed38ab7138.png)](https://cdn.sbox.game/upload/b/d4ddbdb7/78dc/40fa/80e2/deed38ab7138.png)When the editor opens again, press

**Play**. You should now be playing inside Sandbox from your map project.

[![](https://cdn.sbox.game/upload/b/efd4eb43/4d90/43a9/b90d/829cafc16f34.png)](https://cdn.sbox.game/upload/b/efd4eb43/4d90/43a9/b90d/829cafc16f34.png)

You may need to remove the camera in your scene before testing, this is because most games will spawn their own camera in.

# **Using game components and prefabs**

Some games ship with their own components and prefabs, such as ammo pickups.

To find them, open the **Asset Browser**, then find and select the folder for the game you are targeting (for example, **Sandbox**). From there, you can browse and place those game-specific assets into your map.[![](https://cdn.sbox.game/upload/b/641f7626/ee98/46bd/90d8/b3e77bb71bd1.png)](https://cdn.sbox.game/upload/b/641f7626/ee98/46bd/90d8/b3e77bb71bd1.png)
