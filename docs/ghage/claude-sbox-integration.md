---
title: Claude Code (and any MCP client) inside sbox-dev
slug: ghage/claude-sbox-integration
url: https://sbox.game/learn/ghage/claude-sbox-integration
author: ghage
author_slug: ghage
topic: Expert
content_type: Text
tags: [agent, ai, automation, claude]
rating: 1
views: 1473
upvotes: 3
downvotes: 4
updated: 'Updated

  26 Days Ago'
summary: Wire a coding agent into the live editor — drive the scene, query the API,
  write C#, all over a localhost MCP server.
scraped_at: '2026-06-15T12:19:42Z'
---

# Claude Code (and any MCP client) inside sbox-dev

> Wire a coding agent into the live editor — drive the scene, query the API, write C#, all over a localhost MCP server.

# Claude Code (and any MCP client) inside sbox-dev

> Wire a coding agent into the live editor — drive the scene, query the API, write C#, all over a localhost MCP server.

`claude-sbox` is an editor addon that exposes everything reachable from `sbox-dev`'s menus, docks, console, and managed-DLL surface to an MCP-speaking agent like Claude Code, Codex, Claude Desktop, or Cline. The agent can spawn prefabs, drive Hammer cameras, swap entity classes, query the live API schema, run C# snippets, batch-transform selections, hot-reload code — anything you can do by hand in the editor, plus a few things you can't (`reflection_*`, `host_grep`, `dispatcher_batch`, etc).  
  
This walks you through what it is, how to install it, and how to point Claude Code at it. The addon page at <https://sbox.game/f/gendev/2638/1/> has a 5-line install snippet if you just want that.

# What you get

Two things land in the editor once the addon mounts:  
  
**A dock widget at View → ClaudeSbox** — a real PTY terminal docked next to the Console / Asset Browser. Spawns `cmd.exe` on Windows / `bash` on Linux by default; you type whatever drops you into your agent host (e.g. `docker exec -it <your-container> bash`, then `claude`). Full xterm.js-grade grid rendering so TUI agents like Claude Code display correctly.  
  
**An MCP server on** **`http://127.0.0.1:6790`** — localhost-only, three concurrent transports on the same port so whatever MCP client you have already works:  
  
- `POST /<toolname>` — bespoke wire shape the bundled stdio bridge translates into.  
- `POST /mcp` — MCP JSON-RPC 2.0 Streamable HTTP. Direct connection, no bridge needed.  
- `GET /sse` + `POST /sse/message` — legacy SSE transport for older clients.

# What the agent can do

~597 tools surface across these areas. The complete inventory with arg shapes lives in the setup repo at <https://github.com/coffeegrind123/claude-sbox-setup/blob/main/skill/references/mcp-tools.md> — short version:  
  
- **Scene + inspector** — `get_active_scene`, `list_gameobjects`, `set_selection`, `set_property`, `instantiate_prefab`, `batch_transform`, full GameObject lifecycle (`_create`, `_destroy`, `_set_parent`, `_add_component`, etc).  
- **Hammer** — list/select mapnodes, drive `mapview_get_camera` / `_set_camera` per viewport, swap entity classnames, inspect entity-class schemas (Variables/Inputs/Outputs/Tags), validate entity-I/O wiring before you commit it.  
- **ModelDoc / AnimGraph** — session queries, sequence playback, body groups, attachments, hitboxes, bone-tree introspection over any `.vmdl` (including `model_get_info` and `_list_bones` on cold-loaded files).  
- **Schema + docs** (live) — `schema_*` runs over the editor's loaded assemblies, fingerprinted per hot-reload so the agent always queries the current API surface, not stale docs. `docs_*` mirrors `Facepunch/sbox-docs` with citations.  
- **Roslyn devtools** — `compile_snippet` returns real diagnostics, `parse_syntax_tree` dumps the AST, `execute_csharp` runs C# in-editor against the live editor state.  
- **Compile + hotload** — `compile_project`, `hotload_get_last_result`, async `start_compile_project_job` + `poll_job` for long builds.  
- **Physics + audio + particles + NavMesh** — `add_collider(shape)`, `add_joint(type)` (8 joint types), `rigidbody_apply_force`, `sound_play_event` + sound-handle tracking, particle runtime control, `navmesh_calculate_path`.  
- **Assets** — `find_asset`, `list_assets`, `asset_search` against sbox.game's public package library, `asset_mount` (auto-pins to project), full asset CRUD with thumbnail rebuilds + in-memory overrides.  
- **Cross-reference + heap** — `find_type_usages`, `find_method_overrides`, `heap_walk_by_type` for diagnosing managed-side issues.  
- **UI drive** — `list_docks`, `list_menus`, `list_shortcuts`, `invoke_menu`, `invoke_shortcut`, `click_widget`, `send_keys`. Anything in a dock or menu is callable by name.  
- **Auto-generated** — every `[Menu]` / `[Shortcut]` / `[ConCmd]` / `[Editor.Tool]` discovered at startup gets a wrapper tool automatically (~50-150 depending on loaded addons), so new editor tools your own addons add become agent-callable with zero glue code.

