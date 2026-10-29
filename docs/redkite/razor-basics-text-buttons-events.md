---
title: '🧧 Razor basics: text, buttons and events'
slug: redkite/razor-basics-text-buttons-events
url: https://sbox.game/learn/redkite/razor-basics-text-buttons-events
author: redkite
author_slug: redkite
difficulty: Beginner
topic: UI
content_type: Text
tags: [ui]
rating: 2
views: 105
upvotes: 1
downvotes: 0
updated: 'Updated

  16 days ago'
summary: A beginner friendly walk through for making simple interactive game UI.
scraped_at: '2026-10-29T12:28:10Z'
---

# 🧧 Razor basics: text, buttons and events

> A beginner friendly walk through for making simple interactive game UI.

# Razor UI Basics, text, buttons and events

A  beginner friendly walk through for making simple interactive game UI.

## What you will build

- Simple text showing how much health we have
- A button to remove the health[![](https://cdn.sbox.game/upload/b/2f6c39d9/9f2a/4c3b/b8f4/2cdf4981df2f.gif "Example of what we will be building")](https://cdn.sbox.game/upload/b/2f6c39d9/9f2a/4c3b/b8f4/2cdf4981df2f.gif)

## Prerequisites

- A new and empty game scene or project
- Very basic understanding of the editor e.g. what scenes are, how to create entities, the hierarchy view etc.
- Foundational understanding of HTML, CSS and Razor or any similar framework like React, Vue etc.

## 1. Create the HUD object

Open or create a new scene.   
Create a new screen component in our hierarchy view and rename it to "Screen Panel"   
Then add a new **razor component** on that same object and name it `PlayerHUD` this will create two files: `PlayerHUD.razor` and `PlayerHUD.razor.scss`  
Save this where you please in your file system.

[![](https://cdn.sbox.game/upload/b/615c651d/0de5/4777/9f0e/43af13007f70.png "Create screen component in hierachy.")](https://cdn.sbox.game/upload/b/615c651d/0de5/4777/9f0e/43af13007f70.png)[![](https://cdn.sbox.game/upload/b/0470006c/bd50/4f55/b187/f52a226d8745.png "Add new razor component to Screen panel")](https://cdn.sbox.game/upload/b/0470006c/bd50/4f55/b187/f52a226d8745.png)

## 2. Add health text and button to razor component

Open `PlayerHUD.razor` and replace its content with the following

```
@using Sandbox;
@using Sandbox.UI;
@inherits PanelComponent
@namespace Sandbox

<root>
	<div class="health">@HealthText</div>
	<button onclick=@TakeDamage>take damage</button>
</root>

@code
{
	public int Health { get; set; } = 100;

	string HealthText => Health <= 0 ? "u died" : $"Health {Health}";

	void TakeDamage()
	{
		if ( Health <= 0 )
		{
			return;
		}

		Health -= 25;
	}
}
```

The above is a super simple example of a button that reduces our health by 25 whenever it is pressed. Feel free to check your changes now to see our button and text on screen. You should have something like this:   
  
[![](https://cdn.sbox.game/upload/b/2b62d3d0/7a03/41a4/a0e6/92dab51cc795.png "Example of our razor changes")](https://cdn.sbox.game/upload/b/2b62d3d0/7a03/41a4/a0e6/92dab51cc795.png)

## 3. Style our component

Open `PlayerHUD.razor.scss` and replace it with this:

```
PlayerHUD
{
	width: 100%;
	height: 100%;
	background-color: rgba(68, 68, 68, 0.35);
	flex-direction: column;
	justify-content: center;
	align-items: center;
	font-weight: bold;
	pointer-events: all;

	.health
	{
		font-size: 64px;
		color: #fff;
	}

	button
	{
		font-size: 24px;
		color: #fff;
		background-color: #222;
		padding: 12px 24px;
		margin-top: 16px;
		cursor: pointer;
	}
}
```

Note that we must include `pointer-events: all;` as they are disabled by default. ([source](https://sbox.game/dev/doc/ui/interactions)). Once complete you should see the following:

# 3. Play test

Now that everything is done you can test out your changes.

## Sources & Resources

- Basic flow for creating UI: [How to make UI in s&box 2024](https://www.youtube.com/watch?v=4J37tgZ1Qmo)
- S&box UI docs: <https://sbox.game/dev/doc/ui/>
- Helpful breakdown on reactive state with Razor + S&box <https://sbox.game/learn/tesa/ui-buildhash>

I'm planning to try make 1 tutorial per day, I know that a lot of new people have issues with the lack of tutorials and documentation. So hopefully this make it easier for new people to get straight into it but also avoid just AI slopping it out.  
  
  
I really like the s&box platform so I'm hoping creating a lot of tutorials that will assist in the success of s&box thus a good investment of my skills.    
  
If you need help with anything message me on discord  **@barnyard6294**   
  
Please give me feedback on the tutorials, any is appreciated thanks.
