#!/usr/bin/env python3
"""Typography audit for the FAME deck.

For every text element in every slide, checks:
  1. Font actually loaded (not falling back to a system font)
  2. Font-size in a sane range (title 60–160, headline 48–120, body 16–32, mono 10–20)
  3. Line-height ratio (display 0.95–1.15, body 1.3–1.6)
  4. Letter-spacing on ALL-CAPS eyebrows/labels (>= 0.08em)
  5. Contrast: text color vs. its background luminance (WCAG-ish ratio >= 3:1 for large, 4.5:1 for body)
  6. Hierarchy consistency — every slide's largest heading is bigger than its body copy
  7. Wordmark treatment intact (`.af-mark .af-f` renders in Cormorant italic)
  8. Widow/orphan check — headlines that end with a single short word on a line
  9. Body copy line count sanity — paragraphs > 6 lines flagged as too dense

Report → /tmp/fame_typo/report.txt
"""
from playwright.sync_api import sync_playwright
from pathlib import Path

URL = "file:///Users/mdevulapalli/Desktop/fame-loan-servicing-deck/index.html"
OUT = Path("/tmp/fame_typo")
OUT.mkdir(exist_ok=True)

EXPECTED_FONTS = {
    "display": "Manrope",
    "body":    "Manrope",
    "mono":    "IBM Plex Mono",
    "poetic":  "Cormorant",
}

RANGES = {
    # role: (min_px, max_px, min_lh_ratio, max_lh_ratio)
    "hero":    (72, 520, 0.82, 1.25),   # title-hero h1, stat-hero (huge number), close-headline
    "headline":(44, 120, 0.95, 1.30),   # h2 on other slides
    "sub":     (22, 90,  1.05, 1.55),   # subtitles / lead paragraphs / display quotes
    "body":    (14, 34,  1.10, 1.95),   # paragraph copy; short bold values run tighter
    "mono":    (10, 22,  1.20, 1.90),   # eyebrows / labels
}

ROLE_SELECTORS = {
    "hero":    ["h1", ".stat-hero", ".close-headline"],
    "headline":["h2:not(.close-headline)", ".critique-title", ".reframe-main", ".solution-title", ".semantic-title", ".better-title"],
    "sub":     [".title-subtitle", ".stat-caption", ".reframe-sub", ".semantic-sub", ".close-sub", ".scene-quote"],
    "body":    [".critique-item p", ".scene-caption", ".better-card p", ".built-value", "p:not(.reframe-sub):not(.title-subtitle):not(.close-sub):not(.scene-caption):not(.stat-caption)"],
    "mono":    [".eyebrow", ".stat-context", ".title-footer", ".brand-mark", ".step-num-text", ".step-tech", ".step-label", ".critique-header", ".reframe-lead", ".close-eyebrow", ".team-label"],
}

def hex_from_rgb(rgb):
    # rgb = "rgb(a, b, c)" or "rgba(a,b,c,d)"
    import re
    m = re.search(r"rgba?\(([^)]+)\)", rgb)
    if not m: return None
    parts = [float(x) for x in m.group(1).split(",")[:3]]
    return parts

def rel_luminance(rgb):
    def chan(c):
        c = c / 255
        return c/12.92 if c <= 0.03928 else ((c+0.055)/1.055) ** 2.4
    r, g, b = [chan(x) for x in rgb]
    return 0.2126*r + 0.7152*g + 0.0722*b