# Install

You need a working sbox-public checkout (`git clone --recursive https://github.com/Facepunch/sbox-public`).  
  
**Setup repo + engine patches + rebuild.** From a terminal in `<sbox-public>/game/addons/`:

```
git clone https://github.com/coffeegrind123/claude-sbox-setup.git
cd claude-sbox-setup
.\Setup.bat
.\Bootstrap-And-Capture.bat
```

`Setup.bat` applies seven small engine patches to your sbox-public tree. Required by both install paths — they fix the cloud-mount whitelist gates that would otherwise block `package_install` for any tool-type addon, plus a couple of bootstrap-side issues. Idempotent: re-run after every `git pull` on sbox-public. `Bootstrap-And-Capture.bat` recompiles the managed DLLs against the patched source — the editor loads compiled DLLs out of `game/bin/managed/`, so without the rebuild step the patches do nothing. First Bootstrap is slow (~5-15 minutes depending on NuGet cache state); incremental rebuilds afterward are fast.  
  
(Linux: `./Setup.sh` and `./Bootstrap-And-Capture.sh` — full Linux walkthrough under "Install — Linux" in the setup repo's README.)  
  
**Launch the editor + install the addon.** Then:

```
..\..\sbox-dev.exe
```

Open any project, open the developer console, and run **once, ever**:

```
package_install ghage.claude-sbox tools
```

Restart the editor. From here on, every editor restart on every project automatically mounts the latest addon from a global cache at `<sbox-public>/game/.sbox-global/cloud/.bin/` — no redownload, works offline. The MCP host comes up automatically on `http://127.0.0.1:6790`.

# Connect Claude Code

**HTTP** (no bridge needed, easiest):

```
claude mcp add --transport http -s user sbox http://127.0.0.1:6790/mcp
```

If you run Claude Code inside a devcontainer, swap to `http://host.docker.internal:6790/mcp`. On Linux Docker engines you'll need `--add-host=host.docker.internal:host-gateway` on your container.  
  
**Stdio bridge** (Claude Desktop, Cline, anything that doesn't speak HTTP MCP):

```
claude mcp add --transport stdio -s user sbox node "$(pwd)/bridge/dist/bridge.js"
```

The bridge ships pre-built at `game/addons/claude-sbox-setup/bridge/dist/bridge.js` — single self-contained file, Node 20+, no `node_modules` at runtime.  
  
Once connected, run `claude mcp list` and look for `sbox    http://127.0.0.1:6790/mcp    Connected`.

# Install the companion skill

The setup repo ships an `sbox-live` workflow skill — routing guidance, common gotchas, anti-hallucination rules, Unity-to-s&box translation tables. Copying it into Claude Code's user-scope skill directory auto-loads it on s&box prompts so the agent knows when to reach for `editor_highlight` vs `invoke_menu` vs `set_preference`, which tools have `confirm:true` gates, what shapes the schema queries actually return, etc.  
  
From `<sbox-public>/game/addons/claude-sbox-setup/`:

```
# Linux / Mac / WSL
mkdir -p ~/.claude/skills && cp -r skill ~/.claude/skills/sbox-live

# Windows PowerShell
New-Item -ItemType Directory -Force "$HOME/.claude/skills" | Out-Null
Copy-Item -Recurse skill "$HOME/.claude/skills/sbox-live"
```

Skip this if you're using a different MCP client without skill support — the skill is Claude-Code-specific. You'll still get all ~597 tools; you just won't get the curated routing that keeps the model from guessing API shapes when it could be querying them.  
  
Contents:  
  
- `SKILL.md` — the router. "where is X?" → `editor_highlight`. "do X for me" → `invoke_menu` / `invoke_shortcut`. "set my editor to X" → `set_preference`.  
- `references/mcp-tools.md` — the canonical tool inventory with arg shapes and call patterns.  
- `references/unity-translation.md` — Unity to s&box anti-pattern table for ex-Unity devs.  
- `references/ten-rules.md` — cardinal rules the runtime silently enforces.  
- `references/gotchas.md` — surprises that survive a careful schema lookup.  
  
Re-sync after each `git pull` on the setup repo if the `skill/` tree changed — the Updating section below has the one-liner.

# Using it from the dock terminal

If you'd rather skip the host-side terminal entirely and drive the agent from inside `sbox-dev`:  
  
1. View → ClaudeSbox. A `cmd.exe` / `bash` prompt appears in the dock.  
2. Type `docker exec -it <your-container> bash` (or whatever drops you into your environment).  
3. Type `claude` and start a session.  
4. Claude Code reads `.mcp.json` from your sbox-public root and connects to the editor on `host.docker.internal:6790`.  
  
The setup repo ships a sample `.mcp.json` configuration and `bash bridge/scripts/check-setup.sh` that runs 7 readiness checks and reports PASS/FAIL.

# Example prompts

Things that work well as a first prompt:

> "Look at the active scene. What's selected? Spawn a citizen prefab at 0,0,0 and parent it under the selected GameObject."

The agent will pull `get_active_scene`, `get_selection`, `instantiate_prefab` (with `confirm:true` to actually instantiate), then `gameobject_set_parent`. You can watch each tool call land in the editor's Console dock as it happens.  
  
Other patterns:

> "I'm seeing flickering on the ground material at distance. Walk the LOD chain on `models/dev/dev_floor.vmdl` and look for missing distance entries.""Find every type that derives from `Sandbox.GameObject.Component` in this project's loaded assemblies and list them with their containing addon.""Compile this snippet against the project and tell me if it's missing a using directive: `public class Foo : Component { protected override void OnUpdate() => Log.Info(Time.Now); }`""Take a screenshot of the current scene view and save it next to the .sbproj as `latest.png`."

The `doctor` tool is the unified readiness probe — point the agent there if anything looks off; it'll tell you which subsystems are live and which are bootstrap-pending.

# Updating

Routine updates have a fixed order — engine → setup tooling → addon. The setup repo's README documents it under [Routine update procedure](https://github.com/coffeegrind123/claude-sbox-setup#routine-update-procedure), but the short version:

```
cd <sbox-public>\game\addons\claude-sbox-setup
git pull
.\Safe-Pull.bat
.\Bootstrap-And-Capture.bat
```

`Safe-Pull.bat` snapshots your state, reverts patches, pulls sbox-public, re-applies the patches, and verifies — all in one step, with a rollback path if anything fails. Don't use plain `git pull` from sbox-public root unless you know what you're doing; it'll blow up the patch state.  
  
The addon itself auto-updates from sbox.game on every project load via patch 4's global cache — no `package_install` re-run needed when a new version ships.  
  
If the `git pull` brought in `skill/` changes, refresh your installed skill:

```
Copy-Item "skill\SKILL.md" "$HOME/.claude/skills/sbox-live/SKILL.md" -Force
Copy-Item "skill\references\*" "$HOME/.claude/skills/sbox-live/references/" -Force -Recurse
```

Idempotent — re-running on an up-to-date skill is a no-op.

# Troubleshooting

- **`MSB3021: ... being used by another process`** **during Bootstrap** — lingering sbox-dev / VBCSCompiler / MSBuild / dotnet build-server. `Bootstrap-And-Capture.bat` detects and stops these automatically; if you ran the plain upstream `Bootstrap.bat` instead, run `.\Prepare-Bootstrap.bat -Yes` first.  
- **Editor launches but no** **`claude-sbox`** **tab in the dock** — either the engine patches didn't apply (re-run `.\Setup.bat`) or the addon isn't installed (re-run `package_install ghage.claude-sbox tools` in the dev console).  
- **MCP server connects but the agent gets "tool not found"** — hot-reload may have wiped the registration. The addon re-registers on `editor.created` + first frame; restart the editor or run `ping_addon_health`.  
- **Port 6790 already in use** — `netstat -ano | findstr :6790` to find the holder, kill it, restart sbox-dev.  
- **Whitelist errors at compile/mount time** — your sbox-public hasn't been patched. `.\Setup.bat` is idempotent; re-run it.  
  
The setup repo's README has a fuller failure-recovery table under [Routine update procedure → Failure recovery](https://github.com/coffeegrind123/claude-sbox-setup#failure-recovery), plus instructions for rolling back via `.\Restore-From-Backup.bat -List`.
