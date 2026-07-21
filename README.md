# pitchcraft-brand-refs

Authoritative Agentforce / Salesforce brand references vendored by the pitchcraft Claude skill.

📖 **Start here:** [docs/HOW-THE-SKILL-WORKS.md](docs/HOW-THE-SKILL-WORKS.md) — walkthrough of the whole system with reference screenshots from the VizVoice pitch.


The pitchcraft skill (`~/.claude/skills/pitchcraft/`) consumes this repo as a git submodule and reads:

- **`agentforce-brand-spec.md`** — the definitive written spec: colors, wordmark treatment, glass-pill motif, title lockup, brand-word rules, punctuation rules (no em dashes), audit expectations.
- **`assets/agentforce-icon-eb50.svg`** — the 2D one-color Agentforce icon (Electric Blue 50).
- **`assets/salesforce-logo-white.svg`** — official Salesforce horizontal KO logo (white on dark).
- **`assets/salesforce-cloud-white.svg`** — the SF cloud silhouette alone.
- **`templates/deck-template.html`** — the 10-slide brand-locked HTML deck scaffold.
- **`templates/copywriting-guide.md`** — how to write each slide's copy at judge-grade quality.
- **`templates/themes.md`** — five approved palettes + five approved font pairings.
- **`templates/narration-script.md`** — per-slide narration template with timing notes.
- **`scripts/fame_audit.py`** — Playwright layout audit (overflow / character-vs-type collision / text clipping).
- **`scripts/fame_typo.py`** — Playwright typography audit (font-loading, size ranges, contrast, wordmark treatment).

## Update flow

1. Change files here.
2. Commit + push.
3. In the pitchcraft skill dir, run `git submodule update --remote brand-refs` to pull the update.

The skill's `SKILL.md` cites the exact path within this submodule for every rule, so downstream pitches always resolve to the current commit of this repo.

## Non-negotiables (see the spec for the full list)

- **Electric Blue 30 (`#0D3DFF`)** is the mandatory Agentforce accent.
- **Agentforce is one word**; visible text ≥24px uses `<span class="af-mark">Agent<span class="af-f">f</span>orce</span>`.
- **Data Cloud** is the brand name. Never write "Data 360."
- **No em dashes** in visible deck copy.
- **Glass-pill motif** is reserved for the title-chip, reframe-lead, and close-eyebrow. Not scattered.
