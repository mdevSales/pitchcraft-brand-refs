# Pitchcraft · Copywriting Guide

How to write each slide's copy so a judge remembers it. Follow every rule. No filler, no jargon, no "we're excited to announce."

---

## Universal rules (apply to every slide)

1. **One idea per slide.** If you can name two things a slide is doing, split it.
2. **Say something specific.** "We help enterprises transform" → dead. "We let a blind analyst hear the same numbers a sighted one sees" → alive.
3. **Numbers > adjectives.** Not "faster," use "half the time." Not "many people," use "253 million."
4. **Cut every phrase you could remove without losing meaning.** "In today's world…" → cut. "We're proud to present…" → cut.
5. **Use `<em>italic</em>` in HTML only for the emotional beat.** Once per slide, maximum. That's the word the judge should feel.
6. **Read the slide aloud.** If you tripped over a phrase, rewrite it.
7. **Every sentence answers "so what?"** If a sentence doesn't advance the argument, cut it.
8. **No em dashes (—) in visible copy.** Use a period, comma, colon, or middle dot (`·`) instead. Em dashes read as an author's tic on screen and never survive narration cleanly. This applies to headlines, subtitles, body copy, and SVG a11y labels; code comments are fine.

---

## Slide 1 — Title

**Structure:**
- Eyebrow (top-left, small mono caps): the venue or context. Example: `AGENTFORCE FOR GOOD · BUILDER TRACK 2026`
- Wordmark (below eyebrow): the product name, big and confident in accent color.
- H1 (main headline, huge, 156px): a question or bold claim. Ends with a question mark or a period, never both, never neither.
  - GOOD: *"What if your analyst can't see your dashboard?"*
  - BAD: "Introducing VizVoice: The Future of Accessible Analytics"
- Subtitle (34px, secondary color): what the product does, in one sentence, plain English.
- Footer row: date + Salesforce logo (SVG, KO variant on dark palettes).

**Test:** Cover the wordmark. Does the H1 make someone lean in? If not, rewrite.

---

## Slide 2 — The scene

The moment the problem becomes real. NOT a statistic. A person.

**Structure:**
- Big quote-shaped copy, 96px, medium weight, italic-highlight one word: *"Half the room turns toward the screen. The other half has no idea what's on it."*
- Small caption below (mono caps, muted): where this happens. Example: `HAPPENS EVERY TUESDAY IN PRODUCT REVIEW`

**Do:** name the person, name what they were trying to do, name what broke.
**Don't:** describe an industry-wide problem in the abstract.

---

## Slide 3 — The number

One number. Absurdly big. Nothing else competes.

**Structure:**
- Hero number, 460px, gradient fill from white → accent.
- Caption (42px, secondary): what the number means. One sentence. NOT two.
  - GOOD: *"people worldwide with vision loss have zero independent access to these insights."*
  - BAD: "This is a huge problem that affects many people in many industries and we believe our solution can help."
- Context line (mono caps, muted): the source. `SOURCE: WHO 2024`.

**Do:** pick a number the audience knows how to picture (population of a country, dollars of a market, hours of a work-week).
**Don't:** put more than one number on this slide.

---

## Slide 4 — The critique

Why hasn't this been solved? Three tries, each named, each dismissed with a specific fact.

**Structure:**
- Eyebrow: `WHY EVERY EXISTING FIX FALLS SHORT` (or similar).
- Title (104px): the setup line. Ends on a colon.
- Three cards (grid), each with:
  - Card title (28px, accent color): the failed approach. `Alt text`, `Data tables`, `Screen readers`.
  - Body (20px, secondary): one sentence with a concrete failure mode.

**Do:** be specific about the failure. "Alt text goes stale within a sprint" beats "Alt text is often inaccurate."
**Don't:** attack competitors by name.

---

## Slide 5 — The reframe

The turn. One question that reframes the problem so the solution feels inevitable.

**Structure:**
- Eyebrow (mono caps): `A DIFFERENT QUESTION` or `THE REFRAME`.
- Main line, 152px, centered: the question. Italic-highlight the key noun.
  - GOOD: *"What if you didn't need to see the chart at all?"*
  - BAD: "How can we make dashboards more accessible?"
- Sub-line (poetic italic, 44px): the reframe stated as truth.
  - Example: *"Because the real insight isn't in the pixels. It's in the answer you're looking for."*

**This is the line judges are most likely to remember.** Spend the most time here.

---

## Slide 6 — The solution

What your product actually does. In plain English. With an architecture diagram if applicable.

**Structure:**
- Eyebrow: `HOW IT WORKS` or `THE PRODUCT`.
- H2 (96px): one sentence that starts with your product name.
  - GOOD: *"VizVoice turns any Tableau dashboard into a conversation."*
- Architecture diagram (SVG boxes with numbered steps): 4–5 stages, each numbered, tech stack tagged in mono caps below. Data hub in the middle (yellow accent) if you have one.

**Do:** call out the Salesforce pieces by name — Agentforce (one word), Data Cloud, Flow, Apex, Tableau, MuleSoft. Judges love the name-drops when they're accurate.
**Don't:** invent a stack you didn't build.

---

## Slide 7 — The proof (semantic model / trust / defensibility)

The technical bit that makes the product trustworthy or hard to copy. Optional but very strong.

**Structure:**
- Eyebrow: `WHY THIS WORKS` or `NOT SCREENSHOTS. NOT GUESSING.`
- Title (88px): the defensibility claim.
  - GOOD: *"The data a blind user hears comes from the exact same source a sighted user sees."*
- Sub (24px): one paragraph that names the mechanism.
- Visual: an entity diagram, live video clip, or a "one semantic model, two audiences" schematic.

---

## Slide 8 — How we built it (three or four layers)

