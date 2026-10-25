---
title: 🧧 Basic resources tutorial
slug: redkite/basic-game-resources-tutorial
url: https://sbox.game/learn/redkite/basic-game-resources-tutorial
author: redkite
author_slug: redkite
difficulty: Beginner
topic: Editor
content_type: Text
tags: [editor, resources, ui]
rating: 0
views: 16
upvotes: 0
downvotes: 0
updated: 'Updated

  2 days ago'
summary: A beginner friendly walk through to defining and creating your own assets
  using resources.
scraped_at: '2026-10-25T00:05:06Z'
---

# 🧧 Basic resources tutorial

> A beginner friendly walk through to defining and creating your own assets using resources.

# A tutorial on how to create basic game resources

A beginner friendly walkthrough to defining your own asset types in s&box similar to ScriptableObjects in Unity or Resources in Godot.

## Prerequisites

- Foundational understanding of how Razor, specifically parent/child components. Not 100% required if you are only here for resource tutorial.  I have another tutorial here on UI if you need <https://sbox.game/learn/redkite/razor-basics-text-buttons-events>
- A new and empty game scene or project.

## What you will build

- A custom `Weapon` asset type you can create and edit in the editor.
- A row of cards in the centre of the screen. Each card displays the data from one weapon asset.[![](https://cdn.sbox.game/upload/b/4e2225de/e25f/4802/b7cb/eef82314e7d7.png "Example of what we will be building")](https://cdn.sbox.game/upload/b/4e2225de/e25f/4802/b7cb/eef82314e7d7.png)

## What is a resource and why would we use it?

Just so I'm not assuming everyone knows what it is.   
  
It's basically a file that stores data for your game. You make the shape of the data once then you can create as many data files from that as you like. In this tutorial we will be making a weapon so think of the resource as a template for the weapons we will create. The template will say "every weapon has a name, damage and range" and then we can go ahead and follow the template by filling out those values.   
  
Why would we use this instead of just writing it onto a class?

- Data lives outside of your code so to rebalance the bow, you edit `Hammer.weapon` in the editor.
- You write one class. Adding a new weapon means adding a file, not more code.
- Anything can use it. The UI, the player's attack and a shop can all read the same `Bow.weapon`, so the numbers stay consistent.
- It's easy to edit. Designers and beginners can change values in the inspector without reading code.

If you want more of an understanding I'd recommend looking up some tutorials on Godot resources or Unity scriptable objects to further understand if its unclear.

## 1. Create the resource type

Inside our code folder lets create a file called `WeaponResource.cs`

```
using Sandbox;

[AssetType( Name = "Weapon definition", Extension = "weapon", Category = "Weapons" )]

public class WeaponResource : GameResource {    

    [Property] public string Name { get; set; } = "Weapon";    

    [Property] public float Damage { get; set; } = 10f;    

    [Property] public float Range { get; set; } = 500f;

}
```

How the above works:

- `[AssetType]` sets the display name, the file extension (in our case `.weapon`) and then the category in the editor which will make more sense shortly.
- `[Property]` fields appear in the assets inspector and are saved in the file.
- More details can be found be found here <https://sbox.game/dev/doc/assets/resources/custom-assets>

## 2. Create some weapon assets

Once created, right click in our asset file directory and we should see a new asset option called `Weapons` which was our `Category` name.   
Select Weapon definition to create a new Weapon asset.  [![](https://cdn.sbox.game/upload/b/ef1a9066/2950/4b6e/a24e/889fa49f3904.png "Create a new weapon asset using our weapon resource")](https://cdn.sbox.game/upload/b/ef1a9066/2950/4b6e/a24e/889fa49f3904.png)Name this Weapon Hammer (or whichever name you like).   
  
Double click on the newly create hammer asset, this show your weapon in the inspector (see example below).   
  
Add a Damage, Name and  Range as you see fit for the hammer. Then repeat the same steps for a bow and sword. I've done mine as the following but feel free to do your own:

[![](https://cdn.sbox.game/upload/b/6ce87a14/ce6a/4d7d/81dd/b720a7c441bf.png "Set up hammer asset values")](https://cdn.sbox.game/upload/b/6ce87a14/ce6a/4d7d/81dd/b720a7c441bf.png)[![](https://cdn.sbox.game/upload/b/bc840173/af42/4bcf/8f01/f3cd61318713.png "Setup bow asset values")](https://cdn.sbox.game/upload/b/bc840173/af42/4bcf/8f01/f3cd61318713.png)[![](https://cdn.sbox.game/upload/b/a814993d/3e86/4215/9073/235958928de4.png "Set up sword asset values ")](https://cdn.sbox.game/upload/b/a814993d/3e86/4215/9073/235958928de4.png)

## 3. Create the card UI

You could end the tutorial here if you like given that we have already covered the resource creation otherwise we will continue with setting up some basic UI. I have a UI tutorial here if you have unfamiliar: <https://sbox.game/learn/redkite/razor-basics-text-buttons-events>   
  
Create a Screen panel component and then create a razor component called `WeaponCards.razor` with a supplement `WeaponCards.razor.scss` file.   
  
Add the following code to your `WeaponCards.razor` file

```
@using Sandbox;
@using Sandbox.UI;
@inherits PanelComponent

<root>
    @foreach ( var weapon in Weapons )
    {
        <div class="card">
            <div class="name">@weapon.Name</div>
            <div class="stat"><label>Damage</label><span>@weapon.Damage</span></div>
            <div class="stat"><label>Range</label><span>@weapon.Range</span></div>
        </div>
    }
</root>

@code
{
    [Property] public List<WeaponResource> Weapons { get; set; } = new();
}
```

Then add this to your `WeaponCards.razor.scss` file.

```
WeaponCards {
    position: absolute;
    width: 100%;
    height: 100%;
    justify-content: center;
    align-items: center;
    gap: 24px;

    .card {
        flex-direction: column;
        width: 220px;
        padding: 24px;
        gap: 12px;
        background-color: #1f2430;
        border: 2px solid #4a90e2;
        color: white;

        .name {
            font-size: 28px;
            font-weight: 700;
            justify-content: center;
        }

        .stat {
            justify-content: space-between;
            font-size: 20px;
        }
    }
}
```

Attach our `WeaponCards.razor` screen to our screen panel.  Then within our list of weapons we want to add each of our weapon assets we created.

[![](https://cdn.sbox.game/upload/b/ee73b138/b860/4d99/b2de/223599a38d32.png "Add our Weapon cards UI panel to our Screen Panel")](https://cdn.sbox.game/upload/b/ee73b138/b860/4d99/b2de/223599a38d32.png)[![](https://cdn.sbox.game/upload/b/736982d6/0689/4f26/b3e3/18f8e3fd556a.png "Add our weapon assets to our Weapons list")](https://cdn.sbox.game/upload/b/736982d6/0689/4f26/b3e3/18f8e3fd556a.png)

Once we have added all 3 of our weapons when we press play we should be able to see the following UI:   
  
 [![](https://cdn.sbox.game/upload/b/4e2225de/e25f/4802/b7cb/eef82314e7d7.png "Example of final outcome")](https://cdn.sbox.game/upload/b/4e2225de/e25f/4802/b7cb/eef82314e7d7.png)

I'm planning to try make 1 tutorial per day, I know that a lot of new people have issues with the lack of tutorials and documentation. So hopefully this make it easier for new people to get straight into it but also avoid just AI slopping it out.  
  
I really like the s&box platform so I'm hoping creating a lot of tutorials that will assist in the success of s&box thus a good investment of my skills.   
  
Please give me feedback on the tutorials, any is appreciated thanks.
