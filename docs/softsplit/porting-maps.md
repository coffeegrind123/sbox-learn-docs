---
title: Porting Source maps
slug: softsplit/porting-maps
url: https://sbox.game/learn/softsplit/porting-maps
author: Softsplit
author_slug: softsplit
topic: Capable
content_type: Text
tags: [hammer, mapping, porting, source]
rating: 3
views: 1070
upvotes: 3
downvotes: 0
updated: 'Updated

  18 Days Ago'
summary: Step-by-step guide on how to port maps from any Source engine game
scraped_at: '2026-06-08T11:00:46Z'
---

# Porting Source maps

> Step-by-step guide on how to port maps from any Source engine game

# Introduction

**IMPORTANT:**  
This guide relies on Hammer in s&box, which will be deprecated in favour of the new scene mapping tools. In the future, this will be rewritten. Please keep this in mind!

So, you have some old maps lying around from Garry's Mod and you wanna use them as a base to either iterate on or remake in the s&box engine. This guide will show you how I went about it when I was fixing up Big City.  
  
This is not a perfect one-click conversion. Treat the old map as a really strong blockout and asset reference. You can get the shape, scale, material names, prop placement, and a lot of the raw content across, but you should expect to rebuild lighting, clean up materials, replace broken entities, and do a proper art pass once the map is in s&box.

This guide is specifically about the Half-Life: Alyx Workshop Tools route. There are other Source 1 to Source 2 workflows floating around, but this is the one that matters here because the Alyx tools can open a Source 1 VMF directly and upconvert it into a Source 2 VMAP.

# Important context

Source and Source 2 content look similar from far away, but the actual file formats are different.

- Source maps use `.vmf`. Source 2 maps use `.vmap`.
- Source materials use .`vmt`. Source 2 materials use .`vmat`.
- Source models use `.mdl`. Source 2 models use `.vmdl`.

The Source 2 files you edit usually live in the content folder. The engine actually loads compiled versions from the game folder. For example, a material you edit as `.vmat` in `Half-Life Alyx/content` becomes a compiled `.vmat_c` in `Half-Life Alyx/game`. The same idea applies to maps, models, and other resources.  
  
For this guide, copy the editable Source 2 files out of the Alyx content folder when you move into s&box. Do not build the s&box project out of Alyx's compiled `_c` files.

# Prerequisites

You will need the following:

- The `.vmf` of your original map
- A copy of Half-Life: Alyx and the Workshop Tools installed
- The original Source content used by the map, if it had any custom assets
- A new or existing s&box project to copy the converted files into
- GCFScape, VPKEdit or another way to extract Source VPK content, if the map depends on packed game assets

If all you have is a `.bsp`, you will need to decompile it first. A decompiled `.vmf` is usually good enough as a starting point, but it will not be as clean as the author's original file. Expect weird brush cuts, lost entity data, broken visgroups, and some materials or models that need to be manually found later.

# Fix the VMF header first

The Alyx VMF importer expects header data that some decompilers, including BSPSource, do not always write correctly.  
  
Before importing, open the `.vmf` in the old Hammer editor for the game the map came from, then save it again. This is a boring step, but it matters. It can fix missing header data and clean up some decompiler leftovers before Source 2 ever sees the file.  
  
This is especially important for displacements. The importer can shred decompiled displacements pretty badly. Opening and saving the VMF in the right old Hammer version gives the importer a better chance of understanding them.

# Set up a Half-Life: Alyx addon

Open the Half-Life: Alyx Workshop Tools and create a blank addon with a name, e.g. `source1mod_imported`.  
  
You will usually be working with folders like these:

```
C:\Program Files (x86)\Steam\steamapps\common\Half-Life Alyx\content\hlvr_addons\source1mod_imported\
C:\Program Files (x86)\Steam\steamapps\common\Half-Life Alyx\game\hlvr_addons\source1mod_imported\
```

The content folder is where the editable Source 2 files live. The game folder is where compiled content and runtime content live.

# Set up Source content for the importer

Do not only give the importer converted Source 2 materials and models. The VMF importer still needs access to the original Source content because some information is lost during conversion, including important texture scaling data from VTF files.  
  
Create a Source mod folder in the Half-Life: Alyx game directory:

```
Half-Life Alyx/game/source1mod/
```

Put the original Source content in there using the same structure it had in the old game:

