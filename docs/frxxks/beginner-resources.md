---
title: 🎓 Freaks Beginner Resources
slug: frxxks/beginner-resources
url: https://sbox.game/learn/frxxks/beginner-resources
author: Frxxks
author_slug: frxxks
difficulty: Beginner
topic: Editor
content_type: Video
tags: [beginner, collection, compilation, first]
rating: 5
views: 2618
upvotes: 21
downvotes: 0
updated: Updated 14 days ago
summary: A comprehensive beginners resource collection helping you getting started
  with game development in s&box.
scraped_at: '2026-06-01T11:39:57Z'
---

# 🎓 Freaks Beginner Resources

> A comprehensive beginners resource collection helping you getting started with game development in s&box.

[![](https://cdn.sbox.game/upload/b/6f5b7ec8/3b91/4098/8919/ee1cdd1a08d8.png)](https://cdn.sbox.game/upload/b/6f5b7ec8/3b91/4098/8919/ee1cdd1a08d8.png)

# 👋🏻 Welcome!

In this guide you will find a collection of helpful resources that will get you started with the basics of developing a game for s&box.  
This is just a personal list of things I found really helpful when I just started developing for s&box. I hope these resources will help you just as much as they did help me.  
  
Before we head into the thick of things, be aware that...

[Facepunch  provides their own "Getting Started" documentation](https://sbox.game/dev/doc/getting-started).   
You should check it out first!

Furthermore, [as of April 2026, the S&Box Docs have been made officially open source](https://sbox.game/news/update-26-04-08#documentation-open-source). You can check out the [Github Page here](https://github.com/Facepunch/sbox-docs/).  
  
I will make heavy use of links in this guide that directly brings you to the relevant docs sections.

## 📄 Other Beginner resources:

> - [Expansive Beginner Resources Github Page](https://github.com/CSEliot/sbox-resources)  
>   (Thanks @cseliot)

# 🚀 Launching the Editor

As outlined in the [Download & Install Documentation](https://sbox.game/dev/doc/getting-started/installation) the editor can be found in the Steam Tools Section called "*s&box editor*".  
Just install it and launch it trough Steam. Simple right?

If, for some reason, this shouldn’t work, there is a **Workaround** for this!  
Simply **start the sbox-dev.exe** from within the game folder. Make sure it’s the **game** folder you’re looking in and not the editor folder.   
( Just right-click the game in Steam > Manage > Browse local files and double click the sbox-dev.exe file )

Once the launcher is started, you can create a new project or open the default "Sweeper" project for reference.

# **💻 Setting up your Project Locally**

After clicking the **"+ New Project..."** button, you will be greeted by a new window where you can select which **Project Type** you want to create and what name, identifier and the location on your drive it should have.  
  
Currently there are 5 types of projects:

## 👾 **Game - Empty**

> - Use this if you want to create a **Game** for s&box.
> - This is your full "Game" Editor tools, very similar to Unity and Godot.

## 👾 **Game - Player Controller**

> - Contains prefabs for various PlayerController such as: First Person, Third Person and Top Down.

## 👾 **Addon**

> - Use this if you just want to make a general purpose **Map** or a **Model** and upload it into the s&box cloud.
> - These can then be accessed by game developers via the cloud asset browser or by people in the Sandbox Mode's spawn menu.
> - [Addon Projects](https://sbox.game/dev/doc/getting-started/project-types/addon-project) cannot contain code yet, however [Actiongraph](https://sbox.game/dev/doc/editor/actiongraph/intro-to-actiongraphs/) is available for them.

## 👾 **Map**

> - Use this if you want to make a **Map** for any  Game.
> - Perfect for when you just want to make a generic map that can then be used by developers or as a map in Sandbox.

## 👾 **Sandbox Game Addon**

> - Use this if you want to make a **Custom Scripted Entity** specifically for the **Sandbox Mode**.
> - Contains example Scripted Entities for Sandbox.
> - As of now, you can only create Scripted Entities (sents) spawned through the spawn menu. You cannot currently use this to create custom tools.

This guide is assuming you're using the **"Game - Empty"** project type, since all other project types share the same editor environment as "Game - Minimal" but only differ in their restrictions on what type of features you can use.

# 🖥️ Code Tips

## ⚙️ **Setup your IDE**

Make sure you have an [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) installed.  
There are currently 3 officially supported IDE's available: [Visual Studio](https://visualstudio.microsoft.com/), Visual Studio Code and [Rider](https://www.jetbrains.com/rider/). You can change the selected compatibility from the "Edit > Preferences" Menu.  
  
**However** if you know how, you can still set up any IDE of your choice to code for s&box, but you might run into issues. [As you can read in this handy guide](https://sbox.game/learn/brax/ide-setup) ( thanks @braxen ) , there may be further setup needed for the IDE of your choice. Make sure to follow these instructions to get the best experience.

## 🧑🏻‍🎓 **Learn "C#"**

> - [Microsoft's Learning Center C# Course](https://dotnet.microsoft.com/en-us/learn/csharp)
> - [W3schools C# Tutorial](https://www.w3schools.com/cs/index.php)

## 📄 **s&box API reference**

> - [API reference site](https://sbox.game/api)

## 📄 **Other helpful API documentation**

> - [HideInGame bool flag](https://sbox.game/api/Sandbox.MeshComponent/HideInGame)

# 

# ⚙️ **Components**

## 📄 **Property Attributes**

> - [Property Attributes (Custom Inspector Elements)](https://sbox.game/dev/doc/editor/property-attributes)

## 🧑🏻‍🎓 How to set up a Custom Component

> ```
> /// <summary>
> /// My cool custom component description here.
> /// </summary>
>
> [Title( "My Custom Component" )]
> [Category( "My Custom Category" )]
> [Icon( "settings" )] // https://fonts.google.com/icons?icon.set=Material+Icons
> [Alias( "Cool Component" )]
>
> public partial class MyCustomComponent : Component
> {
> // Your component code goes here...
> }
> ```

## 🧑🏻‍🎓 **Buttons in the Inspector**

> ```
> [Button, Title("Press Me!"), Description("This appears when you hover the button")]
> public void TestButton()
> {
>   Log.Info( "Button Pressed!" );
>   // Put the code for what the button should do here.
> }
> ```

# 🔗 Helpful Documentation Links

## 📄 **Notable Doc Pages**

> - [s&box C# Cheat Sheet](https://sbox.game/dev/doc/code/code-basics/cheat-sheet)
> - [Property Attributes (Custom Inspector Elements)](https://sbox.game/dev/doc/editor/property-attributes)
> - [Components](https://sbox.game/dev/doc/scene/components/)
> - [Execution Order](https://sbox.game/dev/doc/scene/components/execution-order)
> - [Events](https://sbox.game/dev/doc/scene/components/events/)
> - [Custom Assets / Game Resources](https://sbox.game/dev/doc/assets/resources/custom-assets)

## 🧑🏻‍🎓 **Learn Razor**

> - [Microsoft Docs Razor Page](https://learn.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start)
> - [W3schools Razor Tutorial](https://www.w3schools.com/Asp/webpages_razor.asp)
> - [Cool cheat sheet by Braxen](https://sboxtricks.dongers.net/sbox/2025/11/20/razor-component-aliases.html)

## 🧑🏻‍🎓 **Learn Flexbox**

> - [Flexbox Froggy Interactive Tutorial](https://flexboxfroggy.com/)

## 🔗 **Other Helpful Links**

> - [Icons Reference for use in the editor](https://fonts.google.com/icons?selected=Material+Icons)
> - [250GB of sound fx files already extracted](https://huggingface.co/buckets/lu2000luk/sfx)  
>   (Thanks @lu2000luk)

## 🔗 **Helpful s&box Github Projects**

> - [Sandbox - by Facepunch](https://github.com/Facepunch/sandbox)
> - [Nicked - by Facepunch](https://github.com/Facepunch/sbox-hc1)
> - [Clover Meadows](https://github.com/MrBrax/clover_meadows_sbox)
> - [Fortwars](https://github.com/Nolankicks/Fortwars)
> - [My Summer Cottage (GameJam Version)](https://github.com/Small-Fish-Dev/My-Summer-Cottage-Jam)
> - [Pizza Clicker](https://github.com/CarsonKompon/pizza_clicker)
> - [Grubs](https://github.com/apetavern/grubs)
> - [Voxel-Party](https://github.com/DrakeFruit/Voxel-Party)
> - [DarkRP Sandbox Edition](https://github.com/sousou63/DarkRP)

## 🐧 **Linux**

> - [s&box Linux Discord](https://discord.gg/haZt7xbmBT)[Discord
>
>   Join the Unofficial s&box Linux Community Discord Server!
>
>   Check out the Unofficial s&box Linux Community community on Discord - hang out with 170 other members and enjoy free voice and text chat.](https://discord.gg/haZt7xbmBT)

[![](https://cdn.sbox.game/upload/b/b419bcfb/f196/4044/b198/15cb7ada1ae3.png)](https://cdn.sbox.game/upload/b/b419bcfb/f196/4044/b198/15cb7ada1ae3.png)

# 📽️ Videos

The following videos are up to date as of April 2026.  
Minor differences may still occur, as s&box constantly gets more features.

## 📽️ **Tutorial Series by Sandking**

> - [#1: Up to date complete beginner Video Tutorial ( 28th of April 2026 )](https://youtu.be/PmB5ADahw-Y?is=gWxKR3pSXLhe2i9y)
> - [#2: Learn the Editor](https://youtu.be/35bO0PpZ0Ro)
> - [#3: How to make a Rolling Ball s&box game](https://youtu.be/HT7d-G0vnw8)
> - [#4: Prefabs and the Action Graph](https://youtu.be/myfndemMkBI)
> - [#5: Syntax Highlighting and C# Primer](https://youtu.be/_SYO7jZrdjM)

> - [Rest of the Playlist](https://www.youtube.com/watch?v=PmB5ADahw-Y&list=PLBXcZnvT6oSQDv0hrgFsncGPAS0mj609P)

> - [How to use s&box scene mapping](https://youtu.be/VXwkXe4_Bdw?is=VJO19H1sFq5dD4pT)  
>   ( thanks @Sandking for all of the above)

> - [Scene Mapping feature overview](https://youtu.be/5EF7eQBur7w)

The following videos may be outdated or are very old and do not reflect the current version of s&box and can show features that no longer exist. Feel free to check them out anyway.

## ⌛ **Older Helpful beginner videos**

> - [Fish School Beginner Playlist](https://www.youtube.com/watch?v=g-ZJFnWPawY&list=PLIcPBTNc7_9oFEEoHSCuPrdGQnU27yLuj)  
>   ( thanks @ubre )

> - [How to use Trigger/Collision Listeners in S&box](https://youtu.be/mgZY9Z4dhVg)
> - [How to make UI](https://youtu.be/4J37tgZ1Qmo)
> - [[Property] Attributes](https://youtu.be/gY5PgW5pH90)  
>   ( thanks @carson )

> - [How To Make Your First S&box Game](https://youtu.be/7ClonlOIMFE)  
>   ( thanks @eridium )

> - [Async Tasks Tutorial](https://www.youtube.com/watch?v=sZPA6Bj_k9g)  
>   ( thanks @derrikcreates )

## 📺 **Other helpful YouTube channels**

> - [Brackey Youtube Channel](https://www.youtube.com/@Brackeys) - Learn to Code for various game engines
> - [Spaderdabomb Youtube Channel](https://www.youtube.com/@spaderdabomb) - Some good Coding tutorials
> - [Code Laboratory Youtube Channel](https://www.youtube.com/@CodeLaboratory) - Good 2D Unity tutorials