Break the work into 3–4 layers. Each layer has: a label, a headline, a one-sentence description.

**Structure:**
- Eyebrow: `UNDER THE HOOD` or `THREE LAYERS OF DESIGN`.
- Title (104px): the shape of the work. Italic-highlight one word.
  - GOOD: *"Three deliberate <em>layers</em> of design."*
- Grid of 3 cards, each with:
  - Icon (SVG, gradient background circle).
  - Label (mono caps, accent): `LAYER 01 · THE AGENT`.
  - Headline (30px): the layer's tagline.
  - Body (18px, secondary): one sentence explaining what makes it good.
- Pillars row at the bottom (mono caps, 3 items): grounded / accessible / sustainable — or whatever your three anchors are.

**Do:** make each layer *distinct*. If two layers are about "the AI part," combine them.
**Don't:** list six things. Three or four, max.

---

## Slide 9 — The bigger idea (a better default)

The philosophical claim. Why this matters beyond the immediate use case.

**Structure:**
- Optional partnership chip (if you have one).
- H2 (124px): the thesis. Italic-highlight the payoff word.
  - GOOD: *"Accessibility isn't a <em>fallback.</em> It's a better <em>default.</em>"*
- Three columns of parallel claims, each with an H3 (40px, italic-highlight) + one-sentence body.
  - Column 1: `Voice is <em>faster</em>` — [one-liner why]
  - Column 2: `Keyboard is <em>universal</em>` — [one-liner why]
  - Column 3: `Numbers-first is <em>clearer</em>` — [one-liner why]

**Do:** make the three columns *parallel*. Same grammatical structure, same length.
**Don't:** put a call-to-action here. This is the ideology slide, not the ask slide.

---

## Slide 10 — Close (team + one line)

The last thing on screen. Simple, human, memorable.

**Structure:**
- Close eyebrow (mono caps, accent): `BUILT IN TWO WEEKS · TEAM OF THREE` or similar credentials.
- Close headline (168px): the one line the judges should remember. Italic-highlight the emotional word.
  - GOOD: *"Voice-first, so <em>every</em> user hears the same story."*
  - BAD: "Thank you for your time and consideration."
- Sub (34px): a one-sentence coda.
- Footer row: team names + circular photos (140px circles, accent border), then Salesforce logo.

**Do:** show the team's faces. Judges vote for people, not products.
**Don't:** end on "Q&A?" — a repeat of the wordmark or the one line is stronger.

---

## Voice: how to write ALL copy

- **Contract everything.** "It's," "we're," "you'll," never "it is," "we are," "you will."
- **Say "you" not "the user."** Even in an internal pitch.
- **Cut adverbs.** "Really important" → "matters." "Very fast" → "instant."
- **Use one word Salesforce brand words correctly:**
  - **Agentforce** (one word, capital A).
  - **Data Cloud** (two words, both capitalized). NEVER "Data 360" unless the user explicitly said so.
  - **Flow** (capitalized when referring to Salesforce Flow).
  - **Apex** (capitalized).
  - **Tableau** (capitalized).
- **Never say:** "revolutionary," "disruptive," "cutting-edge," "next-gen," "game-changer," "leverage" (as a verb), "unlock" (as a verb), "unleash," "empower," "seamless."

---

## Length ceilings (never exceed)

| Element | Max words |
|---|---|
| Title H1 (slide 1) | 10 |
| Scene quote (slide 2) | 25 |
| Stat caption (slide 3) | 20 |
| Critique card body | 20 |
| Reframe main line (slide 5) | 12 |
| Reframe sub-line | 20 |
| Solution H2 | 12 |
| Built-item body | 30 |
| Better-item body | 20 |
| Close headline | 12 |

If you're over the ceiling, cut. Every time.

---

## Brand mechanics (baked into the template — do not fight these)

### The Agentforce wordmark

Any time the product **Agentforce** appears in visible copy at ~24px or larger (headlines, footer chip, in-deck references), wrap the "f" in the wordmark treatment so it echoes the official lockup:

```html
<span class="af-mark">Agent<span class="af-f">f</span>orce</span>
```

The template provides `.af-mark .af-f { transform: skewX(-11deg); }` so the "f" inherits the sans family and picks up a faux-italic. Do **not** apply this to eyebrow-size text (≤ 15px) — the skew reads as a typo at that size. Do **not** switch to Cormorant italic; the official wordmark is sans.

### The Agentforce brand chip on the title slide

The title header pairs the Salesforce logo with the Agentforce 2D icon, separated by a thin divider:

```html
<div class="title-brand-group">
    <span class="sf-logo">…Salesforce SVG…</span>
    <span class="brand-divider"></span>
    <span class="af-icon"><img src="assets/agentforce-icon-eb50.svg" alt="Agentforce"></span>
</div>
```

Keep this lockup unless the user explicitly says the deck is not Agentforce-flavored (rare in a Salesforce hackathon).

### The glass pill motif

Eyebrow-analog labels on the **title chip**, the **reframe lead**, and the **close eyebrow** carry the `.pill` class:

```html
<div class="reframe-lead pill reveal">The reframe</div>
<div class="close-eyebrow pill">This is a solved problem</div>
```

The template ships the brand-spec shadow (`0 26px 26px rgba(6,106,254,0.30)`) and 40px backdrop blur. Do not add pills anywhere else without a reason — they lose meaning if scattered.

### Brand words (say them right, always)

- **Agentforce** — one word, capital A. Never "Agent Force," never "AgentForce."
- **Data Cloud** — two words, both capitalized. **Never write "Data 360" as a brand name** unless the user explicitly asked for it.
- **Flow**, **Apex**, **Tableau**, **MuleSoft**, **Slack**, **Experience Cloud** — capitalized when referring to the Salesforce product.

