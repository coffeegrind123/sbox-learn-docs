---
title: Resource Files
slug: brax/resource-files
url: https://sbox.game/learn/brax/resource-files
author: Braxnet
author_slug: brax
difficulty: Beginner
topic: Platform
content_type: Text
rating: 3
views: 1168
upvotes: 4
downvotes: 0
updated: 'Updated

  32 Days Ago'
summary: If your published game has missing images, check this out
scraped_at: '2026-06-23T09:43:08Z'
---

# Resource Files

> If your published game has missing images, check this out

When you publish a game, compiled resources will automatically be included in the build. However, things like image files (PNG, JPG, etc.), sound files (WAV, MP3, etc.), and other non-compiled assets need to be explicitly added to “Resource Files” in your project settings to be included in the final build.

Go to **⚙️ > Other** and you’ll find a section called **Resource Files**. Here, you can add any files or folders that you want to be packaged with your game.

[![](https://cdn.sbox.game/upload/b/b63cb17e/726f/4778/9537/ca137d689416.png)](https://cdn.sbox.game/upload/b/b63cb17e/726f/4778/9537/ca137d689416.png)By “wildcards”, it means you can use patterns like `*.png` to include all PNG files, or `images/*` to include all files in the “images” folder. This is useful for including multiple assets without having to add each one individually.

`images/*.png` will include all PNG files in the “images” folder.

**Do NOT include “assets” at the start of the path**, as the engine automatically looks for resources in the “assets” directory of your project.

**Do NOT include “materials/*” or “models/*“** and the like, as the engine automatically uploads all compiled resource (extension ending in _c). If you use a wildcard to also upload the source files (without _c), it may cause issues on clients, as they will try to load the source files instead of the compiled versions. If you only need to include specific uncompiled resources, you can add them individually like `materials/my_image.png`.

After saving your settings, publish your game again, and the specified resource files should now be included in the build.
