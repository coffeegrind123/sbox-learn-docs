#!/usr/bin/env node
/*
 * defender_bridge.mjs — long-lived stdin/stdout JSONL host for
 * @stackone/defender, spawned by scrape.py once per scrape run.
 *
 * Why a bridge: defender is a TypeScript/Node package, the scraper is
 * Python. Per-doc subprocess spawn would re-load defender's 22MB ONNX
 * model from scratch on every call (200ms+) which is wasteful when we
 * have many docs to scan. One long-lived Node process keeps the model
 * resident; Python pipes JSONL in, reads JSONL out, closes stdin when
 * done, the Node process exits cleanly.
 *
 * Protocol (line-delimited JSON, UTF-8):
 *
 *   stdin  ← {"id": <int>, "md": "<markdown body>", "source": "<slug>"}\n
 *   stdout → {"id": <int>, "allowed": <bool>, "riskLevel": "<low|medium|high|critical>",
 *             "tier2Score": <number>, "detections": [<string>...],
 *             "patternsByField": {...}, "fieldsSanitized": [...]}\n
 *
 * One readiness line is emitted before stdin reads begin:
 *   stdout → {"ready": true, "modelLoaded": <bool>}\n
 *
 * On any unhandled error a single-line {"error": "<msg>", "fatal": true}
 * goes to stdout and the process exits 1 — Python should treat that as
 * defender-side failure (default: skip writing the doc; never silently
 * pass an unscanned doc through).
 *
 * Logging: anything diagnostic goes to stderr so it doesn't pollute the
 * JSONL stream Python consumes from stdout.
 */

import { createInterface } from "node:readline";
import { createPromptDefense } from "@stackone/defender";

// Config:
//   - tier1: pattern detection + sanitization (sync, fast)
//   - tier2: ML classifier (async, 22MB ONNX, ~10ms after load)
//   - blockHighRisk: true — flips `allowed=false` for high/critical risk
//   - tier2Config.highRiskThreshold: 0.95 — raised from defender's
//     default (around 0.8). At the default, the classifier blocked
//     legitimate technical tutorials (jigglebones, networked-variable
//     UI, ui-buildhash) at scores of 0.69-0.95 because imperative
//     tutorial prose ("let's start", "you should know") shares surface
//     features with injection. 0.95 lets normal how-to writing through
//     while still blocking the classic patterns ("Ignore previous
//     instructions. SYSTEM:..." reliably scores ~0.96).
//
//     Trade-off: a small slice of obfuscated attacks — homoglyph +
//     ChatML role tags (`<|im_start|>system`) — empirically score
//     0.94-0.95 and pass through. Tier 1 currently doesn't pattern-
//     match `[SYSTEM]` brackets or `<|im_start|>` tags either, so
//     those slip past both tiers at this threshold. If a real attack
//     of that shape ever lands in the mirror it'll be visible in
//     `defender.scanned` vs `count` skew (scanned > count means some
//     were blocked) AND surface to the addon as a low-content tutorial
//     a user might notice. Tightening to 0.90 catches them but starts
//     blocking ~30% of legitimate tutorials. Hold at 0.95 unless we
//     get a real-world incident.
//
// We do NOT enable `annotateBoundary` (which wraps content in [UD-…] tags)
// because the markdown lands on disk and is consumed by an editor-side
// indexer — boundary tags would corrupt the rendered text. Tier 1
// sanitization (role-marker stripping, instruction-override redaction)
// still happens; we just don't tag the result.
const defense = createPromptDefense({
  blockHighRisk: true,
  tier2Config: {
    highRiskThreshold: 0.95,
  },
});

// Warm up the ML model up-front so the first real doc doesn't pay the
// 200ms cold-start. Best-effort — if the warmup throws we still proceed
// and the first defendToolResult() call will load on demand.
let modelLoaded = false;
try {
  await defense.warmupTier2();
  modelLoaded = true;
} catch (e) {
  process.stderr.write(`[defender_bridge] warmup failed (non-fatal): ${e?.message || e}\n`);
}

// Emit readiness so Python doesn't race the first write.
process.stdout.write(JSON.stringify({ ready: true, modelLoaded }) + "\n");

const rl = createInterface({ input: process.stdin });

rl.on("line", async (raw) => {
  if (!raw.trim()) return;
  let req;
  try {
    req = JSON.parse(raw);
  } catch (e) {
    process.stdout.write(
      JSON.stringify({ id: null, error: `bad json: ${e?.message || e}` }) + "\n",
    );
    return;
  }

  const id = req.id ?? null;
  const md = req.md;
  const source = req.source ?? "tutorial";

  if (typeof md !== "string") {
    process.stdout.write(
      JSON.stringify({ id, error: "missing or non-string `md` field" }) + "\n",
    );
    return;
  }

  try {
    // The source identifier shows up in defender's structured detections
    // (e.g. patternsByField keys). Use the tutorial slug so blocked-doc
    // logs back in Python read naturally.
    const result = await defense.defendToolResult(md, source);
    process.stdout.write(
      JSON.stringify({
        id,
        allowed: result.allowed,
        riskLevel: result.riskLevel,
        tier2Score: result.tier2Score ?? null,
        detections: result.detections ?? [],
        patternsByField: result.patternsByField ?? {},
        fieldsSanitized: result.fieldsSanitized ?? [],
      }) + "\n",
    );
  } catch (e) {
    process.stdout.write(
      JSON.stringify({
        id,
        error: `defendToolResult threw: ${e?.message || e}`,
      }) + "\n",
    );
  }
});

// Stdin closes => Python is done; exit cleanly.
rl.on("close", () => {
  process.exit(0);
});

// Surface unexpected crashes so Python sees them and can abort the scrape
// instead of silently letting unscanned docs through.
process.on("uncaughtException", (err) => {
  process.stdout.write(
    JSON.stringify({ error: `uncaughtException: ${err?.message || err}`, fatal: true }) + "\n",
  );
  process.exit(1);
});
process.on("unhandledRejection", (err) => {
  process.stdout.write(
    JSON.stringify({ error: `unhandledRejection: ${err?.message || err}`, fatal: true }) + "\n",
  );
  process.exit(1);
});