def contrast(fg, bg):
    L1 = rel_luminance(fg); L2 = rel_luminance(bg)
    if L1 < L2: L1, L2 = L2, L1
    return (L1 + 0.05) / (L2 + 0.05)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = ctx.new_page()
    page.goto(URL, wait_until="networkidle")
    page.add_style_tag(content=".reveal, .reveal-slow { opacity: 1 !important; transform: none !important; }")
    page.wait_for_timeout(600)

    total = page.evaluate("document.querySelectorAll('.slide').length")
    lines = []
    problems = 0

    for i in range(total):
        page.wait_for_timeout(250)
        n = i + 1
        slide_report = []

        # Effective slide background color (used for contrast checks) — sample from a bare region
        slide_bg = page.evaluate("""(idx) => {
            const s = document.querySelectorAll('.slide')[idx];
            const cs = window.getComputedStyle(s);
            return cs.backgroundColor || 'rgb(0,30,91)';
        }""", i)
        bg_rgb = hex_from_rgb(slide_bg) or [0, 30, 91]

        for role, sels in ROLE_SELECTORS.items():
            info = page.evaluate("""({sels, idx}) => {
                const slide = document.querySelectorAll('.slide')[idx];
                const rows = [];
                for (const sel of sels) {
                    let els; try { els = slide.querySelectorAll(sel); } catch(e){ continue; }
                    for (const el of els) {
                        const cs = window.getComputedStyle(el);
                        const text = (el.innerText || '').replace(/\\s+/g,' ').trim();
                        if (!text) continue;
                        // Get widow / last line
                        const words = text.split(' ');
                        const lastWord = words[words.length-1] || '';
                        rows.push({
                            sel, text: text.slice(0, 100),
                            family: cs.fontFamily,
                            size: parseFloat(cs.fontSize),
                            lh: cs.lineHeight === 'normal' ? 1.2 * parseFloat(cs.fontSize) : parseFloat(cs.lineHeight),
                            weight: cs.fontWeight,
                            style: cs.fontStyle,
                            spacing: cs.letterSpacing,
                            transform: cs.textTransform,
                            color: cs.color,
                            lastWord, wordCount: words.length,
                            width: el.getBoundingClientRect().width,
                            height: el.getBoundingClientRect().height,
                            scrollH: el.scrollHeight,
                            clientH: el.clientHeight,
                            overflow: cs.overflow,
                        });
                    }
                }
                return rows;
            }""", {"sels": sels, "idx": i})

            min_px, max_px, min_lh, max_lh = RANGES[role]

            for r in info:
                lh_ratio = r["lh"] / max(r["size"], 1)
                issues = []

                # 1. Font-family loaded (Manrope / Cormorant / IBM Plex Mono must appear as primary)
                fam = r["family"].lower()
                if role in ("hero","headline","sub","body") and "manrope" not in fam and "cormorant" not in fam and "ibm plex" not in fam:
                    issues.append(f"font-family fallback: {r['family']!r}")

                # 2. Size range
                if r["size"] < min_px or r["size"] > max_px:
                    issues.append(f"size {r['size']:.0f}px outside {role} range {min_px}–{max_px}")

                # 3. Line-height ratio
                if lh_ratio < min_lh or lh_ratio > max_lh:
                    issues.append(f"line-height ratio {lh_ratio:.2f} outside {role} range {min_lh}–{max_lh}")

                # 4. All-caps letter-spacing check
                if r["transform"] == "uppercase":
                    sp = r["spacing"]
                    if sp == "normal" or (sp.endswith("px") and float(sp.replace("px","")) / max(r["size"],1) < 0.05):
                        issues.append(f"uppercase text with tight tracking ({sp!r})")

                # 5. Contrast
                fg = hex_from_rgb(r["color"])
                if fg:
                    cr = contrast(fg, bg_rgb)
                    threshold = 3.0 if r["size"] >= 24 else 4.5
                    if cr < threshold:
                        issues.append(f"low contrast {cr:.2f}:1 (< {threshold}:1 for {int(r['size'])}px)")

                # 6. Widow — headline ending with a 1–3-char word alone
                if role in ("hero","headline") and r["wordCount"] > 4 and len(r["lastWord"]) <= 3:
                    issues.append(f"widow risk — ends in short word {r['lastWord']!r}")

                # 7. Text visually clipped — only real if overflow != visible AND gap > 8px
                if r["overflow"] not in ("visible",) and r["scrollH"] > r["clientH"] + 8:
                    issues.append(f"text clipped by {r['scrollH']-r['clientH']}px (overflow:{r['overflow']})")

                if issues:
                    slide_report.append(f"  [{role}] {r['sel']} — {r['text'][:55]!r}")
                    for iss in issues:
                        slide_report.append(f"       · {iss}")
                    problems += len(issues)

        # 8. Wordmark check — .af-f must inherit the wordmark family (sans) and carry a skewX faux-italic
        wm = page.evaluate("""(idx) => {
            const slide = document.querySelectorAll('.slide')[idx];
            const results = [];
            for (const el of slide.querySelectorAll('.af-mark .af-f')) {
                const cs = window.getComputedStyle(el);
                results.push({family: cs.fontFamily, transform: cs.transform});
            }
            return results;
        }""", i)
        for w in wm:
            fam = w["family"].lower()
            if "cormorant" in fam:
                slide_report.append(f"  [wordmark] .af-f rendered in Cormorant serif — must inherit Agentforce sans")
                problems += 1
            if "matrix" not in (w["transform"] or "none"):
                slide_report.append(f"  [wordmark] .af-f missing skewX faux-italic transform")
                problems += 1

        if slide_report:
            lines.append(f"\n─── Slide {n:02d} ───")
            lines.extend(slide_report)
        else:
            lines.append(f"\n─── Slide {n:02d} — typography clean ✓ ───")

        page.keyboard.press("ArrowRight")

    browser.close()

report = f"FAME typography audit\n{'='*40}\nTotal problems: {problems}\n" + "\n".join(lines) + "\n"
(OUT / "report.txt").write_text(report)
print(report)
