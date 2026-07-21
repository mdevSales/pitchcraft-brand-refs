# Pitchcraft Themes

The user picks ONE background palette and ONE font pairing during discovery. Both plug into CSS custom properties at the top of the deck. All options stay on-brand for Salesforce; they change the mood, not the identity.

**Brand constant.** Every palette keeps `--sf-electric-30: #0D3DFF` (the mandatory Agentforce accent) reachable. Palettes may override `--sf-cloud-68` for the mood accent, but the Agentforce brand ink stays available for glass-pill shadows, wordmark treatments, and icon fills.

---

## Background palettes

Each palette defines: `--stage-bg`, `--slide-bg`, `--sf-electric-15` (deep anchor), the atmosphere orb tints, and text roles.

### 1. `midnight-cloud` (default — the VizVoice look)
- Deep navy anchor with Cloud Blue signature accent.
- Feels: cinematic, trustworthy, product-launch.
- Best for: enterprise + trust stories, security, data.

```css
--stage-bg:      #000516;
--slide-bg:      #001E5B;   /* electric-15 */
--sf-cloud-68:   #00B3FF;   /* accent */
--text-primary:  #ffffff;
--text-secondary:#a8c5f5;
--text-muted:    #5b7ba8;
/* orbs: cloud (900px) + electric (700px) + royal (620px) */
```

### 2. `dawn-cloud`
- Off-white paper anchor with Cloud Blue + Ocean accents. Bright, editorial.
- Feels: optimistic, human-centered, magazine cover.
- Best for: healthcare, education, sustainability.

```css
--stage-bg:      #F7FAFF;
--slide-bg:      #FFFFFF;
--sf-cloud-68:   #066AFE;   /* accent */
--text-primary:  #001E5B;
--text-secondary:#3a5c8f;
--text-muted:    #8095b8;
/* orbs on white: cloud-95 (huge, low opacity) + yellow (medium) */
```

### 3. `sunset-gold`
- Deep royal + Trailhead gold. Warm, energetic, celebratory.
- Feels: launch, milestone, "the customer story."
- Best for: customer success, growth, activation.

```css
--stage-bg:      #0A0824;
--slide-bg:      #17114B;
--sf-cloud-68:   #FCC003;   /* accent — Trailhead gold */
--text-primary:  #FFF9E6;
--text-secondary:#DDD1FF;
--text-muted:    #7D6DB0;
/* orbs: yellow (bigger) + electric + pink */
```

### 4. `ocean-teal`
- Cool teal + Cloud Blue. Serene, technical, science-adjacent.
- Feels: scientific, exploratory, deep-tech.
- Best for: AI/ML research, data platforms, developer tools.

```css
--stage-bg:      #001A1F;
--slide-bg:      #003D4A;
--sf-cloud-68:   #04E1CB;   /* accent — teal-80 */
--text-primary:  #E5FDFA;
--text-secondary:#8EDBD3;
--text-muted:    #52807B;
/* orbs: teal (900) + cloud + violet */
```

### 5. `dusk-violet`
- Violet + Cloud Blue over deep indigo. Playful, creative.
- Feels: creative, media, generative AI.
- Best for: creative agencies, marketing, generative products.

```css
--stage-bg:      #0F0426;
--slide-bg:      #1F1050;
--sf-cloud-68:   #D17DFE;   /* accent — violet-65 */
--text-primary:  #FBF3FF;
--text-secondary:#CDB6EE;
--text-muted:    #7B5FA8;
/* orbs: violet (900) + cloud + pink */
```

---

## Font pairings

Each pairing is exactly three roles: `--font-display` (headlines, big numbers), `--font-body` (copy), `--font-poetic` (italic emphasis, pull-quotes), plus a mono for eyebrow labels.

### 1. `manrope-cormorant` (default — the VizVoice look)
- Display / Body: **Manrope** (300–800). Geometric humanist, stands in cleanly for Salesforce Sans.
- Poetic: **Cormorant** italic 400/500. Delicate serif, only used for emotional beats.
- Mono: **IBM Plex Mono** 400/500. Eyebrow labels, timecodes.
- Feels: modern, cinematic, editorial-tech.

### 2. `inter-playfair`
- Display / Body: **Inter** (300–800). Screen-optimized, warm.
- Poetic: **Playfair Display** italic 500. Broad-shouldered serif, feels newspaper.
- Mono: **JetBrains Mono** 400. Deep techy accent.
- Feels: newsroom, thought-leader, "opinion piece."

### 3. `outfit-instrument`
- Display / Body: **Outfit** (300–800). Geometric, slightly quirky, product-launch energy.
- Poetic: **Instrument Serif** italic 400. High-contrast display serif — bold pull quotes.
- Mono: **Space Mono** 400. Retro-terminal accent.
- Feels: startup keynote, "we're the fresh face."

### 4. `figtree-fraunces`
- Display / Body: **Figtree** (300–800). Rounded, approachable.
- Poetic: **Fraunces** italic 400 (opsz "soft"). Modern serif with personality.
- Mono: **DM Mono** 400. Friendly mono.
- Feels: consumer-friendly, warm, D2C.

### 5. `space-grotesk-crimson`
- Display / Body: **Space Grotesk** (300–700). Neo-grotesque, precise.
- Poetic: **Crimson Pro** italic 500. Editorial serif, sober.
- Mono: **JetBrains Mono** 400.
- Feels: dev-tools, dense technical, "we built this from first principles."

---

## Google Fonts import strings (paste into `<head>`)

```html
<!-- manrope-cormorant -->
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&family=Cormorant:ital,wght@1,400;1,500&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">

<!-- inter-playfair -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@1,500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">

<!-- outfit-instrument -->
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@1&family=Space+Mono&display=swap" rel="stylesheet">

<!-- figtree-fraunces -->
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500;600;700;800&family=Fraunces:ital,opsz,wght@1,144,400&family=DM+Mono&display=swap" rel="stylesheet">

<!-- space-grotesk-crimson -->
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Crimson+Pro:ital,wght@1,500&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
```

---

## When rendering, apply the theme like this

At the top of `<style>`:

```css
:root {
    /* --- PALETTE (from user pick) --- */
    --stage-bg:       {{palette.stage-bg}};
    --slide-bg:       {{palette.slide-bg}};
    --sf-cloud-68:    {{palette.accent}};   /* accent */
    --sf-cloud-80:    {{palette.accent-soft}};
    --sf-cloud-95:    {{palette.accent-wash}};
    --sf-yellow-80:   #FCC003;              /* always available for chip highlights */
    --text-primary:   {{palette.text-primary}};
    --text-secondary: {{palette.text-secondary}};
    --text-muted:     {{palette.text-muted}};

    /* --- FONTS (from user pick) --- */
    --font-display:   '{{fonts.display}}', -apple-system, sans-serif;
    --font-body:      '{{fonts.body}}', -apple-system, sans-serif;
    --font-mono:      '{{fonts.mono}}', monospace;
    --font-poetic:    '{{fonts.poetic}}', serif;
}
```

Then adjust the `.orb-*` background gradients to use the palette's accent tint. Everything else in the template inherits automatically.