```
Half-Life Alyx/game/source1mod/gameinfo.txt
Half-Life Alyx/game/source1mod/materials/
Half-Life Alyx/game/source1mod/models/
Half-Life Alyx/game/source1mod/sound/
Half-Life Alyx/game/source1mod/scripts/
```

If the content is inside a Source `.vpk`, extract it first. Source 2 does not import directly from Source VPK files.  
  
You also need a matching folder on the content side for the VMF itself:

```
Half-Life Alyx/content/source1mod/maps/your_map.vmf
```

Putting the VMF here is important. It tells the Source 2 tools that the file is coming from a Source content root.

# Point Half-Life: Alyx at the Source content

Open the active Half-Life: Alyx `gameinfo.gi`. This is located at `Half-Life Alyx/game/hlvr/gameinfo.gi`.

Find the Source1Import block and point it at the source1mod folder with the following edits:

```
Source1Import
{
    "importmod"             "source1mod"
    "importdir"             "..\source1mod"

    "createStaticOverlays"  "1"
    "createPathParticleRopes"   "1"
}
```

# Clean the VMF before importing

Before importing, remove anything that is clearly not useful in s&box.  
  
Good things to remove or simplify:

- Old gameplay logic that only makes sense in Garry's Mod or Source
- Broken point entities from a decompile
- Unused brush entities, triggers, filters, and outputs
- Old cubemap entities, if you already know you are rebuilding probes later
- env sprites, old fog controllers, and post-processing entities you already know you will rebuild
- Props or overlays that reference content you do not have

Do not spend forever polishing the Source version. The goal is to reduce importer noise, not finish the map in the old tools.

# Import the VMF in Half-Life: Alyx Hammer

Open Half-Life: Alyx Hammer.  
  
Go to File > Open.  
  
In the bottom-right file type dropdown, select Source 1 Map Files (.vmf) instead of the normal Source 2 map type.  
  
Open the VMF from your Source content directory:

```
Half-Life Alyx/content/source1mod/maps/your_map.vmf
```

If the setup is correct, Hammer will upconvert the VMF into a Source 2 map. Entities that exist in Source 2 should come across. Other entities will be converted to new versions where the importer knows how. Source lights, for example, are usually converted into Source 2 lights.  
  
Save the result as a `.vmap` in your Alyx addon content folder, for example:

```
Half-Life Alyx/content/hlvr_addons/garrysmod_imported/maps/your_map.vmap
```

Compile or preview the map in Alyx before moving anything to s&box. This lets the tools generate resources and makes obvious import problems easier to find.

# Fix missing content in the Alyx stage

Check VConsole and Hammer's output for missing materials, missing models, and import errors.  
  
When something is missing, fix it in the Alyx conversion setup first. Do not immediately start patching the s&box project. The Alyx stage is your conversion workspace, so it is the best place to chase down old Source references.  
  
Common missing content causes:

- The map used assets from a Source game you did not extract
- The VMF references a material path that differs from the loose files you have
- A model exists, but its materials were not copied
- A VMT used proxies or shader parameters the converter does not understand
- The map depended on detail.vbsp, detail sprites, sound scripts, or other map-specific files

# Materials

Source materials do not become nice modern materials automatically. Tools like kristiker's source1import can get you a `.vmat`, but you should still inspect anything important.  
  
Keep the original `.vmt` and `.vtf` files available during VMF import. Even if you already made Source 2 materials, the VMF importer can still need Source material information for scaling and conversion.  
  
Source VMT keys that usually need human attention:

- `$basetexture`
- `$bumpmap`
- `$normalmapalphaenvmapmask`
- `$envmap`
- `$selfillum`
- `$translucent`
- `$alphatest`
- `$detail`
- `$surfaceprop`

The big thing is packed alpha. Source materials often hide useful masks in alpha channels. In s&box, do not blindly preserve that alpha in the color or normal texture. Work out what the VMT used it for, then split it into the right material input, such as transparency, self illumination, roughness, or another mask.  
  
For common old Valve materials, expect to rebuild roughness and metalness by hand or with simple generated masks. The converted material gets the map visible. The cleanup pass makes it look intentional.

# Models

Alyx has a built-in path for converting old `.mdl` files, but it is picky. Character models with flexes and flex rules usually need extra work and may require the original sources.  
  
To try a direct `.mdl` import, put the `.mdl` and its companion files in the same folder structure they had in Source. For example:

```
Half-Life Alyx/content/source1mod/models/humans/group01/male_07.mdl
```

Then create a `.vmdl` file next to it with a reference to the old model:

