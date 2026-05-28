---
title: 'Bob’s Guides : S&box Custom Playermodel Guide [For your games!]'
slug: bobmac/sboxcustompmguide
url: https://sbox.game/learn/bobmac/sboxcustompmguide
author: Bobmac
author_slug: bobmac
difficulty: Beginner
topic: Modelling
content_type: Text
tags: [beginnerfriendly, custompm, easy, sboxpm]
rating: 4
views: 582
upvotes: 8
downvotes: 0
updated: Updated yesterday
summary: A guide for porting Custom models & S1 models into S&box as custom player
  models!
scraped_at: '2026-05-28T10:06:31Z'
---

# Bob’s Guides : S&box Custom Playermodel Guide [For your games!]

> A guide for porting Custom models & S1 models into S&box as custom player models!

# 🎩 Introduction

Welcome to the **S&box Model Port Guide**!.  
  
This guide is the second guide of my **”Bob’s Guides”** tutorial series and rewritten as an **“S&box Tutorial”!**

You can check out the Steam guide version **below.**  
[![](https://images.steamusercontent.com/ugc/14838972452876969380/48FC796DB6B0DEF7B564A2EA467D1E5021E7FE9D/?imw=5000&imh=5000&ima=fit&impolicy=Letterbox&imcolor=%23000000&letterbox=false)

steamcommunity.com

Steam Community :: Guide :: Bob’s Guides : S&box Custom Playermodel Guide [V1.31]

Welcome to the S&amp;box Model Port Guide !.
S&amp;box is based on heavily modified Source 2 which is newer and more complex than Source 1 .
In this guide, I’ll guide you through the proce](https://steamcommunity.com/sharedfiles/filedetails/?id=3665997623)I know you're here because you hate the sausage characters even I don't. So, this guide is for you. I'll be showing you how to port custom models into **S&box** for your own game. (Sandbox mode support isn't here yet.)

Anyway, You won't need to re-rig, retarget or do crazy stuff. No need to worry about using **Blender**. This guide is aimed from **Beginners**. And, We'll use an automated script for the main part which is very easy. *Thanks to* ***Noztik***. I’d say porting custom models into **S&box** is **100 times easier** than porting into **Garry’s Mod** or other Source 1 games.  
  
**Just to know, this workflow is very easy than it looks! Just follow the instructions carefully and you'll end up getting a working custom model!**[![](https://cdn.sbox.game/upload/b/f4d40936/7dc4/4852/a3dd/ca3e89d9f1a9.png)](https://cdn.sbox.game/upload/b/f4d40936/7dc4/4852/a3dd/ca3e89d9f1a9.png)“Do what you can, with what you have, where you are.”  
— **Theodore Roosevelt, 26th U.S. President**  
  
What are we waiting for? **Let’s get started!**────────────────────────────────────────────────────────────────────────

# ⚙️ Model Requirements [Read]

Alright. Before we start touching anything. We should know if our model is okay to port into **” S&box”**. There are no strict rules. Just to let you know what the engine supports and needs for our process.

**• Requirements**

Let’s start with the **"Requirements"** for your model. You should make sure that your model meets these requirements.

**➜ For model format**

- > You can use models in any format to import into **Blender**. But, we’ll go through **SMD**, **DMX (both from Source 1**), **FBX**, **PMX (From MMD)** and **VRM (from VRoid)** in this guide. There might also be **.blend** files in some models. You can open them inside **Blender** by dragging the **.blend** file into Blender.  
  >   
  > • **.unitypackage** files can be extracted to get FBX. This will be covered in the **"Import (FBX)"** section.  
  >   
  > • **MMD and VRM** models require additional Blender add-ons and a few extra steps.  
  >   
  > • Other formats such as **GLTF/GLB**, **DAE** are straightforward as **FBX**. So, I’ll skip them in the guide. You can find addons to import more complex formats that Blender doesn’t support.

**➜ For texture format**

- > Model’s textures can be **.PNG, .PSD, .JPEG, .TGA, .BMP, .JPG, .DDS.**  
  >   
  > • In some models, only **.PSD** is used. You can open/convert these using **GIMP**, Photoshop, or any image editing tool.

**➜ For your model**

- > Model must be rigged properly with a good rig.  
  > • It should have proper human bones set up. There can be extra spine bones in some models, such as **UE5 models**. You should use an add-on to merge them into **4 or 3 spine bones**. For custom models from **MMD, VRC, VRoid, and many more**. They only use **2 spine bones**. Don’t worry. The script can handle that.
- > Model shouldn't have more than **200K** of vertices/poly.  
  > • Can't confirm and still unknown, but mesh stretching occurs at a higher level. Same for bone count. Having a lot of bones doesn't seem to make problems tho. I don't really know the exact limit for **Source 2** yet..
- > Model's bones shouldn't have weird characters, symbols and foreign languages.  
  > • It's kinda weird but if you see them in your bones' names. either translate them or name it something better!.
- > There shouldn't be any bones before the **"Hips/Pelvis"** bone and it has to be the main root bone of your model before the spine bone.  
  > • The animations will have a laggy effect when switching animations if your model has bones before the **"Hips/Pelvis"** bone. Such as extra root bones. If there are any, remove them by deleting them in Blender in the upcoming sections when you import your model.  
  > • Or, if extra root bones functions as root bones while pelvis bone doesn't. S&box's animations won't work for those root bones which will result in stretching out for your model in-game/engine.
- > Fingers are **optional**.  
  > • The model can have fewer than 5 fingers or even none at all.

[![](https://cdn.sbox.game/upload/b/90997d1f/660b/4383/9c22/e243d3289688.png)](https://cdn.sbox.game/upload/b/90997d1f/660b/4383/9c22/e243d3289688.png)These are the basic requirements your model should have. You’re good to go if your model meets all of these!  
  
 ────────────────────────────────────────────────────────────────────────

# 🛠️ Required tools

We'll need these tools and software before start porting your model into **S&box**. Most of them are **Essential**. But some are **Optional**. Download them first, and we'll set them up in the next section. We'll also need to install add-ons to use in **Blender** to help with the processes of working with other model formats. But, only if you're working with those formats.

**• Blender & Addons**

- >  🟠**Blender**: Blender will be mainly used for this guide. No need to worry, we'll only use it for very easy steps. even beginners can do it.        
  > ➜ Steam Link: <https://store.steampowered.com/app/365670/Blender/>  
  > ➜ Official Link: <https://www.blender.org/>
- >  📙**Blender Source Tools (For Source 1 to S&box)**: A Blender add-on to import, export, and work with the **Source 1** formats. You only need it if you're going to port a model from **Source 1/Gmod** into **S&box**.  
  > ➜ **Link**: [http://steamreview.org/BlenderSourceTools/archives/](https://steamcommunity.com/linkfilter/?u=http%3A%2F%2Fsteamreview.org%2FBlenderSourceTools%2Farchives%2F)
- >  ⚙️**Blender VRM add-on (For VRM only)**: An addon to import the models in VRM format.  
  > ➜ **Link**: [https://extensions.blender.org/add-ons/vrm/](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fextensions.blender.org%2Fadd-ons%2Fvrm%2F)
- >  😺**Blender CATS add-on (Optional)**: An addon to import & fix MMD models, merge the same materials, and many more useful features. We'll be only using this addon for **MMD** models but there are many useful features in this addon. So, grab it if you want.  
  > ➜ **Link**: [https://github.com/teamneoneko/Cats-Blender-Plugin-Unofficial-](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2Fteamneoneko%2FCats-Blender-Plugin-Unofficial-)

[![](https://cdn.sbox.game/upload/b/6a37ca94/7a42/49a7/9aa4/71858367108b.png)](https://cdn.sbox.game/upload/b/6a37ca94/7a42/49a7/9aa4/71858367108b.png) **•** **Required Files**

- >  😎 **Custom Models 2 S&box**:  
  > ➜ **Link**: [https://github.com/BobmacU/CustomModel-2-Sbox](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2FBobmacU%2FCustomModel-2-Sbox)

**•** **Optionals**

- >  📚 **EasyExtractUnitypackage (For .Unitypackage only)**: An efficient tool that can extract .Unitypackage easily.  
  > ⇒ **Link**: [https://github.com/HakuSystems/EasyExtractUnitypackage](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2FHakuSystems%2FEasyExtractUnitypackage)
- >  🔑 **Shapekey+ (Optional)**: An add-on that makes working with shapekeys easier and better!  
  > ➜ **Link** : [https://github.com/MichaelGlenMontague/shape_keys_plus](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2FMichaelGlenMontague%2Fshape_keys_plus)
- >  🦴 **Bone merger (Optional)**: An add-on used to merge bones, also carries bone weights.  
  > ➜ **Link** : [https://github.com/vr-voyage/blender_bones_merger](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2Fvr-voyage%2Fblender_bones_merger)

────────────────────────────────────────────────────────────────────────

# 💻 Setting up

So.. I assume you have installed the required files. Let's start with installing the Blender addons.

**• Installing Blender Add-ons**

Alright, here's how to install Blender add-ons. Scroll down a bit if you know how to install add-ons. Nothing hard, **It's very easy.**  
  
First, open **Blender**. If you're opening it for the first time, a **"Quick Setup"** window will pop up. Set it up however you like—though I recommend **"Blender Dark"** to save your eyes lol. Then save it.  
  
Now press **"Ctrl + ,"** to open the Preferences window. Go to the **"Add-ons"** tab.  
Click the small arrow in the upper right corner and choose **"Install from Disk..."**  
Find your add-on ZIP file, select it, and click **"Install from Disk"**.  
Repeat the same for every add-on you want to install. [![](https://cdn.sbox.game/upload/b/a5cad9b2/0572/4b4d/b34c/6aa2ed31747d.gif)](https://cdn.sbox.game/upload/b/a5cad9b2/0572/4b4d/b34c/6aa2ed31747d.gif)That's all for installing the Blender add-ons. Let's continue.

**• Set up scene**

I know you've installed **Custom Models 2 S&box** file. Extract it, and you'll see four files. Which are.

- > **convert_playermodel.py** : Blender script we'll use for converting our custom model to S&box playermodel and export it as **FBX**.
- > **custommodel2s&box.blend** : Blender scene file to work inside. I've set up the scene to make your workflow easier.
- > **playermodel.vmdl** : Model file that stores the data of the model. If you're a modder from **Source 1**. You'll instantly familiar the name **MDL**. Except there's an extra **"V"** at the start for being **Source 2** format.
- > **playermodel.vanmgrph** : Animation file that stores animation of the model, including **Proportion Trick** set up. In **Source 1**. **MDL** does the job of storing animations, but in **Source 2**, this one took his work.

So, those four will do the work for you to convert your model. Open **Blender**. Drag and drop the **".blend"** file into Blender. or press **Ctrl + O**, browse to the scene file and open it. If you set the **".blend"** to always open with Blender. You just need to double-click the **.blend** file.[![](https://cdn.sbox.game/upload/b/d1bc3c19/2192/4534/8cae/c61ce0f103b7.png)](https://cdn.sbox.game/upload/b/d1bc3c19/2192/4534/8cae/c61ce0f103b7.png)When you're in. You'll see the texts saying this.[![](https://cdn.sbox.game/upload/b/74a052aa/eaf2/4aa7/b8ef/88ce060d098e.png)](https://cdn.sbox.game/upload/b/74a052aa/eaf2/4aa7/b8ef/88ce060d098e.png)Yes, let's do exactly what it says. I'm sure you see the folder icon in the top middle. Click it, browse to the script file in the **"scripts"** folder. Select a script depending on what model you're porting. **"Source 1"** script for models from Gmod or other Source 1 games. And, **"Manual"** for every other custom model.[![](https://cdn.sbox.game/upload/b/a825ac4c/a7f2/4e62/97de/abe7f941deff.png)](https://cdn.sbox.game/upload/b/a825ac4c/a7f2/4e62/97de/abe7f941deff.png)And that's it. You're done with this section! You'll be selecting one section from the next four to import your model into the scene.  
  
 ────────────────────────────────────────────────────────────────────────

# 📥 Importing - FBX

[![](https://cdn.sbox.game/upload/b/09354549/16c3/411a/96f9/421e5663c847.png)](https://cdn.sbox.game/upload/b/09354549/16c3/411a/96f9/421e5663c847.png)Ok, importing an **"FBX"** file into Blender is super easy. Let me show you how you can import **FBX** and **.Unitypackage**. Just to know, I copied almost everything from my last guide and rewrote some stuff.  
  
**• Importing FBX into Blender**

This is child's play, all you gotta do is: Click **"File"** in the top left corner and then hover your cursor on the **“Import”**, and you’ll see a bunch of options pop up beside it. Click **“FBX (.fbx)”** and browse to the location where your model’s FBX is located. Select it and click **”Import FBX”**[![](https://cdn.sbox.game/upload/b/ad2f54e7/65e8/4451/9ab4/f1c7ff36979c.gif)](https://cdn.sbox.game/upload/b/ad2f54e7/65e8/4451/9ab4/f1c7ff36979c.gif)Wait, and there you go!. You just successfully imported the model into the scene. That's all for importing the **FBX**. It's very easy, right? What about models that only come with **.unitypackage**, from **Unity**. I'll show you how. Skip if you don't have one.[![](https://cdn.sbox.game/upload/b/4934f51c/8936/40a1/a3f6/1767241a74c7.png)](https://cdn.sbox.game/upload/b/4934f51c/8936/40a1/a3f6/1767241a74c7.png)**• Extracting Unitypackage**[![](https://cdn.sbox.game/upload/b/f8908f8e/8c38/48f6/837f/f489341e4b92.png)](https://cdn.sbox.game/upload/b/f8908f8e/8c38/48f6/837f/f489341e4b92.png)I assume you already have the tool I linked above. Go get it if you haven't. Let's start. Firstly, you're going to open that tool. This is the **homepage**. Nothing special to see. But hey, it's a useful tool to extract **".Unitypackage"** files.[![](https://cdn.sbox.game/upload/b/43df8493/41e1/4099/94f2/6b8057ca3221.png)](https://cdn.sbox.game/upload/b/43df8493/41e1/4099/94f2/6b8057ca3221.png)Then, click **"Locate Unitypackage"**, browse for your file, select it, and hit **"Open"**. Now click **"Start extraction"** and wait — it’s usually quick (depends on your system). Once done, hit **"View extracted"**, then the button next to your package’s name, and choose **"Open (Selected) Directory"**. That’s where your extracted **".Unitypackage"** folder will be.[![](https://cdn.sbox.game/upload/b/84617bd3/b9ab/4e11/a83b/bc30d60ab7f4.gif)](https://cdn.sbox.game/upload/b/84617bd3/b9ab/4e11/a83b/bc30d60ab7f4.gif)Go inside, and you’ll see a bunch of folders. The **"FBX"** files are usually inside **"FBX"** or **"Models"** folders. Grab them and paste them into your main model folder (where the **.Unitypackage** is), or just make a new folder for them.  
  
But we’re not done yet — when you only have a **".Unitypackage"**, it often doesn’t include textures (in very rare cases). You’ll need to copy the textures as well, which are usually found in the **"Textures"** or **"Tex"** folder. If you don’t see those, check inside **"Materials"** — that’s where they sometimes hide.  
[![](https://cdn.sbox.game/upload/b/2087c7d4/1fb1/4452/8ba1/8e87e8ecd7ca.png)](https://cdn.sbox.game/upload/b/2087c7d4/1fb1/4452/8ba1/8e87e8ecd7ca.png)  
[![](https://cdn.sbox.game/upload/b/dd3cd474/1003/4db7/825e/53c521cede12.png)](https://cdn.sbox.game/upload/b/dd3cd474/1003/4db7/825e/53c521cede12.png)Alright, that's how you can extract Unity's package files. You'll have to use this tool every time you need to extract the package file that comes with the model files.  
  
────────────────────────────────────────────────────────────────────────

# 📥 Importing - Source 1

[![](https://cdn.sbox.game/upload/b/ecae84f5/2b31/45ab/abcc/6cb0799a8dfc.png)](https://cdn.sbox.game/upload/b/ecae84f5/2b31/45ab/abcc/6cb0799a8dfc.png)  
Alright, this is something new. We're going to import **Source 1** models into **S&box**. If you're going to port a model from the **Garry's Mod's workshop**. Make sure you have permission from the creator first. After that, you can download the addon as **GMA** file. Extract it using the good ol' [**Crowbar**](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2FZeqMacaw%2FCrowbar)[github.com] tool and then decompile the **MDL** file to get the model files, which are **SMD** that store the model.  
  
If you're going to port your own ported models or probably used my Gmod guide. I'm sure you have your own files. **SMD** or **DMX** files. Much better if you used **DMX**. Because it's supported natively in **Source 2**. And, I'm sure you know how to import them, too. But here for people who don't know.

**• Importing SMD & DMX**

Let's kick start with the **SMD**. Cuz' that's what you get from decompiling the **MDL** file. Make sure you have the [**Blender Source Tools**](https://steamcommunity.com/linkfilter/?u=http%3A%2F%2Fsteamreview.org%2FBlenderSourceTools%2F)[steamreview.org] installed. To import them. Click **"File"** from the top-left corner, then hover your cursor on the “Import”, and you’ll see a bunch of options pop up beside it. Click **Source Engine....**.  
  
A window will pop up. First thing you have to do is to browse to your **SMD/DMX** files. And then, select one of the files. And then, click the **Bone Append** dropdown. Select **Make New Armature**. Untick **Create collections** as it can cause errors. And click **Import....**.[![](https://cdn.sbox.game/upload/b/a5c8ccf5/7e78/44a2/8723/e0bf885b3116.gif)](https://cdn.sbox.game/upload/b/a5c8ccf5/7e78/44a2/8723/e0bf885b3116.gif)One of the meshes will be imported with an armature. We'll import the rest by doing the same steps again, but this time. Select all the other meshes except the **physics.smd**. We'll set **Validate Against Target** this time. So, our meshes will use the imported armature.[![](https://cdn.sbox.game/upload/b/d582afa4/12d6/495b/b5fb/1168e2de6117.png)](https://cdn.sbox.game/upload/b/d582afa4/12d6/495b/b5fb/1168e2de6117.png)For the **DMX** files. You're done with importing here. But for **SMD**. They store shapekeys in a separate file called **VTA**, which is a disadvantage of **SMD** over **DMX**. We'll handle that.

**• Importing VTA (Shapekeys)**

So, to import the **VTA** correctly. Select the mesh that the shapekeys belong to in Blender. Mostly, the head/face of the model. And then, import the **VTA** file with **Validate Against Target**.[![](https://cdn.sbox.game/upload/b/73d153f3/45a4/484d/90c6/b7d473774ebc.png)](https://cdn.sbox.game/upload/b/73d153f3/45a4/484d/90c6/b7d473774ebc.png)Wait a few seconds, and it'll be imported with an error, and it'll create a thing called **"VTA vertices"**. Ignore the error and delete the **VTA vertices**, and you're done with importing the Source 1 models into Blender.[![](https://cdn.sbox.game/upload/b/89d6465e/9b4f/45a4/8ba5/a7afd9e90fb0.png)](https://cdn.sbox.game/upload/b/89d6465e/9b4f/45a4/8ba5/a7afd9e90fb0.png)  
[![](https://cdn.sbox.game/upload/b/81da62f4/00d7/4478/b2fb/ee04b6e09141.png)](https://cdn.sbox.game/upload/b/81da62f4/00d7/4478/b2fb/ee04b6e09141.png)Last step, we'll only select our model, drag it, and drop it in the **"Input"** collection. So, the script can find your model inside there and work properly.  
  
────────────────────────────────────────────────────────────────────────

# 📥 Importing - MMD

[![](https://cdn.sbox.game/upload/b/cb5c2dcb/77e7/4fd4/ae27/195b2c6d1939.png)](https://cdn.sbox.game/upload/b/cb5c2dcb/77e7/4fd4/ae27/195b2c6d1939.png)Yeah, importing MMD models. It’s easy—only the fixing part can be a bit frustrating, but it’s mostly one-click stuff. Anyway, make sure you installed this [add-on](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2Fteamneoneko%2FCats-Blender-Plugin-Unofficial-%2Freleases%2F)[github.com]. That add-on helps you fix some issues and even assists in other situations. Don't worry. I'll guide you through.

**• Importing PMX**

Importing every model format is just child's play if you know how.  
Open **"Blender"**. *Yes, you're going to work inside Blender. That’s why I keep repeating this in every import section.*  
  
Press **"N"** on your keyboard. A panel will pop out from the right side. Click **"CATS"**, then **"Quick Access"**, and then click the small button beside "Import Model".A small panel will appear asking you to choose a model type... click "MMD". Ignore the others. and, Browse to your **".PMX"** file.[![](https://cdn.sbox.game/upload/b/94c094ed/5f2d/4b27/8331/1499a76c45d6.png)](https://cdn.sbox.game/upload/b/94c094ed/5f2d/4b27/8331/1499a76c45d6.png)Before you import, Set **"Internal Dictionary"** under the **"Rename Bones"** option if you don’t wanna deal with foreign language bone names :).  
Once that’s done, click "Import Model File".[![](https://cdn.sbox.game/upload/b/b23ce81a/cc82/4d8a/8fa7/59b06b4119de.gif)](https://cdn.sbox.game/upload/b/b23ce81a/cc82/4d8a/8fa7/59b06b4119de.gif)  
Your model will be imported. Now let’s clean + fix it using the add-on we installed.  
It’s a one-click fix—no stress, no complicated steps.

**• Fixing the model**[![](https://cdn.sbox.game/upload/b/b2393963/0b55/463b/bdad/7385ceba9abe.png)](https://cdn.sbox.game/upload/b/b2393963/0b55/463b/bdad/7385ceba9abe.png)Alright, let’s start fixing the model. It’s super easy.  
First, Zoom in till you can see your model, and then we need to make the model a **"Single User"**. No clue what it does exactly, but it’s required before the fix by default.  
  
To do that, press **"A"** on your keyboard to select everything.  
Then press **"F3"**, type **"Make Single User"**, and click on **"Make Single User ‣ Object & Data"**.[![](https://cdn.sbox.game/upload/b/e98529c0/0e24/4220/ba88/0dcd2eb2ba58.gif)](https://cdn.sbox.game/upload/b/e98529c0/0e24/4220/ba88/0dcd2eb2ba58.gif)

Now, we’ll fix the model. In the **"CATS"** panel, you'll see **"MMD Options"**.  
Click the dropdown. There it is—**"Fix MMD Model"** button!. Press **A** to select everything before clicking that and then click that **"Fix MMD Model"**.  
  
A warning will pop up—click "OK". It just says to only use this on MMD models. You'll have to wait a bit until it's done.[![](https://cdn.sbox.game/upload/b/be9e89fc/b171/4f6f/8fb1/afd4e9309d04.gif)](https://cdn.sbox.game/upload/b/be9e89fc/b171/4f6f/8fb1/afd4e9309d04.gif)So, what does it fix? It’ll **reparent some bones**, **remove unnecessary bones**, **translate and rename bones**, **merge some weights**, **correct the hips bone**, **convert morphs into shapekeys**, and more.  
  
And that’s it. **Your model is now fixed and ready.**[![](https://cdn.sbox.game/upload/b/b80e3106/ad9e/4eec/a6d2/671e0f1b9d76.png)](https://cdn.sbox.game/upload/b/b80e3106/ad9e/4eec/a6d2/671e0f1b9d76.png)────────────────────────────────────────────────────────────────────────

# 📥 Importing - VRM

[![](https://cdn.sbox.game/upload/b/a0095d74/7922/4b92/9a4a/6ba3f63cf869.png)](https://cdn.sbox.game/upload/b/a0095d74/7922/4b92/9a4a/6ba3f63cf869.png)Importing **VRM** models is pretty straightforward too. The only thing you'll need is the "Blender VRM add-on" here!. So, make sure you have already installed the [add-on](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fextensions.blender.org%2Fadd-ons%2Fvrm%2F). So, let's start.

**• Importing VRM**

This part is just as easy as importing an FBX as it is. Open **Blender**, click **File** on the top-left corner, hover over **Import**, and you’ll see a list of options.  
  
If you’ve installed the VRM add-on, you’ll see **VRM (.vrm)** and **VRMA (.vrma)**. Click **VRM (.vrm)**, then browse to your model’s **.VRM** file, select it, tick ✓ "Extract texture images into the folder", and hit **Open**.  
  
After import, the textures will show up inside your model’s folder. Keep in mind: extracting textures takes a bit longer. Skip it if your model already includes textures.[![](https://cdn.sbox.game/upload/b/aadac4de/0d46/4f4f/821f/6d45966c5d05.gif)](https://cdn.sbox.game/upload/b/aadac4de/0d46/4f4f/821f/6d45966c5d05.gif)After importing the model, you're going to see messy stuff. mostly, **"Colliders"**.. They might be useful in **"VRoid"**. But again, **not in S&box :)**. Maybe if someone made a direct VRM import addon for S&box, as it's a game engine.  
  
Anyway, to remove them, right-click the collection with a white box icon named **"Colliders"** and then click **"Delete Hierarchy"**. And you might want to hide the armature to get a better view of your model in Blender. Just click the eye icon beside the camera icon of your model's armature.[![](https://cdn.sbox.game/upload/b/f6254572/526c/41f9/a848/b3405a5abd2f.gif)](https://cdn.sbox.game/upload/b/f6254572/526c/41f9/a848/b3405a5abd2f.gif)There we go, now. I can see the model in clear view. *cough..* ***Lads, I don't like Vtubers. My friend gave me this VRM model for the tutorial 💀***... Okay, so. This is how we import **VRM**.[![](https://cdn.sbox.game/upload/b/f94bf8b7/22b8/4ff3/9920/43e558ea0222.png)](https://cdn.sbox.game/upload/b/f94bf8b7/22b8/4ff3/9920/43e558ea0222.png)────────────────────────────────────────────────────────────────────────

# 📏 Scaling

Good work, now we can continue to use the script. But we will have to scale up/down our model to match the armature we have in the scene file. But, how much? It's very easy. The scale may be different depending on the model type. It seems like **MMD** and **VRM** models have the same scale. I'm not sure if it depends on the model author. **FBX** doesn't have a fixed scale. So, it can be random. For **Source 1** formats. It'll be very huge compared to the reference armature given in the scene. **But our goal is the same.**

**• Scaling the model**

First, we'll only select our imported model's armature and its meshes. We'll see the differences between scaling for each format below. But, before that. I'll explain what we'll do. We'll scale down our model by selecting the model and its armature. Press **"S"** and move the cursor up/down depending on what we'll do. We can hold **Shift** while scaling for more precise scaling!  
  
For **Source 1**. We'll scale the model down as it's very huge compared to the reference armature. For the others, it depends on your model's size. Most of the time, the model will be perfectly fitted or shorter.  
  
So, when we scale. We will keep our eyes on the **shoulder/clavicle** bones of the reference armature, and we'll scale down our model until our model's shoulder/clavicle is fitted to the reference armature shoulder/clavicle bone in the middle. Just like humans' bones are in the middle.[![](https://cdn.sbox.game/upload/b/b7e48a8f/e7f6/489d/a289/12935c1ece14.png)](https://cdn.sbox.game/upload/b/b7e48a8f/e7f6/489d/a289/12935c1ece14.png)Just like this. After it's fitted. We'll press **"Ctrl + A"** and click **"All transforms"**. So, the scale will be applied. **Now, have a look!**.

**• Source 1 model**[![](https://cdn.sbox.game/upload/b/ca986b11/1b70/4586/8f6e/20c2470d13c9.gif)](https://cdn.sbox.game/upload/b/ca986b11/1b70/4586/8f6e/20c2470d13c9.gif)  
As you can see, I scaled the model down until the model's shoulder is fitted with the reference's shoulder bones in the middle. Let's see how we can do for the other ones.

**• Other models**[![](https://cdn.sbox.game/upload/b/d4fef895/0404/458a/8981/0f0d379c0026.gif)](https://cdn.sbox.game/upload/b/d4fef895/0404/458a/8981/0f0d379c0026.gif)For this **VRM** model. I only had to scale up a little bit to fit the shoulder in the middle. So, I hope you get the concept of what you're going to do. But what about very small models?  
  
**• Very small models**[![](https://cdn.sbox.game/upload/b/e126ce69/fc34/44bb/924f/998c94198af1.png)](https://cdn.sbox.game/upload/b/e126ce69/fc34/44bb/924f/998c94198af1.png)For very small models like this one. Just scale it up until it matches. We'll handle the size problem in the **ModelDoc** later.  
  
So, that's all for scaling the model. We'll proceed to the next section :)  
  
────────────────────────────────────────────────────────────────────────

# 🔤 Bone Rename

Just like good ol' **Source 1**. We'll have to rename the bones in the script to make the script work properly with our custom model's bones. For **Source 1** models, you can just skip this section, as you might've already loaded the **Source 1** version of the script. Which already has the correct bone mapping for your model.

**• Bone mapping**

For other models, scroll down to **line 48**. You'll see a bone mapping table for renaming your model. Let's start with the **"Core"** bones. We have **seven** bones for that. But, only five if you don't want the moving eyes.  
  
So, I already mapped a set of bone names to get you what bones you're going to find. Click the small arrow beside your model's armature. Find the **"Hips"** bone and then keep expanding it by clicking the small arrow beside it, and you'll see more bones. Find five bones which are **Hips, Spine, Chest, Neck, and Head** bones. Names may be different, but there are always the names of core bones at the end of the bone. **See below.**[![](https://cdn.sbox.game/upload/b/d180d818/371e/4f4e/9f01/43eeef21d3d1.png)](https://cdn.sbox.game/upload/b/d180d818/371e/4f4e/9f01/43eeef21d3d1.png)

So, I got **six core bones** instead of five because my model has three spine bones. It's better. Most of the models these days only have two spine bones. But we can still use the script, as the script will handle the third one even if your model doesn't have three spine bones.  
  
By default, **spine_2** one will be commented out. If your model has three spine bones. Remove the hash (#). To set our model's bones in the script. Double-click the bone name in the outliner and press **"Ctrl + C"** and then paste it in the correct place inside the script.[![](https://cdn.sbox.game/upload/b/d97f0f61/1fcd/4d7f/a9cc/a9331abf7626.gif)](https://cdn.sbox.game/upload/b/d97f0f61/1fcd/4d7f/a9cc/a9331abf7626.gif)  
[![](https://cdn.sbox.game/upload/b/6a2030ba/bd10/4562/8ccb/f8fdf3f6eee8.png)](https://cdn.sbox.game/upload/b/6a2030ba/bd10/4562/8ccb/f8fdf3f6eee8.png)Repeat the same for every core bone like that. After that, you'll see two eye bones. It's commented out because not every models has eye bones. If you found eye bones in your model. You can have your model's eyes animated, but you will need extra work later for that.  
  
If you want. Remove the hashes (#) from the eye bone lines, copy the eye bones' names from your model, and paste them in the correct place in the script. and then go to **line 38** and edit **"false"** to **"true"**. So, the script will handle the eye bones.

[![](https://cdn.sbox.game/upload/b/9b8e29f0/1bb7/4ac5/a2df/19130236fe51.png)](https://cdn.sbox.game/upload/b/9b8e29f0/1bb7/4ac5/a2df/19130236fe51.png)

[![](https://cdn.sbox.game/upload/b/e33e1da2/5575/4308/a2b3/f960f79c02e0.png)](https://cdn.sbox.game/upload/b/e33e1da2/5575/4308/a2b3/f960f79c02e0.png)And then, we'll go for the **"Left arm/Right arm"** bones. For those bones, find the **shoulder/clavicle** bone in the outliner first. and then expand the bone structure until you find the finger bones. Here's what I need to find for my model. Names might be tricky, but no. It's actually not. **Ignore the twist, helper, and extra bones!**[![](https://cdn.sbox.game/upload/b/ad8749e7/7fbe/446d/885d/da4ca3fad3a2.png)](https://cdn.sbox.game/upload/b/ad8749e7/7fbe/446d/885d/da4ca3fad3a2.png)  
[![](https://cdn.sbox.game/upload/b/70a37fd0/9f47/4b48/9ac7/085e0a349e78.png)](https://cdn.sbox.game/upload/b/70a37fd0/9f47/4b48/9ac7/085e0a349e78.png)Just like before. We'll put them in the proper places inside the script like that. Do the same for the **Right arm**. If your model has **"meta"** bones in fingers. You'll also need to map them in the script. They're located at **line 81** for the left side and at **line 109** for the right side. They'll be commented out by default. Remove the hashes if you're going to use them and map your meta bones there.  
[![](https://cdn.sbox.game/upload/b/7f74c4f2/f2fb/4a4d/b130/0fd759549bbe.png)](https://cdn.sbox.game/upload/b/7f74c4f2/f2fb/4a4d/b130/0fd759549bbe.png)After that, scroll down in the script, and you'll see **"Left leg/Right leg"**. Only four bones are in this section. You're going to find the **"Upperleg/Thigh"** bone in the outliner and then expand it until you find the toe bone. Ignore the twist, helper, and extra bones.  
[![](https://cdn.sbox.game/upload/b/ab8815bd/7182/453f/8d8b/c179166865c4.png)](https://cdn.sbox.game/upload/b/ab8815bd/7182/453f/8d8b/c179166865c4.png)  
[![](https://cdn.sbox.game/upload/b/fbfcf8e8/8ca2/4dd6/91ee/bd1a2e500d27.png)](https://cdn.sbox.game/upload/b/fbfcf8e8/8ca2/4dd6/91ee/bd1a2e500d27.png)We're done with setting up bone names for the script. Please proceed to the next section. **Will ya?**  
────────────────────────────────────────────────────────────────────────

# 😶 Shapekeys

Unlike my Gmod one, we won't talk much about shapekeys, as **S&box** seems to have a very high shapekey/morph limit. I don't know the exact limit. But I recommend keeping it under **700**. You shouldn’t worry about this unless your model is a very customizable model with hundreds of shapekeys..  
  
Anyway, we should check some stuff about shapekeys before getting our model into **ModelDoc**. It seems to be more strict than the **StudioMDL** from **Source 1**. It doesn't allow special symbols in the shapekey names and seems to break the shapekey/morph with spaces in the name. So, we have to do some preparation for that.  
  
**• Renaming Shapekeys**  
  
This is very simple. First, you will have to click the **"Data"** tab with a green triangle. Scroll down a bit, and you'll see your model's shapekeys there.[![](https://cdn.sbox.game/upload/b/5a5e970e/1655/4243/a329/bcafb78a22ac.png)](https://cdn.sbox.game/upload/b/5a5e970e/1655/4243/a329/bcafb78a22ac.png)And then, you're going to remove **spaces** & special characters from the names. Double-click the shapekey's name and then replace spaces with **underscores( _ )**. And, just give a name for the special character ones. Example as **Mouth ω**. I'll just rename it to **Mouth_Cat** for that.[![](https://cdn.sbox.game/upload/b/7c2ffeac/29bd/410d/abf3/60fcd4875106.png)](https://cdn.sbox.game/upload/b/7c2ffeac/29bd/410d/abf3/60fcd4875106.png)  
[![](https://cdn.sbox.game/upload/b/28bfa5f1/890f/4bd6/8843/e28fdc5f1139.png)](https://cdn.sbox.game/upload/b/28bfa5f1/890f/4bd6/8843/e28fdc5f1139.png)Here's how I do. It's kinda funny, but I'm going to hate **ModelDoc** a lot for that. Keep doing that for all shapekeys until all of them are renamed properly. That's all for this section. There's nothing special for this section.  
────────────────────────────────────────────────────────────────────────

# 📜 Convert script

This section will be very short. I just want you to double-check the bone names, the size scale, and the shapekey names if everything is okay. Having a typo in the bone name mapping will destroy the pose! So, make sure you double-check :)  
  
We'll save the file as a backup before running the script. Press **Ctrl + Alt + S** to save the file as **incremental**. So, it won't overwrite the original scene file. After that, let's run the script.

**• Running the script**

It's very simple. Click the **"▶"** at the top to run the script or you can hover your cursor into the scripting tab and press **"Alt + P**.[![](https://cdn.sbox.game/upload/b/ee4cacbd/d84b/4705/a7c7/32efd978d041.png)](https://cdn.sbox.game/upload/b/ee4cacbd/d84b/4705/a7c7/32efd978d041.png)Wait a bit, and it'll do everything to make the model compatible with **S&box** citizen's rig. Here's what it does.

- > Get the armatures and meshes from the Input collection
- > Handle the different number of possible spine bones
- > Rename the input armature's bones and vertex groups to Human Citizen bones and vertex groups
- > Create metacarpal bones in the input armature
- > Create missing joint helper bones in the input armature
- > Create twist bones in arms and legs in the input armature
- > Create any missing bones in the Human Citizen armature
- > Move the Human Citizen armature's bones to match the Input armature in edit mode
- > Move the Input meshes to the Human Citizen armature
- > Weight paint the metacarpals in the Human Citizen armature
- > Pose the Human Citizen armature to match the reference armature shape
- > Realign miscellaneous bones in the Human Citizen armature
- > Export the Human Citizen armature and meshes
- > Cleanup

[![](https://cdn.sbox.game/upload/b/989c8643/cc5f/4a0d/8ecb/c9f19761641f.png)](https://cdn.sbox.game/upload/b/989c8643/cc5f/4a0d/8ecb/c9f19761641f.png)Yes, it'll pose your model into A-pose after the process because the reference armature is posed in A-pose.  
As you can see, my model is now ready and compatible with **S&box** armature.  
That's all. and it'll export a **FBX** file into the file where the script file is located. We're done with the **Phase 1**, where we prepare our model.

**• Fixing the head pose [Optional]**

But, sometimes. your model's head might be a little bit off. We can fix it easily by using [**this addon**](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2Fteamneoneko%2FCats-Blender-Plugin-Unofficial-)**.** Install it. As I said above. This addon has many useful features including applying pose without having to do many crazy stuff.  
  
So, as you can see here. We have a problem like this and I'll show you how to fix it.[![](https://cdn.sbox.game/upload/b/e546e283/d875/437b/9ca9/0c11b14d2d66.png)](https://cdn.sbox.game/upload/b/e546e283/d875/437b/9ca9/0c11b14d2d66.png)We will need a better view. Press **"Num 3"** from your keyboard's numpad. It'll rotate your camera to a viewpoint where you can see the neck bone clearly to pose it correctly. So, First step is to select the model's head bone. Press **"Ctrl + Tab"** to switch to **"Pose Mode"**. And then, rotate it until it looks okay.[![](https://cdn.sbox.game/upload/b/4076f5d5/1d2d/4183/a25c/c41c945c187c.png)](https://cdn.sbox.game/upload/b/4076f5d5/1d2d/4183/a25c/c41c945c187c.png)After that, Click the **"CATS"** from the sidebar. Make sure you installed and enabled the addon!  
And there'll be many categories. But, the one we'll use is very obvious. It's in **"Pose Mode"**. You can see a button called **"Apply as Rest Pose"**.[![](https://cdn.sbox.game/upload/b/7f56e61b/e2b2/4f18/8664/f94d1094ab92.png)](https://cdn.sbox.game/upload/b/7f56e61b/e2b2/4f18/8664/f94d1094ab92.png)Click it and you're done. It'll apply the armature pose we just posed without having to do the tedious process where you have to apply armature modifiers first, Apply the pose and re-add armature modifiers.

And then, you'll have to export your model as **FBX** in a correct settings. What you have to do is click **"Files"** and then hover on **"Export"** and then click **"FBX (.fbx)"**.[![](https://cdn.sbox.game/upload/b/821ea927/e2e0/4351/be6c/9592a448ccdc.png)](https://cdn.sbox.game/upload/b/821ea927/e2e0/4351/be6c/9592a448ccdc.png)When export window pops up. Look to the right where the settings for your export are located. You'll have to adjust some settings. Firstly, click the **"Armature"** and then you'll see armature settings. Click **"Primary Bone Axis"** and set it to **"X"** from **"Y"**. And then, click **"Secondary Bone Axis"** to **"Z"** from **"X"**. Lastly, untick **"Add leaf bones"** to avoid adding extra end bones. Here's the correct settings you should see.[![](https://cdn.sbox.game/upload/b/21daaf15/e1b1/4978/bd86/a695b43ce49e.png)](https://cdn.sbox.game/upload/b/21daaf15/e1b1/4978/bd86/a695b43ce49e.png)After that, you might want to save it as a preset. So, you don't have to redo the thing when you export another model. Scroll up in the settings. You'll see two small buttons beside **"Operator Presets"**. Click the plus button. Give it a name and then click **"OK"**.[![](https://cdn.sbox.game/upload/b/cdf4241d/b0b1/4100/985c/0b49fc1d942b.png)](https://cdn.sbox.game/upload/b/cdf4241d/b0b1/4100/985c/0b49fc1d942b.png)And then select the path into the same folder where your firstly exported **"FBX"** is located. Remember that the convert script does the export automatically when you run it. You're going to overwrite the exported one with your current fixed one. And then, click **"Export FBX"**.[![](https://cdn.sbox.game/upload/b/314d008b/3562/4fab/8d6f/b565e2af4cb8.png)](https://cdn.sbox.game/upload/b/314d008b/3562/4fab/8d6f/b565e2af4cb8.png)That'd be all for this section and **phase 1**.[![](https://cdn.sbox.game/upload/b/cbdd0dc4/e53e/4a2d/b2f3/10095f684009.png)](https://cdn.sbox.game/upload/b/cbdd0dc4/e53e/4a2d/b2f3/10095f684009.png)────────────────────────────────────────────────────────────────────────  
────────────────────────────────────────────────────────────────────────

# 📑 ModelDoc Setup

Welcome from **Phase 2**. We'll be going to import our model. So, open **"S&box editor"** and open a project or create one if you want to work on a fresh project. I'll work on my own one. We'll wait until the project is launched.  
  
When you're in, click **"Assets** folder from the **"Asset browser"**. and then, click **"New"**. click **"Folder"**. Name it **"models"**. And, create another folder and name it whatever you like for your model folder. I'll just name it **"Tutorial Model"** for my model's folder.[![](https://cdn.sbox.game/upload/b/d9ad8b4c/e638/4093/afab/398ae0d4dbdf.png)](https://cdn.sbox.game/upload/b/d9ad8b4c/e638/4093/afab/398ae0d4dbdf.png)Alright, after that, we'll return to the folder where our custom model's **FBX** file is located. When you're in. Rename the **FBX**, **VMDL**, and **Vanmgrph** to your model's name or anything you want. I'll just name it **"My playermodel"**.  [![](https://cdn.sbox.game/upload/b/e22364fc/02f0/4220/98e0/4969a05f3824.png)](https://cdn.sbox.game/upload/b/e22364fc/02f0/4220/98e0/4969a05f3824.png)And then, go back to the editor. Click the file path box, and then it'll select the entire path to your model folder. Press **"Ctrl + C"** and open another file explorer. Paste the path in the path box, and it'll open the model folder in your file explorer. Copy your **FBX**, **VMDL**, **Vanmgrph** files into that folder. Don't cut them. especially the **VMDL** and **Vanmgrph**. They serve as base files for your model. So, you can use them when you port more models.

[![](https://cdn.sbox.game/upload/b/f3594362/ae63/4d95/9d2d/d5db784e9c8c.png)](https://cdn.sbox.game/upload/b/f3594362/ae63/4d95/9d2d/d5db784e9c8c.png)[![](https://cdn.sbox.game/upload/b/1873e86c/5bdc/4379/80e3/fdfcbbff7135.png)](https://cdn.sbox.game/upload/b/1873e86c/5bdc/4379/80e3/fdfcbbff7135.png)

After that, you'll see your model files in the editor. What you have to do is open the **VMDL** by clicking it. And **ModelDoc** will open. In this guide, I won't be teaching you to use the **ModelDoc** until I master it myself, and the tool is most likely going to be replaced sooner. But I'll give you a quick rundown to get you comfortable with the tool.[![](https://cdn.sbox.game/upload/b/7c3c459f/cdce/4181/bdb0/f33bca5f848b.png)](https://cdn.sbox.game/upload/b/7c3c459f/cdce/4181/bdb0/f33bca5f848b.png)

> Red area : Where you can see and select to edit the nodes of the model.  
> - If you're a modder from **Source 1**. Just think of it like **QC commands**. We use nodes in S2 instead of writing commands.  
>   
> Blue area : Where you can add nodes for your model.  
> - For this one. I recommend that you click each node and read what it does. You can click the **"Star"** for quick access to the most used nodes.  
>   
> Yellow area ; Where you can edit the nodes.  
> - When you select one node from the outliner. You'll be able to edit the node's properties there by adjusting, providing files, and more.  
>   
> Green area : Where you can edit **"View Settings**, **Lighting Mode**, **Visualization Mode**, **HUD settings**, **Mesh Display**, **Component Display** and more..  
> - Just mess around with it if needed. It's just for the viewport anyway.  
>   
> Purple area : Where you can preview your model, and is also called **"Viewport"**.  
> - Hold **"RMB"** while your cursor is in the viewport to move around. And, you can also hold **"Ctrl + RMB"** to rotate the model when you want to preview the lighting from different angles.  
>   
> Orange area : Where you can see your compiled model's bones, meshes, and more listed in there.  
> - Nothing special.  
>   
> Cyan area : Where you can control animations, morphs, and more.  
> - You will need to pull the edge of that window to see the full view of the area. When you wanna preview the morphs. Click **"Enable Manual Slider Control"**, and you'll be able to edit and preview your shapekeys.

Anyway, we're done with the quick rundown. Let's continue. First thing you have to do is click the small blue sheet icon under **"RenderMeshList"**. And there'll be many properties, but you'll see **"Source File"**. Click the small magnifying glass icon to open the local browser. Browse into the **"models"** folder and your model's folder, and then open your model's **FBX** file.[![](https://cdn.sbox.game/upload/b/9a739e31/e7b8/4d26/b64c/972fbc5570eb.png)](https://cdn.sbox.game/upload/b/9a739e31/e7b8/4d26/b64c/972fbc5570eb.png)Your model will show up without any textures. We got red missing textures in S2. And then, if you look a little bit lower. You'll see **"proportion_trick"** in the **"AnimationList"**. Click it and open your model's FBX there by doing the same thing you did to import your model's FBX.[![](https://cdn.sbox.game/upload/b/d1070b25/b896/4023/9ef6/ee390514e075.png)](https://cdn.sbox.game/upload/b/d1070b25/b896/4023/9ef6/ee390514e075.png)One last thing, if you look up. You'll see **"Graph"** with a **"Vanmgrph"** imported. But we'll have to import ours there. Click the small magnifying glass icon below the box and then open the **"Vanmgrph"** file of your model or the model won't have any playermodel animations![![](https://cdn.sbox.game/upload/b/657ef4f9/0cd9/450c/a9b1/4c9e55a289c5.png)](https://cdn.sbox.game/upload/b/657ef4f9/0cd9/450c/a9b1/4c9e55a289c5.png)After that, last thing we want to do is to disable eye attachments if our model doesn't use eye bones. Or, warnings will show up in the compile log and console. You're going to find the **"AttachmentLists"**. Click the dropdown and then you'll see **"Prefab [....]"**. Click the dropdown of that too. After that, you'll have to disable five nodes shown below. Hold **"Ctrl"** and click all five. Right-click and click **"Disable"**.[![](https://cdn.sbox.game/upload/b/eb32db9c/9076/41f5/a357/daae338d6c3d.png)](https://cdn.sbox.game/upload/b/eb32db9c/9076/41f5/a357/daae338d6c3d.png)And that's all for this section. We'll set up materials and textures for your model in the next section.  
────────────────────────────────────────────────────────────────────────

# 🎨 Material Setup

Alright, we don't want our model without any textures. In S&box. **Might be weird but your model won't work properly without having materials assigned.** But, It's very easy to set them up. I'd say it's much easier than **Source 1**.

**• Material Editor**

So, the first thing to do is create another folder inside your model's folder. Name it "materials" or something. You don't need to do this, but staying organized is a good habit. And, copy all of your model's texture files into that folder. Texture files will show up in the editor.[![](https://cdn.sbox.game/upload/b/841ac4f1/95fb/4152/a7d2/b0e127343899.png)](https://cdn.sbox.game/upload/b/841ac4f1/95fb/4152/a7d2/b0e127343899.png)  
[![](https://cdn.sbox.game/upload/b/b578174f/5d5d/4b40/a98a/682111b959ef.png)](https://cdn.sbox.game/upload/b/b578174f/5d5d/4b40/a98a/682111b959ef.png)After that, you will have to right-click a texture and click **"Create Material"**. It'll ask you where you want to save your material file, but just click **"Save"** as it'll point to your material folder by default. You can have a name for your material, too. But I'll leave it as it is.[![](https://cdn.sbox.game/upload/b/747c025a/8e0e/4913/b734/1eaedb611163.gif)](https://cdn.sbox.game/upload/b/747c025a/8e0e/4913/b734/1eaedb611163.gif)**Wait!**. For the models with **"PBR"** textures. You can add prefixes at the end of the normal map and other masks' names to set them up automatically for you. See : <https://sbox.game/dev/doc/assets/naming-conventions>[![](https://cdn.sbox.game/upload/b/16f543ec/e07d/4f91/967c/3e8a42f0539c.png)](https://cdn.sbox.game/upload/b/16f543ec/e07d/4f91/967c/3e8a42f0539c.png)So, you can rename the end prefixes of your PBR textures to set them up automatically by the **"Material Editor"** when you create a material of the color texture. If you're lazy. You can also set them up in the editor later.  
  
Anyway, you gotta have to repeat and keep creating the materials for every texture except for **"Normal maps** and **mask textures**" or any textures that serve as secondary texture. After that, we'll need to edit our material as necessary. For example, a texture that needs an alpha mask to work properly.

Open the **"VMAT"** of the texture that needs to be edited. **"Material Editor"** will be opened. I'll give you a quick rundown to get you comfortable with the tool.[![](https://cdn.sbox.game/upload/b/05f4ca76/ca4f/4b48/ac18/f07649732ddc.png)](https://cdn.sbox.game/upload/b/05f4ca76/ca4f/4b48/ac18/f07649732ddc.png)

> - Red area : Where you can create a new material, open an existing material through the material browser, save the material, and lastly, save all the materials.  
>   - Create a new material : **"Ctrl + N"**  
>   - Open a material file from the material browser : **"Ctrl + O"**  
>   - Open a material file from the file browser : **"Ctrl + Shift + O"**  
>   - Save current material : **"Ctrl + S"**  
>   - Save all edited materials : **"Ctrl + Shift + S"**
> - Blue area : Where you can select shaders through local or cloud.  
>   - By default, it'll always be **"Complex"** shader. For simple materials, you can also use **"Generic"** or **"Simple"** for simple PBR and many more.
> - Yellow area : Where you can turn on/off features of the shader you're using.  
>   - Features can be different depending on the shader, and some features can't be used together. You just need to tick the ones you want to use and provide the textures, or have to adjust what is needed.
> - Cyan area : Where you can adjust the settings and textures of the shader.  
>   - You can open/import textures and adjust settings for what is needed there. The **magnifying** glass icon buttons or **folder** icon buttons can be clicked to import textures through the texture browser or file browser.
> - Green area : Where you can preview the material you're editing. You can hold **"RMB"** while your cursor is in the viewport to move the camera around. You can also switch between **"Sphere, Cube, Plane, or Model"** to preview your material. Untick **"Overwrite"** if viewing as a model is preferred.

For editing the material. Here's what you need to know for editing. When finding the opening in the mask/texture file. Change **"Images"** to **"All Images"** every time you import a mask texture. Therefore, it'll display all mask textures without prefixes.[![](https://cdn.sbox.game/upload/b/2e6f3823/beed/4ae6/a33b/5974476d377b.png)](https://cdn.sbox.game/upload/b/2e6f3823/beed/4ae6/a33b/5974476d377b.png)And here are some guides about using mask textures.

- If you want to use an alpha mask : Tick **"Alpha Test"** or **"Translucent"**. A new option called **"Translucent"** will show up. You can click the folder icon to find your alpha mask.
- If you want to use **PBR** : Tick **"Specular"** from the **"PBR"** for PBR specular lighting. Also, tick **"Metalness Texture"** to use **Metalness map"**.
- If you want to use an emissive mask : Tick **"Selfillum"** and a new option called **"Selfillum"** will show up. Import your emissive mask and adjust settings if needed.

You just have to mess around for others as well. And you'll know how it works. Here's an example material setup.[![](https://cdn.sbox.game/upload/b/73cbb148/9cb9/45e8/aa32/5fc8fde498a4.png)](https://cdn.sbox.game/upload/b/73cbb148/9cb9/45e8/aa32/5fc8fde498a4.png)When you edited the material. Press **"Ctrl + S"** to save the material.  
  
**• Setting up Materials**

We're done with the materials. So, we'll go back to the **"ModelDoc"**. You'll see **"MaterialGroupList"**. Click the **"DefaultMaterialGroup"**. Make sure **"Globally Replace All Materials In Model"** is unticked. It'll be unticked, but untick it if it's ticked.  
And, you'll see the list of materials used in your model. We just need to open the material file for each one. Don't mind about my model lying down on the ground in the viewport.[![](https://cdn.sbox.game/upload/b/748fae06/4ac9/4481/9d30/8b943c1bc393.png)](https://cdn.sbox.game/upload/b/748fae06/4ac9/4481/9d30/8b943c1bc393.png)This part is very easy peasy. Just click the magnifying glass icon for each material and open your material files (VMAT) for each material slot. See how it did below.[![](https://cdn.sbox.game/upload/b/c5d21589/21dc/49a6/85e3/7bc5cd4a448a.png)](https://cdn.sbox.game/upload/b/c5d21589/21dc/49a6/85e3/7bc5cd4a448a.png)That's it. You just need to assign each material to its correct place. If you don't know which one should be used for which one. Check inside **"Blender"** for that. Click the **"Materials"** tab, select one material, and you'll see the imported texture files for the material.[![](https://cdn.sbox.game/upload/b/ebf1f256/5f69/4c41/bd41/039ef90db6a8.png)](https://cdn.sbox.game/upload/b/ebf1f256/5f69/4c41/bd41/039ef90db6a8.png)After all, press **"Needs Compiling"** and it'll compile your model, or you can also press **"F9"**. But, make sure you imported the correct files, including the **"anmgrph"** or the animations won't work. Wait a few good seconds and stalls.[![](https://cdn.sbox.game/upload/b/62038cc2/94b5/47b8/b4de/cb0cbbe85f79.png)](https://cdn.sbox.game/upload/b/62038cc2/94b5/47b8/b4de/cb0cbbe85f79.png)When it says **"Compiled and Up-To-Date"**, your model will be compiled as a **usable playermodel**.[![](https://cdn.sbox.game/upload/b/9efcc54c/5c96/46c5/840f/6552f7ca2768.png)](https://cdn.sbox.game/upload/b/9efcc54c/5c96/46c5/840f/6552f7ca2768.png)────────────────────────────────────────────────────────────────────────

# 👶 Size Adjustment

I know you were forced to scale down/up your model depending on your model to fit the reference armature in the script part. But we can fix it just by adjusting some values and calculations.   
  
**• Size adjustments**First, open your **"VMDL"** or if you're still in the **"ModelDoc"**. Scroll down a bit in the node outliner, and you'll see **"ModelModifierList"** with a node called **"ScaleAndMirror"**. And you'll see a value **"Scale"**.[![](https://cdn.sbox.game/upload/b/c122e0b9/8a6a/47be/b175/569be6e6160e.png)](https://cdn.sbox.game/upload/b/c122e0b9/8a6a/47be/b175/569be6e6160e.png)  
[![](https://cdn.sbox.game/upload/b/9771bcb8/bff6/44d4/b4c0/75e6e6fb1f56.png)](https://cdn.sbox.game/upload/b/9771bcb8/bff6/44d4/b4c0/75e6e6fb1f56.png)Let's just say your model is 1/4 of the reference armature's size. Then, we'll calculate the size by dividing **"0.3937"** with **"4"**. So, we get **"0.0984"**. Then we will type in the calculated value in the box and compile the model again. We'll have to eyeball it until it looks correct for this until I find a correct solution.  
For my model. It's just a little bit shorter than the reference armature. So, I'll just use **"0.3837"**. For your model, open the Blender scene file again, import your model, and compare it.[![](https://cdn.sbox.game/upload/b/ec47c094/6420/4444/9e2c/ef0184a0d9fa.png)](https://cdn.sbox.game/upload/b/ec47c094/6420/4444/9e2c/ef0184a0d9fa.png)  
[![](https://cdn.sbox.game/upload/b/47212cf3/00fe/4390/b938/25ce56d0b37c.png)](https://cdn.sbox.game/upload/b/47212cf3/00fe/4390/b938/25ce56d0b37c.png)After that, compile the model to see the changes. If you're not satisfied. Keep messing with the values until the size looks good for you.  
────────────────────────────────────────────────────────────────────────

# 👕 Adding Bodygroups [Optional]

[![](https://cdn.sbox.game/upload/b/f23b55d9/2a2b/4734/84a2/15840b691f43.png)](https://cdn.sbox.game/upload/b/f23b55d9/2a2b/4734/84a2/15840b691f43.png)In this section, we'll add bodygroups for our model. It's simple and easy. We only need to mess around in the **"ModelDoc"** for that. I'll guide you the way.

**• Adding bodygroups**

Adding bodygroups is very easy to do as well. But I learned to add them while writing this right here. It was fast to learn tho. Let's see.  
  
First. Make sure you're in the **"ModelDoc"**. Alright, You're in. So, if we want to make bodygroups. We also need to have them separated **renderMesh**. But, as we know. Our FBX is imported as one single file for all, and we don't have time to separate them inside **Blender**.  
  
Luckily, we have a trick to deal with it without having to mess with Blender. Click your imported rendermesh in the **"RenderMeshList"**. And, you'll see your model's parts being ticked.[![](https://cdn.sbox.game/upload/b/9f11511a/f550/4276/bcb7/dfb7ea1cfd89.png)](https://cdn.sbox.game/upload/b/9f11511a/f550/4276/bcb7/dfb7ea1cfd89.png)What we have to do is. Duplicate our rendermesh for the number of bodygroups we need. We'll keep one static. So, let me elaborate on our plan.  
  
We'll duplicate our rendermesh by selecting it in the node outliner and pressing **"Ctrl + D"**. And, we'll untick the parts we want as bodygroup in the first rendermesh and leave the parts we don't want as a bodygroup, such as face, hair, body parts, and some more.  
  
In the second one. We'll untick the ones from the first rendermesh and only tick what we want to have as a bodygroup part. And then, duplicate the second rendermesh as we need to make more bodygroups. We can also rename the rendermesh by pressing **"F2"** while the node is selected. See below.[![](https://cdn.sbox.game/upload/b/b173e675/7cd1/420c/973e/2f9e867446cf.gif)](https://cdn.sbox.game/upload/b/b173e675/7cd1/420c/973e/2f9e867446cf.gif)  
[![](https://cdn.sbox.game/upload/b/65924bc1/9e62/47bb/8d10/aaa14ba997b1.gif)](https://cdn.sbox.game/upload/b/65924bc1/9e62/47bb/8d10/aaa14ba997b1.gif)Just like that, I separated the tail part as a separate rendermesh without having to use Blender. We'll do it for many meshes we need for bodygroups. This is how I did. It's simple if you understand. Leave the first rendermesh with the main parts we don't want as bodygroups, and duplicate the rendermesh for the parts we want as bodygroups. After that, **compile the model again**. So, our separated meshes will be compiled to set up and use as bodygroup later.[![](https://cdn.sbox.game/upload/b/8c85e1ba/d883/4be1/a2ee/f891f5ae3235.png)](https://cdn.sbox.game/upload/b/8c85e1ba/d883/4be1/a2ee/f891f5ae3235.png)After that, we'll add a node called **"Bodygroup"**. Click **"Add"** and type in **"Bodygroup"** and click **"BodygroupChoice"** instead. So, we can skip the part of creating the parent node.[![](https://cdn.sbox.game/upload/b/828eb36b/bc75/47a2/be3d/aec4ee347fce.png)](https://cdn.sbox.game/upload/b/828eb36b/bc75/47a2/be3d/aec4ee347fce.png)And, click it. It'll ask you where the bodygroup choice should be created. We don't have any parent bodygroup node. So, click **"(New BodyGroup)"**. Type in a name for your bodygroup without spaces. Use underscores instead of spaces if you need. Click **"OK"** and a bodygroup will be created. I'll do a bodygroup for the tail. So, I'll name it **"Tail"**.[![](https://cdn.sbox.game/upload/b/8a6cd122/41ed/4c7a/a1a7/c849a139123b.png)](https://cdn.sbox.game/upload/b/8a6cd122/41ed/4c7a/a1a7/c849a139123b.png)  
[![](https://cdn.sbox.game/upload/b/60c9f3a7/c561/467a/860c/6fe7d8f643ce.png)](https://cdn.sbox.game/upload/b/60c9f3a7/c561/467a/860c/6fe7d8f643ce.png)When it's created. Click **"Choice #0 (default)"** and click **"Add mesh"** in the node editor, and click the small dropdown arrow to select the meshes we separated. You can select one and then add more if you need.  
[![](https://cdn.sbox.game/upload/b/513d04a1/b4ea/480f/9954/189af32e295f.png)](https://cdn.sbox.game/upload/b/513d04a1/b4ea/480f/9954/189af32e295f.png)  
[![](https://cdn.sbox.game/upload/b/be21836f/c636/4f21/920f/a325ec25dcd7.png)](https://cdn.sbox.game/upload/b/be21836f/c636/4f21/920f/a325ec25dcd7.png)After you added a mesh or more than two for a slot. Right-click the **"Bodygroup"** node with the name you gave and click **"Add BodyGroupChoice"**. And leave it empty to make an empty group, which will make the mesh be able to toggle off when you select the second choice. Just like how bodygroups in Source/Gmod do.[![](https://cdn.sbox.game/upload/b/2eaa8872/4fc0/48ec/b30b/6c9bbccb0ee7.png)](https://cdn.sbox.game/upload/b/2eaa8872/4fc0/48ec/b30b/6c9bbccb0ee7.png)Keep in mind that you can also make switchable bodygroups by adding many choices with different types of meshes. Example as **"Hat_01**, **Hat_02**, **Hat_03**", etc.. Having an empty group is optional too!. So, you just need to know how the bodygroups can work with, and it'll be very fun and useful to work with!  
  
Anyway, when you want to create a new bodygroup. Right-click **"BodyGroupList"** and click **"Add BodyGroup"**. And, you'll be able to do another one for other meshes. Keep repeating until you have added bodygroups for all the meshes you want as toggleable,

[![](https://cdn.sbox.game/upload/b/aa753566/2afb/4ca7/9475/9acb7131b21b.png)](https://cdn.sbox.game/upload/b/aa753566/2afb/4ca7/9475/9acb7131b21b.png)[![](https://cdn.sbox.game/upload/b/e2334f77/929e/4920/b6af/c1c598db041e.png)](https://cdn.sbox.game/upload/b/e2334f77/929e/4920/b6af/c1c598db041e.png)

Compile your model again, and the bodygroups will show up when you use your model in the scene editor. That's all for this section.[![](https://cdn.sbox.game/upload/b/322fd4d0/d4aa/4302/9b61/fbe3e6cd276b.png)](https://cdn.sbox.game/upload/b/322fd4d0/d4aa/4302/9b61/fbe3e6cd276b.png)────────────────────────────────────────────────────────────────────────

# 👁️ Moving Eyes [Optional]

Alright, you want extra work. Let's work then. For this section. It's still optional even if you had **"EYES_ENABLED"** as true. It's not very noticeable unless you look closer.  
We'll do some adjustments if needed, but I've adjusted the thing as best as I could. But, might need adjustments depending on your model's eye size and bones.  
  
**• Attachments adjustments**As long as your model has eye bones and is set up in the script. The eyes should be working. But, there's a chance it might've messed up. For that, you'll have to fix it by adjusting values.  
  
The first thing is fixing the eyes to face forward correctly. Your model's eyes might not be facing the foward correctly. To fix that. Open your **"VMDL"** to open it in the **"ModelDoc"**. Scroll down in the node outliner and find **"AttachmentList"**. You'll see two attachments below it.  
  
Select each ones and you'll have to edit the **Y** value in **"Relative Angles"** in the node editor. By default. It should be **"90"**, which works best for me. If your model is having a problem with that value. Try decreasing or increasing the value of the value and compile the model again.[![](https://cdn.sbox.game/upload/b/35740a3a/e6a3/4889/a436/7ef1b55d0938.png)](https://cdn.sbox.game/upload/b/35740a3a/e6a3/4889/a436/7ef1b55d0938.png)There's also a note saying about that. So, I hope you understood that.  
After that, for models with big eyes. You'll have to adjust the **"Reduce_Eye_Darting"** weightlist.  
You'll find it under **"WeightListList"**. Select it and adjust the slider values of **"eye_L** and **"eye_R"**[![](https://cdn.sbox.game/upload/b/4ebfb4f6/6dc4/4f10/9ea8/250d9c8b23d3.png)](https://cdn.sbox.game/upload/b/4ebfb4f6/6dc4/4f10/9ea8/250d9c8b23d3.png)I haven't ported any models with big eyes or gotten problem with it. So, I can't tell what's good for you. My model is fine with how it is. Here's the note for that.  
  
"Some models have their eye bone far behind the eye, so the pivot angle is greater than the human citizen model, which has the eye bone in the center of the eye. Adjust the eye_R and eye_L sliders below to adjust how much to reduce the animation by. The default is 75%, meaning that the animation is 25% of what it normally is."

**• Adjusting Eye Movement**

After that, you can do one more thing. Which is limiting how much the eyes can move. You might want to use it to make the eyes move further or use it to fix some issues. To do that, move your eyes up to the **"Graph"** thing first. Where the **"anmgrph"** for your model is loaded. You'll see an **"Edit"** button. Click it.[![](https://cdn.sbox.game/upload/b/71b5a869/1cd3/4799/b093/6c04fa26e35c.png)](https://cdn.sbox.game/upload/b/71b5a869/1cd3/4799/b093/6c04fa26e35c.png)Move your cursor into the checkerboard window where all of the animation nodes are located. funny checkboards.. And then, hold **"MMB"** to move around. But, you gotta move to the right side. Scroll your **"MMB"** button to zoom in/out. What we gotta find is four green nodes above a huge **"Section 05..."** node.[![](https://cdn.sbox.game/upload/b/d5aa030a/5ffc/4fcb/b54e/538683998146.gif)](https://cdn.sbox.game/upload/b/d5aa030a/5ffc/4fcb/b54e/538683998146.gif)When you found them, you gotta have to edit all four of them. First, by selecting one of them, it'll show its properties in the **"Properties"** panel. You'll have to adjust **"Pitch"** and **"Yaw"** values to limit or give the eyes a bigger space. And when you're satisfied. Press **"Ctrl + S"** and close the **"AnimGraph"**.[![](https://cdn.sbox.game/upload/b/6a42220f/449c/45e3/b0da/50fefcb81953.png)](https://cdn.sbox.game/upload/b/6a42220f/449c/45e3/b0da/50fefcb81953.png)  
[![](https://cdn.sbox.game/upload/b/f13d8be5/b2bf/41dc/be09/e906d5783d5e.png)](https://cdn.sbox.game/upload/b/f13d8be5/b2bf/41dc/be09/e906d5783d5e.png)If you want to disable the feature. You'll have to find the **"GameDataList"** category. Click the dropdown of **"Prefab [...]"**. And, you'll see **"LookAtChains"** group. Click the dropdown of it and scroll a bit. You'll see **"EyeRLookChain"** and **"EyeLLookChain"** nodes. All you gotta do is right-click and click **"Disable"** and compile your model again.[![](https://cdn.sbox.game/upload/b/898f92d6/7c28/4a59/bd1b/8122faf141fa.png)](https://cdn.sbox.game/upload/b/898f92d6/7c28/4a59/bd1b/8122faf141fa.png)────────────────────────────────────────────────────────────────────────

# ⏩ Animation speeds [Optional]

For very tiny models or models half the size of a human citizen or less. Your model might be sliding on the ground instead of walking, crouching, or running. You can easily fix that.

**• Sliding animation fix**

Open your **"AnmGrph"** in the **"ModelDoc"** again. And, then you'll see a tab called **"Parameters"**. By default, the tab is very small. So, we can hold the edge of the tab with our cursor and move it up to move up the tab. like this.[![](https://cdn.sbox.game/upload/b/b2432363/c03d/4654/88ec/0e82188e078c.png)](https://cdn.sbox.game/upload/b/b2432363/c03d/4654/88ec/0e82188e078c.png)After that, scroll down in the list and find **"speed_scale"** float parameter right under **"speed_reload"**. Select it and you'll see its properties in the **"Properties"** tab. Change **"Default Value"** to higher to fix the issue. Press **"Ctrl + S'** to save it. See the changes in the scene editor. Modify if not satisfied. Repeat until it looks fine. For very tall models. You might need to do the opposite to fix the issue.[![](https://cdn.sbox.game/upload/b/75fed42e/1e48/49ce/ac29/e937d9dc2dda.png)](https://cdn.sbox.game/upload/b/75fed42e/1e48/49ce/ac29/e937d9dc2dda.png)That's all for this section :)  
────────────────────────────────────────────────────────────────────────

# 🏃‍➡️ Testing

Oh boy.. We've been doing this thing for a while. Now, it's time to test it. To do that, we'll create a **"Player Controller"** and replace our custom model with the sausage model. Let's do this.

**• Testing the playermodel**

First, right-click in the scene viewport or in the hierarchy. Hover your cursor on **"Create"** and then click **"Player Controller"**. Name the controller whatever you like, and then the player controller with a sausage guy will be created. Pull the controller until it touches the ground if it's flying. Oh, btw, sausage guy's name is **"Terry"**. But, we don't want **"Terry"**. Instead, we'll use our model.[![](https://cdn.sbox.game/upload/b/95859c18/a1b0/4315/8506/75b41c26674e.png)](https://cdn.sbox.game/upload/b/95859c18/a1b0/4315/8506/75b41c26674e.png)Click the small arrow beside **"Player Controller"** in the hierarchy. You'll see a child component called **"Body"**. Click it and see the inspector. The model is rendered with a **"Model Renderer (skinned)"**, and you'll see that the sausage model is used there.  
  
To use our custom model. Drag our custom model's **"VMDL"** from the **"Asset Browser"** and drop it in the box beside with **"Model"**. Bam. Terry is now gone and will be switched to your custom model.[![](https://cdn.sbox.game/upload/b/bbc4bb03/24ed/4326/9434/7064312edac5.png)](https://cdn.sbox.game/upload/b/bbc4bb03/24ed/4326/9434/7064312edac5.png)To play around with your model and test. Click the green **▶** button at the top. Scene will load, and you'll get to control your custom model. Move around, jump around, Crouch and more to test your model if it's fine or not. It'll be fine as long as you follow the instructions carefully![![](https://cdn.sbox.game/upload/b/c00c1d8e/03fb/4643/864a/594284bae0cb.gif)](https://cdn.sbox.game/upload/b/c00c1d8e/03fb/4643/864a/594284bae0cb.gif)  
[![](https://cdn.sbox.game/upload/b/e4ed2ee8/81f3/4cb9/93c4/02909c6d18e3.gif)](https://cdn.sbox.game/upload/b/e4ed2ee8/81f3/4cb9/93c4/02909c6d18e3.gif)  
[![](https://cdn.sbox.game/upload/b/b4de25a3/dd9b/420f/a04a/061c9b8d23b0.gif)](https://cdn.sbox.game/upload/b/b4de25a3/dd9b/420f/a04a/061c9b8d23b0.gif)As you can see, mine is working correctly. If it's working correctly. Congrats! You just ported a custom model into **S&box**!. To test the ragdoll physics. Drag and drop your model's **"VMDL"** into the scene and place it anywhere, and click the play button.  
  
You might ask why we don't have to do the ragdoll ourselves? Because the collision joints and collisions are calculated when we compile our model. We used the citizens' VMDL as a base. So, they're set up for you. But sometimes. There can be issues with it but it's very rare.  
  
That's all for this section!. You made it! :D  
────────────────────────────────────────────────────────────────────────  
────────────────────────────────────────────────────────────────────────

# 🏁 Final Words

**Huge congrats!** You just finished the guide. I know this guide would be pretty long to write, and I wrote this guide in just 5 days after finding a proper way. I ain't a professional in this area yet. So, feel free to point out mistakes, give suggestions, and more as you want.  
  
I hope this guide is useful for people who want to use custom models and who've been hating **"S&box"** for currently sausage (Terry) and default citizens available to use. There's currently no custom playermodel support for the sandbox gamemode yet. We'll most likely get it because why not? But you can still use them in your own game in the meantime.[![](https://cdn.sbox.game/upload/b/60587bf8/e5e5/4463/8248/e49a70c8d38f.png)](https://cdn.sbox.game/upload/b/60587bf8/e5e5/4463/8248/e49a70c8d38f.png)Oh—and if this guide helped you out, feel free to share it with someone who needs it. Spread this one out as you can!  
Thank you so much for using the guide! :)  
────────────────────────────────────────────────────────────────────────

# 👑 Credits & Changelogs

**Credits** to everyone who deserves it and, **”Changelog”** for the guide.  
  
— **”Credits”** —

[**乃ㄖ乃爪卂匚 Ü**](https://steamcommunity.com/id/Bobmacjefferson) **: Writing the guide**

[**Rokkira**](https://steamcommunity.com/profiles/76561198062671681) **: Friend who helped with the process**

[**Noztik**](https://steamcommunity.com/linkfilter/?u=https%3A%2F%2Fgithub.com%2FNoztik) **: The creator of the convert script**

[**Max**](https://steamcommunity.com/profiles/76561197999825207) **: Explaining the concept and additional help**

[**Grodbert**](https://steamcommunity.com/profiles/76561198049083824) **: Additional helps**

— **”Change Log”** —  
  
**V1.0** - **”Tutorial released!”**  
  
• Released the tutorial in **S&box tutorials**.  
────────────────────────────────────────────────────────────────────────
