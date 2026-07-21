# Agentforce / Salesforce Brand Spec for Pitchcraft

Authoritative reference for the pitchcraft skill. Everything here is derived from the Agentforce brand guideline materials shared by the pitch team; the pitchcraft skill vendors this repo as a git submodule and reads these rules at scaffold time.

If a rule below conflicts with an older screenshot or a partner deck, this doc wins.

---

## 1. Color

### Core palette (mandatory)

| Token | Hex | Purpose |
|---|---|---|
| `--sf-electric-15` | `#001E5B` | Deepest navy. Slide anchor / dark backgrounds. |
| `--sf-electric-30` | `#0D3DFF` | **Primary Agentforce Electric Blue accent.** Use for glass-pill shadows, wordmark strokes, and icon fills. Mandatory presence on any Agentforce-flavored slide. |
| `--sf-electric-50` | `#2E5BFF` | Mid Electric Blue. Icon fills, secondary accents. |
| `--sf-cloud-68` | `#00B3FF` | Cloud Blue signature. Mood accent (may be overridden per theme). |
| `--sf-cloud-80` | `#90D0FE` | Cloud tint for softer surfaces. |
| `--sf-cloud-95` | `#EAF5FE` | Wash / paper. |

### Secondary accents (theme-scoped)

| Token | Hex | Use |
|---|---|---|
| `--sf-yellow-80` | `#FCC003` | Trailhead gold. Data-loop callouts, highlight moments. |
| `--sf-teal-60` | `#06A59A` | Ocean theme accent. |
| `--sf-teal-80` | `#04E1CB` | Ocean-mood signature. |
| `--sf-pink-60` | `#FF538A` | Emphasis chip in warm palettes. |
| `--sf-violet-65` | `#D17DFE` | Dusk-violet theme accent. |

### Contrast rules

- White text on `--sf-electric-15` or `--sf-electric-30` must render at ≥4.5:1 for body copy, ≥3:1 for large display.
- Never place `--sf-electric-30` text on `--sf-electric-15` (fails contrast). Use white or `--sf-cloud-80` instead.

---

## 2. Typography

### The Agentforce wordmark

The official Agentforce lockup uses a sans italic "f" inside an otherwise-upright sans wordmark. Avant Garde Italic is not web-available, so pitchcraft synthesizes it via CSS:

```html
<span class="af-mark">Agent<span class="af-f">f</span>orce</span>
```

```css
.af-mark { font-family: inherit; font-weight: inherit; }
.af-mark .af-f {
    font-family: inherit;
    font-weight: inherit;
    font-style: normal;
    color: inherit;
    display: inline-block;
    transform: skewX(-11deg);
    transform-origin: 0 100%;
    padding: 0 0.04em 0 0.02em;
}
```

Rules:
- Apply the mark whenever "Agentforce" appears at ≥24px.
- Never render the italic "f" in Cormorant or any serif — the wordmark stays sans.
- Never use the mark at eyebrow-size (≤15px). At small sizes the skew reads as a typo.

### Font pairings (five approved)

| Pairing | Display | Body | Poetic (italic) | Mono (labels) |
|---|---|---|---|---|
| `manrope-cormorant` **(default)** | Manrope 300–800 | Manrope 400 | Cormorant italic 400/500 | IBM Plex Mono 400/500 |
| `inter-playfair` | Inter | Inter | Playfair Display italic 500 | JetBrains Mono 400 |
| `outfit-instrument` | Outfit | Outfit | Instrument Serif italic 400 | Space Mono 400 |
| `figtree-fraunces` | Figtree | Figtree | Fraunces italic 400 | DM Mono 400 |
| `space-grotesk-crimson` | Space Grotesk 300–700 | Space Grotesk 400 | Crimson Pro italic 500 | JetBrains Mono 400 |

### Type roles

| Role | Size range (px) | Line height | Where |
|---|---|---|---|
| Hero | 72–520 | 0.82–1.25 | Title H1, stat hero, close headline |
| Headline | 44–120 | 0.95–1.30 | h2 on non-title slides, critique title, reframe main |
| Sub | 22–90 | 1.05–1.55 | Subtitles, lead paragraphs, display quotes |
| Body | 14–34 | 1.10–1.95 | Paragraph copy, card bodies |
| Mono | 10–22 | 1.20–1.90 | Eyebrows, labels, footnotes, step tags |

All-caps mono labels must carry letter-spacing ≥0.08em.

### Emphasis with `<em>`

- Reserved for the emotional beat, once per slide maximum.
- Renders in the theme's poetic italic (`--font-poetic`).
- Do not italicize proper product names ("Agentforce," "Data 360"). Use the wordmark treatment instead.

---

## 3. The glass-pill motif

Applied to three eyebrow-analog elements only:

