---
title: Seperate viewmodel FOV rendering
slug: brax/viewmodel-fov
url: https://sbox.game/learn/brax/viewmodel-fov
author: Braxnet
author_slug: brax
topic: Capable
content_type: Text
rating: 2
views: 99
upvotes: 1
downvotes: 0
updated: 'Updated

  12 days ago'
scraped_at: '2026-11-14T13:07:53Z'
---

# Seperate viewmodel FOV rendering

[![](https://cdn.sbox.game/upload/b/1b7de7b6/3a14/4d5d/bbb0/cc106594c247.png "Before")](https://cdn.sbox.game/upload/b/1b7de7b6/3a14/4d5d/bbb0/cc106594c247.png)[![](https://cdn.sbox.game/upload/b/61fbc375/1661/48f3/883a/6803b9cbe5ec.png "After")](https://cdn.sbox.game/upload/b/61fbc375/1661/48f3/883a/6803b9cbe5ec.png)

View models are drawn by the main camera, so they change size with the player's FOV. This draws them at a fixed FOV instead, so you pose them once and they look the same at any setting. They're still lit and shadowed by the world, graded with it, drawn over walls and under the HUD.  
  
It works by rendering the view models in a second view from inside the main camera's frame, with `CommandList.DrawView`, and blending the result over the frame before post-processing. Nothing is scaled, so models parented to bones stay in place.  
  
Written for s&box 26.10.27.

# Setup

1. Add `ViewModelFov.cs` to your code and put the component on your main camera.
2. Put `viewmodel_composite.shader` at `Assets/shaders/viewmodel_composite.shader`.
3. Tag the root of every view model `viewmodel`.
4. If your view models use the overlay layer, call `ViewModelFov.UseGameLayer( viewModel )` when you create one, or they're drawn twice.

Pose your view models at the component's `FieldOfView`, 60 by default.

# How it works

- A disabled camera sees only `viewmodel`, `light` and `viewmodel_light`, at the view model FOV.  
- A command list on the main camera, at `Stage.AfterTransparent`, renders it into an HDR texture with `DrawView`, with a transparent background and post-processing off.  
- A full-screen premultiplied alpha blend lays the texture over the frame. Bloom, tonemapping and the UI come after it.  
- The main camera excludes `viewmodel`.  
  
Lights carry `light` by default. The sky and envmap probes get `viewmodel_light` so their reflections reach the view models without the sky being drawn. The sun's shadow cascades are reused from the main view, so the world shadows the view models.

# ViewModelFov.cs

```
using Sandbox.Rendering;

/// <summary>
/// Draws everything tagged "viewmodel" at a field of view of its own, whatever the camera's. Put it on the main camera.
///
/// A second, disabled camera renders the view models from inside the main camera's frame into an HDR texture, which is
/// laid over the frame before post processing. The view models are lit and shadowed by the world, graded with it,
/// drawn over walls and under the HUD, and nothing is scaled, so models parented to bones stay where they belong.
/// </summary>
[Title( "View Model FOV" ), Category( "Rendering" ), Icon( "back_hand" )]
public sealed class ViewModelFov : Component
{
	/// <summary>Put this on the root of every view model. Tags are inherited, so its children come along.</summary>
	public const string ViewModelTag = "viewmodel";

	/// <summary>Every Light carries this by default, so the view models are lit by every light.</summary>
	public const string LightTag = "light";

	/// <summary>
	/// Given to the sky and to envmap probes so their reflections reach the view models. Envmap probes have no tag of
	/// their own, and the sky's cubemap carries "skybox", which would draw the sky over the whole frame.
	/// </summary>
	public const string ReflectionsTag = "viewmodel_light";

	/// <summary>The field of view the view models are authored at and drawn at, on the camera's own FOV axis.</summary>
	[Property, Range( 30, 120 )] public float FieldOfView { get; set; } = 60f;

	[Property, Range( 0.1f, 10f )] public float NearClip { get; set; } = 0.5f;

	private CameraComponent _world;
	private CameraComponent _camera;
	private CommandList _commands;
	private Material _composite;
	private TimeSince _sinceTagged;

	protected override void OnEnabled()
	{
		_world = GetComponent<CameraComponent>();
		if ( !_world.IsValid() )
		{
			Log.Warning( $"{this} needs a CameraComponent on the same GameObject" );
			return;
		}

		_composite = Material.FromShader( "shaders/viewmodel_composite.shader" );

		// At the scene root, not under the main camera: post process effects are gathered from a camera's children.
		var cameraObject = new GameObject( true, "View Model Camera" ) { NetworkMode = NetworkMode.Never };
		cameraObject.Flags |= GameObjectFlags.NotSaved;

		// Disabled, so it only renders when the main camera's command list asks it to.
		_camera = cameraObject.Components.Create<CameraComponent>( false );
		_camera.IsMainCamera = false;
		_camera.EnablePostProcessing = false;
		_camera.BackgroundColor = Color.Transparent;
		_camera.ZNear = NearClip;
		_camera.ZFar = 1000f;
		_camera.RenderTags.Add( ViewModelTag );
		_camera.RenderTags.Add( LightTag );
		_camera.RenderTags.Add( ReflectionsTag );

		_commands = new CommandList( "View Model FOV" ) { Flags = CommandList.Flag.PostProcess };

		// HDR, so the view models go into the frame before tonemapping, the same as the world.
		var target = _commands.GetRenderTarget( "viewmodel_fov", 1, ImageFormat.RGBA16161616F, ImageFormat.Default );
		_commands.DrawView( _camera, target, new ViewSetup
		{
			EnablePostprocessing = false,
			EnableUI = false,
			ClearColor = Color.Transparent,
			ViewHash = 0x564d464f
		} );
		_commands.ResourceBarrierTransition( target, ResourceState.PixelShaderResource );
		_commands.Attributes.Set( "ViewModelColor", target.ColorTexture );
		_commands.Blit( _composite );

		// The main camera stops drawing the view models; the command list draws them instead. AfterTransparent is
		// before bloom, tonemapping and the UI, and a negative order puts it ahead of depth of field.
		_world.RenderExcludeTags.Add( ViewModelTag );
		_world.AddCommandList( _commands, Stage.AfterTransparent, -100 );

		_sinceTagged = float.MaxValue;
	}

	protected override void OnDisabled()
	{
		if ( _world.IsValid() )
		{
			_world.RemoveCommandList( _commands );
			_world.RenderExcludeTags.Remove( ViewModelTag );
		}

		_camera?.GameObject.Destroy();
		_camera = null;
		_commands = null;
	}

	protected override void OnPreRender()
	{
		if ( !_world.IsValid() || !_camera.IsValid() ) return;

		_camera.Enabled = false;
		_camera.WorldTransform = _world.WorldTransform;
		_camera.FovAxis = _world.FovAxis;
		_camera.FieldOfView = FieldOfView;
		_camera.ZNear = NearClip;

		// Hidden the same ways as on the main camera, except for the view model tag itself.
		var excluded = new TagSet();
		foreach ( var tag in _world.RenderExcludeTags.TryGetAll() )
		{
			if ( tag != ViewModelTag ) excluded.Add( tag );
		}

		_camera.RenderExcludeTags = excluded;

		// Skies and probes come and go with maps, so look for them again now and then.
		if ( _sinceTagged > 2f )
		{
			_sinceTagged = 0;
			foreach ( var sky in Scene.GetAllComponents<SkyBox2D>() ) sky.GameObject.Tags.Add( ReflectionsTag );
			foreach ( var probe in Scene.GetAllComponents<EnvmapProbe>() ) probe.GameObject.Tags.Add( ReflectionsTag );
		}
	}

	/// <summary>
	/// Moves a view model's renderers from the overlay layer to the game layer. The overlay layer keeps view models out of
	/// walls when the main camera draws them, but here it would only draw them twice. Renderers on neither layer, like a
	/// hidden animation rig, are left alone.
	/// </summary>
	public static void UseGameLayer( GameObject viewModel )
	{
		foreach ( var renderer in viewModel.Components.GetAll<ModelRenderer>( FindMode.EverythingInSelfAndDescendants ) )
		{
			if ( !renderer.RenderOptions.Overlay ) continue;

			renderer.RenderOptions.Game = true;
			renderer.RenderOptions.Overlay = false;
		}
	}

	/// <summary>
	/// Where the main camera sees a point of a view model: the same place on screen, nearer or further. Use it for
	/// anything that is hit by the main camera's rays, like a world panel on a view model.
	/// </summary>
	public Vector3 ToWorldView( Vector3 point )
	{
		if ( !_world.IsValid() ) return point;

		var eye = _world.WorldPosition;
		var forward = _world.WorldRotation.Forward;
		var depth = Vector3.Dot( point - eye, forward );

		return point + forward * (depth * (HalfFovTangent( FieldOfView ) / HalfFovTangent( _world.FieldOfView ) - 1f));
	}

	private float HalfFovTangent( float fieldOfView )
	{
		var degrees = _world.FovAxis == CameraComponent.Axis.Vertical
			? Screen.CreateVerticalFieldOfView( fieldOfView, Screen.Aspect )
			: fieldOfView;

		return MathF.Tan( degrees.DegreeToRadian() * 0.5f );
	}
}
```

# viewmodel_composite.shader

```
HEADER
{
    Description = "Puts the view models, drawn by ViewModelFov at a field of view of their own, over the world before post processing";
    DevShader = true;
}

MODES
{
    Default();
    Forward();
}

FEATURES
{
}

COMMON
{
    #include "postprocess/shared.hlsl"
}

struct VertexInput
{
    float3 vPositionOs : POSITION < Semantic( PosXyz ); >;
    float2 vTexCoord : TEXCOORD0 < Semantic( LowPrecisionUv ); >;
};

struct PixelInput
{
    float2 vTexCoord : TEXCOORD0;

    #if ( PROGRAM == VFX_PROGRAM_VS )
        float4 vPositionPs : SV_Position;
    #endif

    #if ( PROGRAM == VFX_PROGRAM_PS )
        float4 vPositionSs : SV_Position;
    #endif
};

VS
{
    PixelInput MainVs( VertexInput i )
    {
        PixelInput o;
        o.vPositionPs = float4( i.vPositionOs.xy, 0.0f, 1.0f );
        o.vTexCoord = i.vTexCoord;
        return o;
    }
}

PS
{
    #include "postprocess/common.hlsl"

    // over everything, so the view models never go into walls
    RenderState( DepthEnable, false );
    RenderState( DepthWriteEnable, false );

    // the view models' texture was cleared to nothing, so its colour is already multiplied by its alpha
    RenderState( BlendEnable, true );
    RenderState( SrcBlend, ONE );
    RenderState( DstBlend, INV_SRC_ALPHA );

    // linear HDR, the same as the world it goes over
    Texture2D g_tViewModel < Attribute( "ViewModelColor" ); SrgbRead( false ); >;

    float4 MainPs( PixelInput i ) : SV_Target0
    {
        return g_tViewModel.Load( int3( i.vPositionSs.xy, 0 ) );
    }
}
```