```
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->
{
    m_sMDLFilename = "models/humans/group01/male_07.mdl"
}
```

Open that `.vmdl` in the Source 2 tools and it should try to compile itself into a `.vmdl_c`.  
  
You still need `.vmat` materials in the matching material paths. If the old model used:

```
materials/models/humans/male/group01/citizen_sheet.vmt
```

then the Source 2 version should be:

```
materials/models/humans/male/group01/citizen_sheet.vmat
```

ModelDoc can also help clean up old converted models. Use File > Import > Import and Convert old .VMDL. It will process the old compiled model and write FBX files you can inspect or adjust. This is useful when a converted prop exists but needs cleanup before moving into s&box.

# 3D skyboxes

Source maps often use a 3D skybox at a different scale. The Source 2 importer tries to detect skybox geometry and split it into a separate 3D skybox map, but this usually only works well if the original skybox geometry was already in its own instance or prefab.  
  
If you open the imported map in Hammer and the 3D skybox is missing or appears merged into the main map, separate it manually.  
  
Find the 3D skybox geometry. It is usually in an enclosed box somewhere outside the playable area.  
  
Select the skybox geometry and any entities inside it.  
  
Press Ctrl+X.  
  
Create a new map with File > New.  
  
Save it with a clear name, such as `your_map_skybox.vmap`.  
  
Press Ctrl+Shift+V for Paste Special. Use Start at center of original, then confirm.  
  
Open Map > Map Properties in the skybox map and set Map Type to 3D Skybox.  
  
Go back to the main map and add a skybox_reference entity that references the `skybox.vmap`.  
  
Set the skybox_reference position to 0, 0, 0.  
  
Copy, do not move, the light_environment and env_sky entities into the skybox map too. The skybox needs its own lighting and sky to render correctly.

# Cubemaps and lightprobes

The importer may try to convert old cubemaps into Source 2's combined box-projected cubemap and lightprobe volumes. Treat the result as a first guess.  
  
For gameplay spaces, use a higher lightprobe voxel resolution so dynamic objects and players light correctly. For distant or inaccessible areas, lower resolution is usually fine.  
  
Avoid gaps between lightprobe volumes. Gaps can make players or dynamic props render black, fullbright, or just weirdly lit. Overlap is okay and is often necessary when using edge blending.  
  
Use priority when a smaller volume sits inside a larger one.  
  
For cubemaps, use Hammer's cubemap/reflection debug view to see how cubemaps affect surfaces.  
  
Cubemap edge blending is controlled with Edge Fade Dist values on X, Y, and Z. A value of 0 gives a hard edge. Higher values fade between volumes.  
  
Be careful with large edge blends and lots of overlapping cubemap volumes. The faded edge region has to sample multiple cubemaps and can get expensive fast.

# Lighting

Plan to relight the map.  
  
Imported lights are useful as reference points, but Source 2 and s&box lighting behave differently enough that old values rarely look finished. If you are importing through Half-Life: Alyx, you also need to think in terms of the newer lighting systems and VRAD3.  
  
Imported Source lights may have absurdly high ranges, sometimes in the tens of thousands. Source 2 uses the Range value during compile to decide what objects should be tested for each light, so oversized ranges can drastically increase compile times.  
  
Also watch lights using the stationary Direct Lighting type. Only 4 stationary direct lights can emit on a face before artifacts can start to happen.  
  
A practical order is:

- Set up the sky and environment lighting
- Fix the sun angle and brightness
- Fix obviously excessive light ranges
- Add major bounce or fill where the old map relied on Source lightmaps
- Rebuild practical lights: windows, lamps, signs, interiors
- Tune exposure and fog last

Do not chase final lighting while half the map still has broken materials. Bad materials will lie to you about lighting.

# Sounds and scripts

Source maps often reference `sound/`, `scripts/`, and soundscape data. s&box will not magically recreate every Source soundscape or entity-driven audio setup.  
  
Bring the raw audio over if you are allowed to use it, then rebuild the actual ambience in s&box. For looping city ambience, wind, hums, and room tones, it is usually faster to place clean sound emitters in the scene than to preserve old Source soundscape logic.

# Entities and gameplay

Most Source entity logic should be treated as reference, not final behavior.  
  
Things like doors, buttons, teleporters, triggers, scripted sequences, NPC spawns, and map-specific logic usually need to be rebuilt using s&box components or game code. Keep the imported entity positions if they are helpful, but do not expect the old I/O setup to behave the same way.