1. The **title-slide context chip** (right side of the title header).
2. The **reframe lead** (`.reframe-lead.pill`, slide 5).
3. The **close eyebrow** (`.close-eyebrow.pill`, slide 10).

### Exact spec

```css
.pill {
    display: inline-block;
    padding: 14px 28px;
    background: rgba(255, 255, 255, 0.20);
    backdrop-filter: blur(40px) saturate(1.1);
    -webkit-backdrop-filter: blur(40px) saturate(1.1);
    border: 1px solid rgba(255, 255, 255, 0.28);
    border-radius: 999px;
    box-shadow:
        0 26px 26px rgba(6, 106, 254, 0.30),
        inset 0 1px 0 rgba(255, 255, 255, 0.35);
    color: #ffffff;
    font-size: 16px;
    letter-spacing: 0.28em;
}
```

Notes:
- Shadow color is `#066AFE @ 30%` (Electric Blue signature glow), not the palette accent.
- On light backgrounds the text color flips to `--sf-electric-15`; the shadow softens to `rgba(6, 106, 254, 0.18)`.
- Do not stack pills. Do not add pills to random labels.

---

## 4. The title-slide lockup

Every Agentforce-flavored deck opens with the Salesforce cloud + hairline divider + Agentforce icon lockup in the top-left, and the glass-pill context chip on the right:

```html
<div class="title-header reveal">
    <span class="title-brand-group">
        <span class="sf-logo"><img src="assets/salesforce-logo-white.svg" alt="Salesforce"></span>
        <span class="brand-divider" aria-hidden="true"></span>
        <span class="af-icon"><img src="assets/agentforce-icon-eb50.svg" alt="Agentforce"></span>
    </span>
    <span class="brand-mark pill">Venue · Context</span>
</div>
```

- `.sf-logo img` height: 44px.
- `.af-icon img` height: 40px.
- `.brand-divider`: 1px wide, 28px tall, `rgba(255,255,255,0.28)`.

---

## 5. The Agentforce 2D icon (`agentforce-icon-eb50.svg`)

One-color face with sunglasses and two ears. Ships in this repo under `assets/agentforce-icon-eb50.svg`.

Rules:
- Use only the 2D one-color version at title-slide scale (≤48px tall).
- Do not tint below Electric Blue 30. On white backgrounds, use the negative variant (invert to `--sf-electric-15`).
- Do not combine the icon with the Astro character in the same lockup. Astro is a separate treatment.

---

## 6. Voice and copy

### Brand words

- **Agentforce** — one word, capital A. Never "Agent Force." Never "AgentForce."
- **Data 360** — the current Salesforce brand name (rebranded from Data Cloud). Always written "Data 360" in visible copy. **Narration rule:** say "Data three sixty," never "Data three hundred sixty."
- **Flow**, **Apex**, **Tableau**, **MuleSoft**, **Slack**, **Experience Cloud** — capitalized when referring to the Salesforce product.

### Punctuation

- **No em dashes (—) in visible deck copy.** Use commas, periods, colons, or the middle dot `·`. Applies to headlines, subtitles, body copy, and SVG a11y labels. Code comments are fine.
- Middle dot `·` is the preferred separator in eyebrow strings ("For FAME · Prepared by Salesforce").
- Avoid semicolons in headlines; use two sentences instead.

### Rhetorical constraints

- Numbers before adjectives. "Half the time," not "faster."
- One idea per slide. If you can name two, split.
- Cut every phrase you could remove without losing meaning.
- Never use: "revolutionary," "disruptive," "cutting-edge," "next-gen," "game-changer," "leverage" (verb), "unlock" (verb), "unleash," "empower," "seamless."

---

## 7. Layout and motion

- Every slide is fixed 1920×1080. The `.deck-stage` scales to viewport via `transform: scale(...)` from `transform-origin: 0 0`.
- Reveal animations are limited: `opacity 0→1` + `translateY(28px→0)` for `.reveal`, plus a slower blur-in for `.reveal-slow` on hero stats.
- Never animate more than six items per slide.
- `prefers-reduced-motion` cuts durations to 200ms globally.

---

## 8. Layout + typography audit

Two Playwright scripts live under `scripts/`. Run them from a project deck to verify brand compliance before recording video:

- `scripts/fame_audit.py` — checks every slide element for overflow, character/type collision, and text clipping.
- `scripts/fame_typo.py` — checks font loading, size ranges, line-height ratios, all-caps tracking, contrast, widow risk, and the Agentforce wordmark treatment (verifies `.af-f` inherits sans and carries a `skewX` transform).

Both write reports to `/tmp/fame_audit/` and `/tmp/fame_typo/` respectively. A brand-compliant deck should return `Total problems: 0` from both.

---

## Version

Spec revision: 2026-07 (post-FAME servicing deck polish).
Origin: Agentforce brand guideline materials + Electric Blue 30 mandate + glass-pill Figma spec.
