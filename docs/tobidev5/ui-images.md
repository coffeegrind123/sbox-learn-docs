---
title: Adding images to UI
slug: tobidev5/ui-images
url: https://sbox.game/learn/tobidev5/ui-images
author: tobidev5
author_slug: tobidev5
difficulty: Beginner
topic: UI
content_type: Text
tags: [css, image, images, panel]
rating: 3
views: 1240
upvotes: 4
downvotes: 0
updated: 'Updated

  43 Days Ago'
summary: How to add images to your razor ui
scraped_at: '2026-08-23T06:42:26Z'
---

# Adding images to UI

> How to add images to your razor ui

# Adding Images to your UI!

Adding images to s&box is harder than it seems, because they aren't automatically built into your game

# Creating the razor component:

```
@using Sandbox;
@using Sandbox.UI;
@inherits PanelComponent
@namespace Sandbox

<root>
 <div class>
 <img src=@IMAGE_PATH />
 </div>
</root>

@code
{
 public const string IMAGE_PATH = $"Ui/Images/example.png";
 protected override int BuildHash() => System.HashCode.Combine(IMAGE_PATH);
}
```

For example here, the image has to be in Assets/Images, and the name is `example.png`. You can always change the path, but keep in mind that the images have to be inside of Assets/ and you always have to add the file extension **(.png / .jpeg / .webp)**.

# To automatically create the component, we will use this .cs script:

```
using System;
public sealed class ImageComponent : Component
{
	public ScreenPanel screenPanel;
	public ImageExample UiElement;
	protected override void OnAwake()
	{
		screenPanel = GameObject.Components.GetOrCreate<ScreenPanel>();
		UiElement = GameObject.Components.GetOrCreate<ImageExample>();
	}
}
```

It is important that you name the Razor component `ImageExample.razor` for it to work, or change the class name in the C# script.  
Now, we will create a new empty GameObject in the scene and add the ImageComponent component to it.  
After saving the scene, you should see the image.

# Now you can add an SCSS file to style the image, named ImageExample.razor.scss, with this content:

```
root {
    justify-content: center;
    align-items: center;
}

div {
    width: 100%;
    height: 100%;

    justify-content: center;
    align-items: center;
}

img {
    width: 300px;
    height: 300px;

    border-radius: 16px;
    object-fit: cover;
}
```

It should now look something like this:[![](https://cdn.sbox.game/upload/b/442b6590/6941/4ecd/8f34/b92053ef6244.png)](https://cdn.sbox.game/upload/b/442b6590/6941/4ecd/8f34/b92053ef6244.png)The problem is that when starting a new game instance, we can't see the image anymore. So we have to go to **Settings -> Other -> Resource Files** and then put in our image path like this, ignoring the Assets/ folder. For example: **Ui/Images/***

[![](https://cdn.sbox.game/upload/b/3a9436d0/acb6/4288/8ffe/2ea7d588ecdc.png)](https://cdn.sbox.game/upload/b/3a9436d0/acb6/4288/8ffe/2ea7d588ecdc.png)[![](https://cdn.sbox.game/upload/b/889f056d/5fa8/4531/9846/b1dd17b8d9c0.png)](https://cdn.sbox.game/upload/b/889f056d/5fa8/4531/9846/b1dd17b8d9c0.png)

After that, we can start new instances of the game and the image will be there.

# Common Problems:

- If the image doesn't show up or takes up half of the screen, check if your scripts are named like this:[![](https://cdn.sbox.game/upload/b/103f2a04/da94/4fe0/aa90/d822b8e6f988.png)](https://cdn.sbox.game/upload/b/103f2a04/da94/4fe0/aa90/d822b8e6f988.png)
- Also, make sure that your image is in the right path and that you either changed the path in the script or use an image called**`example.png`****.**
- Make sure you have a GameObject with the Image component and that you saved the scene.
- Make sure you didn't forget the "*" in the resource file path:  
  `Correct: Ui/Images/*`  `Incorrect: Ui/Images/`
- If it still doesn't work you can join my [discord server](https://discord.gg/GqkKyyYyB) and ask for help:

# If this tutorial helped you, please rate it and leave a like