# Move the converted map into s&box

Once the `.vmap` opens in Alyx Hammer and the worst missing-content errors are handled, copy the editable converted Source 2 files into your s&box project's Assets folder.  
  
Copy from `Half-Life Alyx/content`, not `Half-Life Alyx/game`.  
  
Keep paths stable when you copy. If the converted map expects `materials/concrete/foo.vmat`, put the material at `Assets/materials/concrete/foo.vmat`. If you flatten folders or rename things early, you will create a pile of broken references for yourself.  
  
After copying, open the s&box editor and let the asset system scan and compile. Then open the `.vmap` from the Asset Browser.

# Create a scene

A `.vmap` is the map asset. In s&box you will usually also want a scene that loads it, especially if the map is part of a game or addon package.  
  
Create a scene, add a GameObject with the MapInstance component, and make sure the scene points at the copied `.vmap`.  
  
Once the scene loads, test it in-game as early as possible. You want to find scale, collision, lighting, and spawn issues before you spend time making the materials pretty.

# First cleanup pass in s&box

The first s&box pass is about making the map usable, not beautiful.  
  
Check these first:

- Collision on world geometry and converted props
- Missing materials
- Missing models
- Fullbright or blown-out lighting
- Water, glass, sprites, decals, and translucent materials
- Trigger volumes or brush entities that imported as dead geometry

If the map is huge, do this pass in sections. Big open maps like Big City are easier to fix if you pick one district or landmark, get it into a good state, then move outward.

# Troubleshooting

## **The VMF will not import**

Make sure the VMF was opened and saved in the old Hammer editor first. Make sure it is inside `Half-Life Alyx/content/source1mod/maps`. Make sure `gameinfo.gi` has the Source1Import block pointing at `Half-Life Alyx/game/source1mod`.

## **Everything has missing materials**

Check that the original `.vmt` and `.vtf` files exist in the Source mod folder and that the folder structure matches the material paths in the VMF.

## **Converted materials exist, but texture scale is wrong**

Make sure you gave the VMF importer access to the original Source content. The importer needs Source material and texture data; converted Source 2 materials alone are not enough.

## **Models are invisible or erroring**

Make sure the model and its materials were copied. A model can convert successfully while still pointing at missing materials. Check VConsole for the exact path it wants.

## **The map is black**

Add or fix environment lighting first. Then check whether the imported materials are valid. A black map is not always a lighting problem; broken shaders or missing textures can look the same at a glance.

## **Dynamic props or players are black**

Check lightprobe coverage. Look for gaps between volumes and use the lightprobe debug grid to confirm that the playable space is covered.

## **Compile times are terrible**

Check imported light ranges. Old lights can import with enormous ranges, and Source 2 uses range during compile to decide what each light can affect.

## **Collision feels wrong**

Check world collision separately from prop collision. Imported brushwork and imported models fail in different ways. If a model is the problem, open its `.vmdl` and simplify or rebuild the collision setup.

## **Water looks bad**

Rebuild it. Source water shaders do not translate cleanly to s&box materials. Keep the brush or plane placement as a reference and make a new water material that fits the scene.

## **Decals and overlays disappeared**

Make sure createStaticOverlays was enabled during import. Even then, expect to replace many old overlays, sprites, stains, and signs by hand.

# Summary

The short version is that you are using Half-Life: Alyx as the conversion bridge. Fix the VMF in the old Hammer first, give Alyx access to the original Source content through source1mod, open the VMF in Alyx Hammer as a Source 1 map, then save and clean the converted VMAP before copying the editable Source 2 assets into s&box.

Once the map is in s&box, treat it like a real s&box map instead of a finished port. Rebuild broken materials, check model collision, separate the 3D skybox, redo lighting and probes, replace Source entity logic, then test it in-game until the map feels intentional again.

Although it isn't a good example, you're free to use my existing Big City port as a reference which I have linked below:[![](https://opengraph.githubassets.com/83a012b2408b8c8d84083e5765baf5af110feb1bde0b5d7bb9a50c5a0cabde71/Softsplit/softsplit.big_city)

GitHub

GitHub - Softsplit/softsplit.big_city: gm_bigcity, ported to s&box.

gm_bigcity, ported to s&box. Contribute to Softsplit/softsplit.big_city development by creating an account on GitHub.](https://github.com/Softsplit/softsplit.big_city)  
Good luck, and happy mapping!

- Asphaltian
