# Narration Script Template

One narration entry per slide. Each entry has:
- `slide` — 1-indexed slide number
- `hold` — how long the slide should be on screen (seconds). Longer than the narration itself, so there's a small breathing pause between slides.
- `text` — the exact words to speak.

## How to tune hold times

1. Speak the text aloud at a natural pace. Time it with a stopwatch.
2. Add ~1 second per slide for a breath at the end.
3. If you're using ElevenLabs, `tts_elevenlabs.py` will pad with silence to exactly match `hold`.
4. If you're using `say`, `tts_say.py` does the same.
5. If you're self-recording, aim to end each slide's narration ~1 second before the next arrow press.

## Narration voice rules

- **Contractions everywhere.** "We're not interpreting screenshots" — never "We are not."
- **Em-dash for a real pause.** "Meet VizVoice — a voice-first analytics agent…"
- **Ellipsis for a *breath*, not thought-drift.** "So what if you didn't need to see the chart at all…"
- **Say "you" not "the user."** Even for internal pitches.
- **Numbers spelled out for stat slides.** "Two hundred and fifty-three million" — NOT "253 million" (TTS engines say "two hundred fifty three" without the "and," which sounds off).
- **Agentforce is ONE word.** Written and spoken.
- **Never say "revolutionary," "cutting-edge," "next-gen," "leverage," "unlock," "empower," "seamless."**

## JSON format (what the TTS scripts consume)

```json
[
  {"slide": 1, "hold": 12, "text": "Let me start with a question. What if your best analyst couldn't see your dashboard? Meet VizVoice. A voice-first analytics agent, built for people who are blind or have low vision."},
  {"slide": 2, "hold": 16, "text": "Imagine you're in a product review, and someone says, \"Can you pull up the dashboard?\" Half the room turns toward the screen. The other half has no idea what's on it. That's the experience millions of blind and low-vision users face every day."}
]
```

## Splitting: intro vs demo vs outro

- **intro** — slides 1 through the slide right before your live demo (usually 6 or 7).
- **demo** — if you have an app demo MP4, this is a passthrough (no TTS). Skip these slides in the narration JSON.
- **outro** — the slides after the demo (usually the last 3: how-we-built-it, better-default, close/team).

## Pause tokens (only for ElevenLabs / `say`)

Both engines respect these markers if the recorder passes them through:

- `<pause:400>` — insert 400ms of silence.
- `<break time="1s"/>` (ElevenLabs SSML-style) — insert a 1-second pause.

Use pauses sparingly — one per slide max. They're for the moment BEFORE a payoff line: *"Because the real insight isn't in the pixels. <pause:500> It's in the answer you're looking for."*
