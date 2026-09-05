---
title: Retargeting Humanoid Animations
slug: notpointless/retarget-humanoid-animations
url: https://sbox.game/learn/notpointless/retarget-humanoid-animations
author: chomnr
author_slug: notpointless
difficulty: Beginner
topic: Animation
content_type: Video
tags: [animation, humanoid, retargeting]
rating: 1
views: 37
upvotes: 0
downvotes: 2
updated: 'Updated

  2 days ago'
summary: Retarget humanoid animations between different rigs in s&box with automatic
  bone mapping, root motion, and optional animation variants.
scraped_at: '2026-09-05T10:07:48Z'
---

# Retargeting Humanoid Animations

> Retarget humanoid animations between different rigs in s&box with automatic bone mapping, root motion, and optional animation variants.

# Requirements

- [Humanoid Retargeter](https://sbox.game/notpointless/chomnr_humanoid_retargeter)
- A rigged humanoid model
- A humanoid animation

Your target model should already be properly rigged and imported into s&box before proceeding. Make sure the skeleton contains the expected humanoid bones and that the armature is configured correctly.

# Additional Features

Humanoid Retargeter can also generate optional animation variants during conversion:

- **Footstep Events** Adds footstep events at detected foot contacts for sounds, effects, or gameplay.
- **Mirrored Variants** Creates a mirrored version of the animation by swapping the left and right sides.
- **Additive Variants** Creates an additive version that can be layered on top of another animation or pose.

# 1. Open the Humanoid Retargeter

In the s&box Editor, open the Humanoid Retargeter from:   
  
 View → Humanoid Retargeter   
[](https://cdn.sbox.game/upload/b/05cba447/ffd9/450b/94d3/7d00b499c2fb.mp4)

# 2. Select Your Source Animation

Click **+ Add Files...** and select the humanoid animation you want to retarget.  
[](https://cdn.sbox.game/upload/b/9d0f913f/d20a/48ab/99eb/16fc1f07737f.mp4)

Once added, the Humanoid Retargeter will load the animation and detect its skeleton automatically.

# 3. Select Your Target Model ◇ Optional

Click the **Target Model** field and select the humanoid model you want the animation retargeted onto.  
   
note: custom model support is still a little sketchy. consider it in alpha.   
[](https://cdn.sbox.game/upload/b/f77d014a/c600/4e3b/9791/a6e59199bb2d.mp4)

if no target model is selected, the Humanoid Retargeter can still process the animation using its detected humanoid mapping.

# 4. Choose an Output ◇ Optional

Select an **Output** location if you want to choose where the retargeted animation will be saved.

If left empty, the Humanoid Retargeter will use its default output location.

# 5. Convert the Animation

Once everything is ready, click **Convert All** to retarget the animation.

[](https://cdn.sbox.game/upload/b/f3e9ee25/16ac/4877/ba79/de48f17407a6.mp4)

When the conversion finishes, the retargeted animation will be available on your output model and ready to use in s&box.
