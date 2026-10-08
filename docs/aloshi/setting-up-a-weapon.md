---
title: Setting Up a Basic Weapon
slug: aloshi/setting-up-a-weapon
url: https://sbox.game/learn/aloshi/setting-up-a-weapon
author: aloshi
author_slug: aloshi
difficulty: Beginner
topic: Gameplay
content_type: Text
tags: [basecombatweapon, viewmodel, weapon, worldmodel]
rating: 0
views: 77
upvotes: 0
downvotes: 0
updated: 'Updated

  7 days ago'
summary: Set up a pistol that can be added to the Inventory component's Loadout as
  a starting weapon. Works in first and third person.
scraped_at: '2026-10-08T12:59:50Z'
---

# Setting Up a Basic Weapon

> Set up a pistol that can be added to the Inventory component's Loadout as a starting weapon. Works in first and third person.

Since the [official docs](https://sbox.game/dev/doc/assets/ready-to-use-assets/first-person-weapons) are currently *very* light on details, here's a more detailed walkthrough on how to set up a weapon using the models available in the [sboxweapons package](https://sbox.game/facepunch/sboxweapons).

I'm not an experienced s&box developer. These are my notes as I stumbled through the process for the first time myself. Corrections welcome.

# Where we're going

Our end goal is to have a Prefab of a pistol (the USP) that can be added to the BaseInventoryComponent's Loadout as a starting weapon. The pistol will work in first and third person.  
  
The sboxweapons package provides models, but they're not set up as immediately-usable prefabs. To do this, we'll need to create a couple intermediate prefabs:

- The **ViewModel** prefab: this is what you see in first person while holding the gun.
- The **WorldModel** prefab: this is what other players see in your player model's hands (including you, when in third person mode).

After we've created those, we'll create the weapon prefab itself (with the BaseCombatWeapon component) and a scene to test it in.

# Creating the ViewModel Prefab (v_usp)

In the Asset Browser, create a new Prefab and name it v_usp.[![](https://cdn.sbox.game/upload/b/28cd2ee7/4bd9/4d42/a40d/a09508750651.png)](https://cdn.sbox.game/upload/b/28cd2ee7/4bd9/4d42/a40d/a09508750651.png)Double click it to open it in the editor.  
[![](https://cdn.sbox.game/upload/b/f791e41d/c841/4c96/bb5c/426404560ec2.png)](https://cdn.sbox.game/upload/b/f791e41d/c841/4c96/bb5c/426404560ec2.png)Add a Model Renderer (skinned) component to the root GameObject.[![](https://cdn.sbox.game/upload/b/ab4c46af/0563/4ba5/bb7c/678e069504b4.png)](https://cdn.sbox.game/upload/b/ab4c46af/0563/4ba5/bb7c/678e069504b4.png)Next, in the Asset Browser, go over to Cloud on the left, filter to Models, and search for the **ViewModel USP** model by Facepunch.

[![](https://cdn.sbox.game/upload/b/3a3a95e1/2016/465d/88ed/581b30a8f94c.png)](https://cdn.sbox.game/upload/b/3a3a95e1/2016/465d/88ed/581b30a8f94c.png)Now, *with the v_usp prefab's root GameObject still selected*, click and drag the **ViewModel USP** model into the Mesh Renderer (skinned) component's Model field.[](https://cdn.sbox.game/upload/b/56c9d5ef/6b9c/4ee2/9a57/3b67e8bb4d9e.mp4)

Next, we need to mark up where the bullets come from (the muzzle) and where shell casing eject from. First, check **Create Attachments** on the Model Renderer component. This will create two empty GameObjects as children of the root v_usp GameObject based on the attach points defined in the model.

[![](https://cdn.sbox.game/upload/b/2f3cf1bf/9ef8/4f30/a255/da26c09c4732.png)](https://cdn.sbox.game/upload/b/2f3cf1bf/9ef8/4f30/a255/da26c09c4732.png)[![](https://cdn.sbox.game/upload/b/34834a5c/b0bc/4483/b88e/3be733b7ce6e.png)](https://cdn.sbox.game/upload/b/34834a5c/b0bc/4483/b88e/3be733b7ce6e.png)

Add the Weapon Model component (sandbox.BaseWeaponModel) and fill in Renderer with the Model Renderer component above, and the Muzzle Game Object and Shell Eject Game Object with the two children we just created.  
[](https://cdn.sbox.game/upload/b/748435e8/65ad/4834/bcc7/64f8fdef58af.mp4)

If you skip setting up the Weapon Model component here, there will be no muzzle flash or bullets when you fire the gun.

# Creating the WorldModel Prefab (w_usp)

Again, create a new Prefab, this time name it w_usp, then open it. Again, add the Model renderer (skinned) component.[![](https://cdn.sbox.game/upload/b/1fb10899/0ee4/4467/b93f/14fd06ec9404.png)](https://cdn.sbox.game/upload/b/1fb10899/0ee4/4467/b93f/14fd06ec9404.png)

Open the Cloud section on the Asset Browser, filter to Models, search **USP**, drag it into the Model field on your w_usp prefab's root GameObject.[](https://cdn.sbox.game/upload/b/91fc5b14/2b7f/4b0b/8228/7ddbcaff6d11.mp4)  
Like we did for the the viewmodel prefab, check "Create Attachments" on the Model Renderer component, add the Weapon Model component, then fill in the Renderer, Muzzle Game Object, and Shell Eject Game Object fields.[![](https://cdn.sbox.game/upload/b/d73ce8a3/0bde/490b/b40f/564920fa64c6.png)](https://cdn.sbox.game/upload/b/d73ce8a3/0bde/490b/b40f/564920fa64c6.png)

# Creating the Weapon

Now we'll bring these two prefabs together to make the equippable weapon. Once again, create a new prefab and name it weapon_usp. Open it and add the Weapon component (sandbox.BaseCombatWeapon).[![](https://cdn.sbox.game/upload/b/b33bc2fd/fad3/4dda/8d0e/5917bfc34474.png)](https://cdn.sbox.game/upload/b/b33bc2fd/fad3/4dda/8d0e/5917bfc34474.png)Fill in Display Name = "USP".  
[![](https://cdn.sbox.game/upload/b/3fe383dd/71ce/46cb/b321/254fb1bda5ca.png)](https://cdn.sbox.game/upload/b/3fe383dd/71ce/46cb/b321/254fb1bda5ca.png)

Go to the ViewModel tab, click and drag your **v_usp.prefab** into the View Model Prefab field.  
[](https://cdn.sbox.game/upload/b/4b1d8348/ea39/4bb7/9c6b/8fa66dc888fa.mp4)In the WorldModel tab, drag **w_usp.prefab** into the World Model Prefab field. Set Hold Type to **pistol**.[![](https://cdn.sbox.game/upload/b/191cee07/e323/41a5/b07d/038fc125d062.png)](https://cdn.sbox.game/upload/b/191cee07/e323/41a5/b07d/038fc125d062.png)

# Testing it

## Creating the basic test scene

We're going to set up a basic scene with a player and some ground to stand on. This time, create a new **Scene** (e.g. usp_test) and open it.   
  
Add a new Plane:  
[![](https://cdn.sbox.game/upload/b/705b7ad6/a727/4341/a9a7/9b9f39453fa7.png)](https://cdn.sbox.game/upload/b/705b7ad6/a727/4341/a9a7/9b9f39453fa7.png)Add a Collider - Plane component so we can stand on it. Change the size from the default of (50, 50) to (100, 100) to match the model. [![](https://cdn.sbox.game/upload/b/256373e1/b798/4003/8c8b/3c63c3f42517.png)](https://cdn.sbox.game/upload/b/256373e1/b798/4003/8c8b/3c63c3f42517.png)Let's add a Sun, pointed downwards, to light things up.  Create -> Light -> Sun, set the X rotation to 90 (pointing down), and move it out of the way.[![](https://cdn.sbox.game/upload/b/468c768c/3952/440b/a81e/10a14c56f317.png)](https://cdn.sbox.game/upload/b/468c768c/3952/440b/a81e/10a14c56f317.png)  
Add a Camera and a PlayerController (both under the root of the "Create" menu):[![](https://cdn.sbox.game/upload/b/de051ef6/2243/4488/9ce6/7be3d66167e6.png)](https://cdn.sbox.game/upload/b/de051ef6/2243/4488/9ce6/7be3d66167e6.png)At this point you could press Play and control your sausage man.

## Equipping the Weapon

Add the "Inventory" component to the Player Controller GameObject.  
[![](https://cdn.sbox.game/upload/b/beb7d557/b8f3/4a2b/bbae/55e8ef5eb1d2.png)](https://cdn.sbox.game/upload/b/beb7d557/b8f3/4a2b/bbae/55e8ef5eb1d2.png)Click the '+' button and select Loadout.  
[![](https://cdn.sbox.game/upload/b/d551c9c0/66c3/457e/8e96/6eab3d102fe4.png)](https://cdn.sbox.game/upload/b/d551c9c0/66c3/457e/8e96/6eab3d102fe4.png)Under Starting Items, add your **weapon_usp.prefab**. [![](https://cdn.sbox.game/upload/b/38023121/33c0/4767/93a1/4deaaa317f5d.png)](https://cdn.sbox.game/upload/b/38023121/33c0/4767/93a1/4deaaa317f5d.png)

Press play, and...

[](https://cdn.sbox.game/upload/b/85c9ff71/3399/48ec/aff8/10617cd680e0.mp4)*In this footage I pressed "C" to switch to first-person partway through.*

# Wow, it's kinda busted

## Issue #1: The ViewModel is visible in third person

This seems to be the case in the official testbed game on s&box as well  (in the "viewmodel" test). 🤷  
  
A workaround is to add the "firstperson" tag to the "Render Exclude Tags" field on the Camera when in third person (BaseCombatWeapon automatically adds this "firstperson" tag to our ViewModel).  
  
Luckily, we can do this pretty easily with a custom component using [ICameraModifier](https://sbox.game/dev/doc/scene/components/reference/camera-effects). Create a new custom component named HideViewmodelThirdPerson on the Player Controller GameObject with this code:

```
using Sandbox;

public sealed class HideViewmodelThirdPerson : Component, ICameraModifier
{
	[RequireComponent]
	PlayerController playerController { get; set; }

	private const string firstPersonTag = "firstperson";

	public void ModifyCamera( CameraComponent camera, ref CameraView view )
	{
		if ( playerController.IsValid() )
		{
			if ( playerController.ThirdPerson && !camera.RenderExcludeTags.Contains( firstPersonTag ) )
				camera.RenderExcludeTags.Add( firstPersonTag );
			else if ( !playerController.ThirdPerson && camera.RenderExcludeTags.Contains( firstPersonTag ) )
				camera.RenderExcludeTags.Remove( firstPersonTag );
		}
	}
}
```

No configuration necessary, just make sure it's added to your Player Controller.  If someone knows a better way to do this, please let me know.

## Issue #2: The ViewModel has no arms/hands

The [docs](https://sbox.game/dev/doc/assets/ready-to-use-assets/first-person-weapons#how-to-use-our-weapons-arms) currently mention bone merging is a thing, but don't explain how to do it. 🤷

1. In our ViewModel prefab (v_usp), create an empty GameObject named "arms." Add the Model Renderer (Skinned) component to it.
2. Go to the Asset Browser -> Cloud -> models -> search for "ViewModel citizen arms". Click and drag it into the Model property on the new arms GameObject.
3. On the arms GameObject, set "Bones -> Bone Merge Target" to the Model Renderer on the root v_usp GameObject.

[![](https://cdn.sbox.game/upload/b/9acd1283/cf37/4d50/b5b1/1e4d915869f6.png)](https://cdn.sbox.game/upload/b/9acd1283/cf37/4d50/b5b1/1e4d915869f6.png)Now we have arms!  
[![](https://cdn.sbox.game/upload/b/13673265/f56f/40a2/b75e/3c0ec7e402bc.png)](https://cdn.sbox.game/upload/b/13673265/f56f/40a2/b75e/3c0ec7e402bc.png)

## Issue #3: The WorldModel isn't visible in third person

In the hierarchy panel, expand the "Player Controller" GameObject and click Body. Go to the Model Renderer (skinned) component and check the Bones / Create Bone Objects box.  
[![](https://cdn.sbox.game/upload/b/3e7df070/79bf/48e9/a1f5/eec6c9555918.png)](https://cdn.sbox.game/upload/b/3e7df070/79bf/48e9/a1f5/eec6c9555918.png)  
Now the gun appears properly, just in the wrong spot (you can press Escape -> click Eject, or press F8, to get a free camera while the game is running).[![](https://cdn.sbox.game/upload/b/09931f60/2163/4eb3/9d2a/b38a999d9950.png)](https://cdn.sbox.game/upload/b/09931f60/2163/4eb3/9d2a/b38a999d9950.png)This is because the game is placing the origin of the WeaponView at the hold_r bone

[![](https://cdn.sbox.game/upload/b/ec9e1aa0/974e/4361/9727/4b4b00993fc9.png)](https://cdn.sbox.game/upload/b/ec9e1aa0/974e/4361/9727/4b4b00993fc9.png)[![](https://cdn.sbox.game/upload/b/4e189f09/6eb2/4f6c/a3d8/c10e8a64457f.png)](https://cdn.sbox.game/upload/b/4e189f09/6eb2/4f6c/a3d8/c10e8a64457f.png)

We can move/scale the root GameObject in the WorldView prefab (w_usp) to improve this. I found a position of (2.5, 0, -2.5) is better, although I think this model is just too small for the Citizen's hands. This feels like a hack, someone let me know if there's a more correct way to do this.

## Issue #4: The back of the gun hits the near clipping plane when it reloads and disappears

Drop the Znear property on the Camera from 10 -> 7.  
[![](https://cdn.sbox.game/upload/b/56fc6052/f863/4409/9ffd/65c7d903e991.png)](https://cdn.sbox.game/upload/b/56fc6052/f863/4409/9ffd/65c7d903e991.png)

## Issue #5: There's no fire sound

We can fix this by filling in "Attack Sound" on weapon_usp (in the Weapon component, under the "Shooting" tab).[![](https://cdn.sbox.game/upload/b/e0925666/7340/41f3/adf2/fd03a28c487c.png)](https://cdn.sbox.game/upload/b/e0925666/7340/41f3/adf2/fd03a28c487c.png)

# All together now

*(Again, I'm using C to toggle first/third person and F8 to eject the camera to inspect the world model.)*Yay, it works! From here you can do all manner of customization by modifying the settings on BaseCombatWeapon (or creating a custom component that subclasses it for more advanced behavior).
