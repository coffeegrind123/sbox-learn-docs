---
title: Writing shaders that respond to Quality Settings
slug: carsonk/shader_quality_settings
url: https://sbox.game/learn/carsonk/shader_quality_settings
author: Carson Kompon
author_slug: carsonk
topic: Capable
content_type: Text
tags: [quality, render, settings, shader]
rating: 4
views: 1011
upvotes: 12
downvotes: 0
updated: 'Updated

  12 Days Ago'
summary: How to make your shaders run better when players have low video settings
scraped_at: '2026-06-10T10:05:15Z'
---

# Writing shaders that respond to Quality Settings

> How to make your shaders run better when players have low video settings

# Accessing Video Quality Settings via ConVars

The different video settings in s&box actually just set ConVars behind-the-scenes.

**Reading ConVars from Game Code**

```
using Sandbox;

// Read a convar value (always returns string)
string value = ConsoleSystem.GetValue( "r.shadows.quality" );

// Convert to the type you need
int shadowQuality = ConsoleSystem.GetValue( "r.shadows.quality" ).ToInt();
float maxAniso = ConsoleSystem.GetValue( "r_max_anisotropy" ).ToFloat();
bool muted = ConsoleSystem.GetValue( "snd_mute" ).ToBool();
```

# Available Quality ConVars

These are set based on the user's Video Settings.

**Shadow Quality**

| ConVar                                           | Low | Medium | High | Description                                          |

|----------------------------|-----|--------|-----|-------------------------------|

| `r.shadows.quality`                    | 1       | 2              | 3        | Shadow filter quality (tap count) |

| `r.shadows.maxresolution`        | 512   | 1024        | 2048 | Max shadow map resolution         |

| `r.shadows.csm.maxresolution` | 1024 | 2048      | 4096 | CSM atlas resolution                        |

| `r.shadows.csm.maxcascades`    | 2       | 3             | 4        | Number of CSM cascades              |

**Post-Process Quality**

| ConVar                                 | Low | Medium | High | Description                                                                       |

|-----------------------|-----|--------|------|--------------------------------------------|

| `r_ao_quality`                     | 1       | 2             | 3          | Ambient occlusion sample count tier                     |

| `r_ao_resolution`               | 4      | 2             | 2          | AO resolution downscale factor                               |

| `r_dof_quality`                   | 1       | 2             | 3          | Depth of field quality                                                   |

| `r_motionblur_quality`     | 0      | 1              | 2          | Motion blur sample tier (0=off)                                |

| `r_ssr_downsample_ratio` | 0      | 4             | 2          | Screen-space reflections downsample (0=off)   |

**Texture Quality**

| ConVar                                                             | Low  | Medium | High   | Description                                        |

|-------------------------------------|-----|--------|------|------------------------------|

| `r_texture_stream_max_resolution`           | 1024  | 2048      | 8192   | Max streamed texture resolution |

| `r_texture_stream_resolution_bias_min` | 0.5     | 0.8          | 1.0      | Minimum mip bias                           |

| `r_max_anisotropy`                                         | 1         | 2             | 4        | Anisotropic filtering level                 |

**Volumetric Fog Quality**

| ConVar                      | Low  | Medium | High     | Description                       |

|------------------|-----|--------|-------|----------------------|

| `volume_fog_width`  | 60     | 120         | 240      | Fog volume X resolution |

| `volume_fog_height`| 40     | 80          | 160       | Fog volume Y resolution |

| `volume_fog_depth`  | 32     | 32           | 64        | Fog volume Z slices         |

# Defining Your Own Quality ConVar

```
using Sandbox;

public static class MyShaderQuality
{
    [ConVar( "my_effect_quality", Min = 0, Max = 3 )]
    public static int Quality { get; set; } = 2;
}
```

**Listening for Changes**

Use the `[Change]` attribute on your ConVar property:

```
[ConVar( "my_effect_quality" )]
[Change]
public static int Quality { get; set; } = 2;

private static void OnQualityChanged( int oldValue, int newValue )
{
    Log.Info( $"Quality changed: {oldValue} -> {newValue}" );
    // Update your shader attributes, rebuild materials, etc.
}
```

# Passing ConVar Values to Your Custom Shader

In a post-process component or rendering hook:

```
public override void Render()
{
    int quality = ConsoleSystem.GetValue( "r_ao_quality" ).ToInt();

    // Pass as a shader attribute
    Attributes.Set( "MyAOQuality", quality );

    // Or toggle a dynamic combo
    Attributes.SetCombo( "D_MY_EFFECT", quality > 0 ? 1 : 0 );

    Blit( blitMode, "MyEffect" );
}
```

In your `.shader` file:

```
// Read the attribute
int MyAOQuality < Attribute( "MyAOQuality" ); Default( 2 ); >;

// Or use a dynamic combo for compile-time branching
DynamicCombo( D_MY_EFFECT, 0..1, Sys( All ) );

MainPs( PixelInput i )
{
    #if ( D_MY_EFFECT == 0 )
        return baseColor;
    #endif

    // Quality-adaptive sampling
    int samples = MyAOQuality * 4; // 4, 8, 12
    // ...
}
```

# Quick Reference: Reading Current Quality Tier

```
/// Returns 0-3 representing the current shadow filter quality
public static int GetShadowQuality() =>
    ConsoleSystem.GetValue( "r.shadows.quality" ).ToInt();

/// Returns 0-3 representing post-process AO quality
public static int GetAOQuality() =>
    ConsoleSystem.GetValue( "r_ao_quality" ).ToInt();

/// Returns 0-2 representing motion blur quality (0 = off)
public static int GetMotionBlurQuality() =>
    ConsoleSystem.GetValue( "r_motionblur_quality" ).ToInt();
```
