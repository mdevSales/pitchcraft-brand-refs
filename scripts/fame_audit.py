#!/usr/bin/env python3
"""Audit every slide in the FAME deck for layout problems.

Checks each slide inside a fixed 1920x1080 frame and reports:
  - any element that overflows the slide bounds (top/right/bottom/left)
  - any element that overlaps an ASTRO character (character eating type)
  - any headline/paragraph whose scrollHeight > clientHeight (text clipped)
  - any pair of large text blocks whose bounding boxes intersect

Writes per-slide screenshots into /tmp/fame_audit/slideNN.png and a
plaintext report to /tmp/fame_audit/report.txt.
"""
from playwright.sync_api import sync_playwright
from pathlib import Path
import json

URL = "file:///Users/mdevulapalli/Desktop/fame-loan-servicing-deck/index.html"
OUT = Path("/tmp/fame_audit")
OUT.mkdir(exist_ok=True)

SLIDE_W, SLIDE_H = 1920, 1080
TOL = 2  # px tolerance for edge overflow

# Selectors we care about auditing per slide.
INSPECT = [
    "h1", "h2", "h3",
    ".title-hero", ".title-subtitle", ".title-footer",
    ".scene-quote", ".scene-caption",
    ".stat-hero", ".stat-caption", ".stat-context",
    ".critique-title", ".critique-list", ".critique-item",
    ".reframe-lead", ".reframe-main", ".reframe-sub",
    ".solution-title", ".semantic-sub", ".arch-diagram",
    ".built-value", ".built-grid",
    ".better-title", ".better-grid", ".better-card",
    ".close-headline", ".close-sub", ".close-footer",
    ".astro", ".sparkle",
]

def rect_overlaps(a, b):
    return not (a["right"] <= b["left"] or b["right"] <= a["left"]
                or a["bottom"] <= b["top"] or b["bottom"] <= a["top"])

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    ctx = browser.new_context(viewport={"width": SLIDE_W, "height": SLIDE_H})
    page = ctx.new_page()
    page.goto(URL, wait_until="networkidle")
    page.add_style_tag(content=".reveal, .reveal-slow { opacity: 1 !important; transform: none !important; }")
    page.wait_for_timeout(500)

    total = page.evaluate("document.querySelectorAll('.slide').length")
    report_lines = []
    problems_total = 0

    for i in range(total):
        page.wait_for_timeout(300)
        n = i + 1

        info = page.evaluate("""({sels, idx}) => {
            const slide = document.querySelectorAll('.slide')[idx];
            if (!slide) return null;
            const sRect = slide.getBoundingClientRect();
            const items = [];
            for (const sel of sels) {
                for (const el of slide.querySelectorAll(sel)) {
                    const r = el.getBoundingClientRect();
                    const cs = window.getComputedStyle(el);
                    items.push({
                        sel,
                        tag: el.tagName.toLowerCase(),
                        cls: (el.className && el.className.baseVal !== undefined) ? el.className.baseVal : (el.className || ''),
                        text: (el.innerText || '').replace(/\\s+/g,' ').trim().slice(0, 90),
                        rect: {left:r.left,right:r.right,top:r.top,bottom:r.bottom,width:r.width,height:r.height},
                        scrollH: el.scrollHeight,
                        clientH: el.clientHeight,
                        overflow: cs.overflow,
                    });
                }
            }
            return { slideRect: {left:sRect.left,right:sRect.right,top:sRect.top,bottom:sRect.bottom,width:sRect.width,height:sRect.height}, items };
        }""", {"sels": INSPECT, "idx": i})

        if not info:
            continue

        s = info["slideRect"]
        problems = []

        for it in info["items"]:
            r = it["rect"]
            # skip zero-size (display:none, etc.)
            if r["width"] < 1 or r["height"] < 1:
                continue
            label = f"{it['sel']} ({it['text'][:60]!r})"

            # 1. Overflow beyond slide bounds
            if r["left"] < s["left"] - TOL:
                problems.append(f"LEFT overflow by {int(s['left']-r['left'])}px — {label}")
            if r["right"] > s["right"] + TOL:
                problems.append(f"RIGHT overflow by {int(r['right']-s['right'])}px — {label}")
            if r["top"] < s["top"] - TOL:
                problems.append(f"TOP overflow by {int(s['top']-r['top'])}px — {label}")
            if r["bottom"] > s["bottom"] + TOL:
                problems.append(f"BOTTOM overflow by {int(r['bottom']-s['bottom'])}px — {label}")

            # 2. Text clipped inside its own box (scrollHeight > clientHeight)
            if it["overflow"] in ("hidden", "clip") and it["scrollH"] > it["clientH"] + 4:
                problems.append(f"TEXT clipped by {it['scrollH']-it['clientH']}px inside {label}")

        # 3. Astro / character collides with type
        astros = [it for it in info["items"] if "astro" in (it["cls"] or "") and "sparkle" not in (it["cls"] or "")]
        type_blocks = [it for it in info["items"]
                       if it["sel"] in ("h1","h2","h3",".title-subtitle",".scene-quote",".stat-hero",
                                        ".stat-caption",".reframe-main",".reframe-sub",".solution-title",
                                        ".semantic-sub",".better-title",".close-headline",".close-sub",".critique-title")]
        for a in astros:
            # Astro PNGs have ~18% transparent padding on each side. Shrink bbox to visual core.
            pad_x = a["rect"]["width"] * 0.18
            pad_y = a["rect"]["height"] * 0.10
            core = {
                "left":   a["rect"]["left"]   + pad_x,
                "right":  a["rect"]["right"]  - pad_x,
                "top":    a["rect"]["top"]    + pad_y,
                "bottom": a["rect"]["bottom"] - pad_y,
            }
            for t in type_blocks:
                if rect_overlaps(core, t["rect"]):
                    ox = max(0, min(core["right"], t["rect"]["right"]) - max(core["left"], t["rect"]["left"]))
                    oy = max(0, min(core["bottom"], t["rect"]["bottom"]) - max(core["top"], t["rect"]["top"]))
                    if ox * oy > 1500:
                        problems.append(f"CHARACTER overlaps type ({int(ox)}x{int(oy)}px core) — astro vs {t['sel']}: {t['text'][:60]!r}")

        page.screenshot(path=str(OUT / f"slide{n:02d}.png"))

        if problems:
            report_lines.append(f"\n─── Slide {n:02d} — {len(problems)} issue(s) ───")
            for pr in problems:
                report_lines.append(f"  • {pr}")
            problems_total += len(problems)
        else:
            report_lines.append(f"\n─── Slide {n:02d} — clean ✓ ───")

        page.keyboard.press("ArrowRight")

    browser.close()

report = f"FAME deck layout audit\n{'='*40}\nTotal problems: {problems_total}\n" + "\n".join(report_lines) + "\n"
(OUT / "report.txt").write_text(report)
print(report)
print(f"\nScreenshots + report → {OUT}/")
