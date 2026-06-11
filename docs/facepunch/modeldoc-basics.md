---
title: Intro to ModelDoc
slug: facepunch/modeldoc-basics
url: https://sbox.game/learn/facepunch/modeldoc-basics
author: Facepunch
author_slug: facepunch
difficulty: Beginner
topic: Editor
content_type: Text
tags: [3d, editor, intro, introduction]
rating: 0
views: 88
upvotes: 0
downvotes: 0
updated: 'Updated

  Yesterday'
summary: Import a 3D model and make your first .vmdl using ModelDoc
scraped_at: '2026-06-11T10:39:48Z'
---

# Intro to ModelDoc

> Import a 3D model and make your first .vmdl using ModelDoc

In this tutorial, we'll cover importing a 3D model for use in s&box using ModelDoc.

Start by ensuring you have a project open - if you don't know how to do this, check out this guide for [Creating your First Project](https://sbox.game/learn/facepunch/creating-first-project)

# Setup

## Importing a 3D model

All projects load data from their **Assets** folder, and it's up to you how you'd like to organize your file structure within that. [![](https://cdn.sbox.game/upload/b/8f960a18/b803/4a5b/b5bf/d8efe49ce6e0.png)](https://cdn.sbox.game/upload/b/8f960a18/b803/4a5b/b5bf/d8efe49ce6e0.png)

In this case, we'll go into the **Asset Browser** (or File Explorer) and add a **Models** folder for our model files to go into.  
  
Next, drag your modeland any associated texture files into the Asset Browser to import them into the project.

For 3D models we recommend either **.fbx or .obj** file formats  
For textures we support **.png, .jpeg** & **.tga** file formats

[![](https://cdn.sbox.game/upload/b/97e0ef65/09c4/40fb/af7b/dbf0b7a87003.png)](https://cdn.sbox.game/upload/b/97e0ef65/09c4/40fb/af7b/dbf0b7a87003.png)We're going to use this oil drum as an example - you can see all our image textures and our .fbx file.

## Creating a .vmdl

[![](https://cdn.sbox.game/upload/b/1d67a56f/245f/4814/9382/291cfba231d1.png)](https://cdn.sbox.game/upload/b/1d67a56f/245f/4814/9382/291cfba231d1.png)  
Now we can make our **.vmdl** - this stores all of the prop data to make it function.  
  
**Right-click on your imported 3d file > Create Model...** [![](https://cdn.sbox.game/upload/b/2d29e046/f092/4dbe/9351/0197c72fef6d.png)](https://cdn.sbox.game/upload/b/2d29e046/f092/4dbe/9351/0197c72fef6d.png)This will assign the model as the rendered mesh and set it's name to mirror that of the 3d file.  
[![](https://cdn.sbox.game/upload/b/cc1d9dcf/069e/46ae/aacc/ec2de49b23c7.png)](https://cdn.sbox.game/upload/b/cc1d9dcf/069e/46ae/aacc/ec2de49b23c7.png)You can see from the thumbnail, we're missing a material! So let's fix that real quick.

## Creating a .vmat

[![](https://cdn.sbox.game/upload/b/98bd9b45/fc0f/48f7/ade9/3c65a38b1324.png)](https://cdn.sbox.game/upload/b/98bd9b45/fc0f/48f7/ade9/3c65a38b1324.png)A **.vmat** is just a Material - you plug in your textures, choose a shader to render them and then you can assign the material to your models.   
  
Same as the .vmdl, you can right-click one of your textures and choose **Create Material**. [![](https://cdn.sbox.game/upload/b/6668ac45/1663/46e6/819b/69713239284a.png)](https://cdn.sbox.game/upload/b/6668ac45/1663/46e6/819b/69713239284a.png)We won't go into detail on the Material Editor, just double click the newly created material and make sure all of your textures are plugged into the correct inputs.

As mentioned under the **Naming Conventions** section, if your textures have the appropriate naming conventions, they will automatically be plugged into all relevant texture inputs after clicking Create Material. Neat! 

If your model has a metalness, emissive or tint mask, make sure to check those on the left column and plug those in as well. Enable **Specular** for proper light reflections.[![](https://cdn.sbox.game/upload/b/39ae4ce9/b339/4fee/b1ac/5047f5c04e4b.png)](https://cdn.sbox.game/upload/b/39ae4ce9/b339/4fee/b1ac/5047f5c04e4b.png)Now we can double-click the .vmdl we created before and take a look at ModelDoc!

# ModelDoc

[![](https://cdn.sbox.game/upload/b/816afe7a/fe77/4deb/8b35/b38a7a007ee1.png)](https://cdn.sbox.game/upload/b/816afe7a/fe77/4deb/8b35/b38a7a007ee1.png)Opening your model, you should see ModelDoc looking pretty close to the above.

If your 3d model includes level of detail meshes, they may have been automatically set up for you, but for tutorial purposes we'll start with a mostly clean .vmdl. 

## Interface

The main sections of the interface we'll worry about for this tutorial include the main **Viewport**, the **Node Editor** column to the left of that, and then the **Outliner** column to the very left of the screen. [![](https://cdn.sbox.game/upload/b/fcc2d31a/0613/4b8e/9716/db42a36286eb.png)](https://cdn.sbox.game/upload/b/fcc2d31a/0613/4b8e/9716/db42a36286eb.png)To add new Nodes, you can press either the blue +Add button and search, or you can right-click in an empty space within the Outliner and choose 'Add' from there. You can also right-click on the headers to get relevant node suggestions.

## Rendermesh

Selecting your .fbx under RenderMeshList in the Outliner will show you all the objects within your model, with tick boxes to control what is and isn't rendered. This is useful as we can use one .fbx to contain all of our LOD meshes, gibs and anything else we may want this asset to use. [![](https://cdn.sbox.game/upload/b/88ffb210/46ea/4126/8c5e/c7b918134507.png)](https://cdn.sbox.game/upload/b/88ffb210/46ea/4126/8c5e/c7b918134507.png)

Depending on your 3d package and export settings, you may need to mess with **Import Scale** and change the units to match your software, or export as the default for s&box which is Inches.

For the oil drum, I've selected just our LOD0 mesh and renamed this to LOD0 at the top.

## Material Groups

[![](https://cdn.sbox.game/upload/b/c9855e65/03cc/4fb1/bf40/d87bd1d92968.png)](https://cdn.sbox.game/upload/b/c9855e65/03cc/4fb1/bf40/d87bd1d92968.png)The **DefaultMaterialGroup** node exposes your models material slots. If your model has multiple material ID's, they'll be shown here, or you can tick the checkbox to override them and use a single material instead.  
  
**Skins**  
By adding more Material Group nodes, we can make it so the model can switch between materials in-editor. Right-click on the **MaterialGroupList** header and choose Add **MaterialGroup**[![](https://cdn.sbox.game/upload/b/fd358e17/7e35/40a7/bc12/11feb0002269.png)](https://cdn.sbox.game/upload/b/fd358e17/7e35/40a7/bc12/11feb0002269.png)

Making any changes to your .vmdl will require you to Recompile. Just hit the 'Needs Compiling' button when prompted.

For this oil drum example, we'll add an explosive barrel material as an optional skin. You can preview this in the viewport by switching material group just above the Node Editor window on the top bar.

[![](https://cdn.sbox.game/upload/b/496cd3a6/2b72/4cd9/ba11/25f8a0aabc6d.png)](https://cdn.sbox.game/upload/b/496cd3a6/2b72/4cd9/ba11/25f8a0aabc6d.png)

## Collision

**Primitives**  
The easiest and least expensive method of adding collision to our models is by using primitives. We can do this by right-clicking the Outliner, choosing Add and then choosing one of the following nodes:

- PhysicsShapeBox
- PhysicsShapeCapsule
- PhysicsShapeCylinder
- PhysicsShapeSphere

When added, you get a gizmo in the viewport that lets you move it into place. Press **Q** to get the transform handles and **T** for an XYZ gizmo. You can also type values in manually within the Node Editor window.  
  
You can also set the collisions **Surface Property**, which will determine the FX and sounds played when its walked on, hit, shot, etc. This setting will also determine the **Calculated Mass** of the collision mesh, which determines the final weight the object will be. We can override this later.[![](https://cdn.sbox.game/upload/b/c920f767/7931/41f2/952f/1495c53bf407.png)](https://cdn.sbox.game/upload/b/c920f767/7931/41f2/952f/1495c53bf407.png)A Cylinder physics shape is all we need in this oil drum example, but let's briefly look at the other most common methods of generating collision.  
  
**PhysicsHull**Hull collision can be made using both of these nodes:

- **PhysicsHullFromRender** - Directly references the visible geometry under RenderMeshList to generate a collision hull.
- **PhysicsHullFile** - Point towards a 3D model file to reference in order to generate a collision hull. Useful for if you make collision meshes manually in your 3D software.

These give additional options to refine the generated hull, like Face Merge Angle, Max Vertices Per Hull and the option to generate hulls per mesh or per element.  
  
Collision generated this way does not account for concave meshes like shown below. [![](https://cdn.sbox.game/upload/b/4329bef1/76e5/4c57/83ed/8b5343a3a72d.png)](https://cdn.sbox.game/upload/b/4329bef1/76e5/4c57/83ed/8b5343a3a72d.png)**PhysicsMesh**Similar nodes to PhysicsHull collisions - they can render concave, however they have no simulated physics capabilities, static only.

## Level Of Detail

[![](https://cdn.sbox.game/upload/b/977d5602/ca0a/45f3/98fc/3246b797d55d.png)](https://cdn.sbox.game/upload/b/977d5602/ca0a/45f3/98fc/3246b797d55d.png)Level of Detail meshes (LODs) are increasingly decimated versions of your model that load in as the object gets further from the camera.  
  
You can set this up two ways - use AutoLODs in ModelDoc to generate them automatically **OR** load in LODs from a 3d model file.  
  
**AutoLODs**We're going to tell ModelDoc to use our current LOD0 mesh to generate lower detail versions for use as LODs.[![](https://cdn.sbox.game/upload/b/9c238803/4832/45d4/87f9/eedb9fd01a35.png)](https://cdn.sbox.game/upload/b/9c238803/4832/45d4/87f9/eedb9fd01a35.png)First we'll right-click the Outliner and add a **LODGroup** node. Click 'Add Mesh' and assign our LOD0 rendermesh, then we can press **Auto Generate LODs**. This will populate the LODGroupList and give us finer control over the decimation process for each LOD step. [![](https://cdn.sbox.game/upload/b/ba026b88/75c0/4916/834d/01838f62a010.png "Hover over the sliders to see tooltips!")](https://cdn.sbox.game/upload/b/ba026b88/75c0/4916/834d/01838f62a010.png)You'll want to make sure the Switch Threshold is at the lowest value possible per LOD step to where the transition isn't visually obvious. You can preview the LODs in the Viewport properly by selecting **LOD: AutoLOD** on the top bar.  
  
And that's it!   
  
**Manual**LODs made by hand usually give the best results and offer the finest control, but they take time.[![](https://cdn.sbox.game/upload/b/cbcf4554/7760/483a/9019/d626f97e13b0.png)](https://cdn.sbox.game/upload/b/cbcf4554/7760/483a/9019/d626f97e13b0.png)First, we need to make a RenderMesh per LOD Level. We can take our **LOD0** RenderMesh from earlier and CTRL+D to duplicate it. We'll name each LOD appropriately and assign the corresponding meshes (**LOD1** uses **oil_drum_a_LOD1**, **LOD2** uses **oil_drum_a_LOD2**, and so on).  
  
Next we need to add LODGroup to our Outliner, then click 'Add Mesh' and assign our LOD0 rendermesh. Then select the LOD 0 node and CTRL + D to duplicate it until you have one for each one of your RenderMesh LODs, in our case, 5. Then we'll go through each one and make sure it's pointed to the correct LOD rendermesh (LOD 1 uses LOD1, you get the idea).

Then we'll assign a Switch Threshold for each of those - as a starting point, I like to use:[![](https://cdn.sbox.game/upload/b/a29836f6/d656/49d2/b0a1/869127c877c4.png)](https://cdn.sbox.game/upload/b/a29836f6/d656/49d2/b0a1/869127c877c4.png)You can preview the LODs in the Viewport properly by selecting **LOD: AutoLOD** on the top bar.  You should be able to zoom in and out in the viewport and it'll switch through the LODs.  
  
Your LODs are now set up and working!

An easier way to verify this is working is to click the monitor icon at the top of the viewport and tick 'Rendering Info' to display the mesh info.[![](https://cdn.sbox.game/upload/b/f2d0563a/52c2/4d6a/8230/071934848e9e.png)](https://cdn.sbox.game/upload/b/f2d0563a/52c2/4d6a/8230/071934848e9e.png)

## Markup

Markup nodes are used to overwrite mesh data with specific values.  
  
**PhysicsBodyMarkup**[![](https://cdn.sbox.game/upload/b/1b5739a7/5665/4d07/b236/80b23edbb04c.png)](https://cdn.sbox.game/upload/b/1b5739a7/5665/4d07/b236/80b23edbb04c.png)**Mass Override** (kg) is the most common value to change with this node. To ensure accurate physics when interacting with the model, it's good to use accurate weight values. Without this PhysicsBodyMarkup node, it will default to the sum of the **Calculated Mass** values of all active colliders in the .vmdl, which is usually way too high.

eg. our oil drum collider is calculated at nearly **750kg**, whereas a filled 55-gallon oil drum in real life is roughly 200kg, or 30kg empty. 

Options like Linear and Angular Damping are great when considering the shape and material an object is and how it will move when flung around.   
Higher linear damping will increase air drag, whereas higher angular damping reduces rotation velocity.  
  
Overriding Center of Mass can be useful for things like hammers where the head is significantly heavier than the handle, so the mass center is shifted higher up.

## Prop Data

Prop Data nodes are necessary for physics props that need to be explosive, flammable or breakable (has gibs). [![](https://cdn.sbox.game/upload/b/e43dc745/8093/4ad2/82c0/daa0d9e5299b.png)](https://cdn.sbox.game/upload/b/e43dc745/8093/4ad2/82c0/daa0d9e5299b.png)

# What We've Learnt

You should now be able to set up an asset in ModelDoc to include materials, LODs, collision, accurate mass and even gameplay properties!
