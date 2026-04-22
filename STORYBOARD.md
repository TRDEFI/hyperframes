# STORYBOARD.md — TRDEFI Product Video

## Production Info
- **Product:** Tongue Kiss Big Eye Dog Slippers — TRDEFI.com
- **Format:** 1080×1920 (9:16 Portrait)
- **Duration:** ~17.2s
- **Style:** Maximalist Type (High-Energy Product Showcase)
- **Audio:** edge-tts JennyNeural +8%, word-level timestamps

---

## Global Settings

**Format:** 1080×1920 portrait
**Audio:** JennyNeural +8% narration + ambient underscore
**VO direction:** Energetic, young-female, social-media ad register — punchy delivery with pauses between beats. "Wait" lands with surprise. CTA is confident, not desperate.
**Style basis:** DESIGN.md — pink/yellow/cyan triad, Montserrat Black headlines, dark background with radial glow

---

## Global Guardrails

- Push color presence. Pink at 20% opacity radial glow, yellow price text, cyan accents.
- Motion visible and intentional — every element has at least one mid-scene animation.
- Use all 6 product photos scattered across beats.
- 8-10 visual elements per beat minimum.
- Maximum 2 consecutive text-only beats. Third must have visual.
- Opening beat must have visual asset (not text-only).

---

## Asset Audit

| Asset | Type | Assign to Beat | Role |
|-------|------|---------------|------|
| img_1.webp | Product photo | Beat 1, 2 | Full-bleed hero, center |
| img_2.webp | Product photo | Beat 2, 5 | Close-up lifestyle |
| img_3.webp | Product photo | Beat 3 | Benefits showcase |
| img_4.webp | Product photo | Beat 4, 5 | Reviews/social proof |
| img_5.webp | Product photo | Beat 3 | Benefits variety |
| img_6.webp | Product photo | Beat 4 | Reviews depth |

---

## Per-Beat Direction

---

### BEAT 1 — COLD OPEN HOOK (0:00–0:02.5s)

**VO:** "Wait — these slippers?"

**Concept:** Immediate impact. The viewer SCREAMS to a halt. A giant "WAIT." slams into frame while product photo bleeds in behind it. The hook is the visual AND the audio — they land together. Bold, loud, unapologetic.

**Visual description:**
- Full-bleed product image (img_1) as animated background, slow zoom 1.0 → 1.06
- "WAIT." in Montserrat Black 180px, pure white, centered — SLAMS in from scale 0.7 with `expo.out`
- "these slippers?" in Montserrat 900 100px, Electric Yellow, drops below "WAIT." with `back.out(1.4)` overshoot
- 5 decorative sparkles (SVG stars) scatter across frame — staggered, random-ish angles
- Radial pink glow pulses (scale 1.0 → 1.08, sine.inOut loop)
- Ghost text "TRDEFI" drifts slowly in background at 5% opacity

**Mood:** Surprised, curious, stopped-in-tracks. TikTok-scroll-stopper energy.

**Assets:** img_1.webp full-bleed background with Ken Burns zoom

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| Background img | ZOOMS | scale 1→1.06, 2.5s sine.inOut |
| WAIT text | SLAMS | scale 0.7→1, opacity 0→1, 0.4s expo.out @ 0.15s |
| these slippers? | DROPS | y: 60→0, scale 0.9→1, 0.5s back.out(1.4) @ 0.35s |
| Sparkles | BURST | scale 0→1, opacity 0→1, stagger 0.1s, elastic.out @ 0.2s |
| Radial glow | BREATHES | scale 1→1.08, 4s sine.inOut loop |
| Ghost text | DRIFTS | x: ±15px, y: ±8px, 10s sine.inOut loop |

**Transition OUT:** Zoom crossfade — scene1 scales 1→1.12 + fades while scene2 scales 0.88→1 + rises from below

**Depth layers:**
- BG: img_1 with radial glow overlay
- MG: "WAIT." + "these slippers?" text
- FG: 5 sparkles scattered

**SFX:** No SFX — the VO "Wait" IS the sound moment.

---

### BEAT 2 — PRODUCT REVEAL (0:02.5–0:05.5s)

**VO:** "They are absolutely incredible."

**Concept:** The product gets its close-up. Three product photos tumble in from different directions like a gallery wall reveal. Text anchors right side with key info. The product speaks for itself.

**Visual description:**
- Product image transitions: img_1 fades, img_2 rises from scale 0.85
- Product name "TONGUE KISS" in Hot Pink 64px drops in from top
- "BIG EYE DOG SLIPPERS" in White 88px slides in from left
- Price "£25.41" in Electric Yellow 80px with strikethrough "£31.99"
- Star rating "⭐⭐⭐⭐⭐ 127 reviews" in White 28px
- Floating card effect: subtle rotation ±2°, box-shadow depth
- 4 sparkles orbit the product image

**Mood:** Confident, proud. The product earns its spotlight.

**Assets:** img_2.webp (center, larger), price text, rating stars

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| Product img | TUMBLES | rotation: -4→0, scale: 0.85→1, 0.5s back.out(1.2) |
| TONGUE KISS | CASCADE | y: -60→0, opacity 0→1, 0.4s power2.out @ 0.1s stagger |
| Price | POPS | scale 0.8→1, 0.3s elastic.out(1, 0.5) |
| Stars | SHIMMER | opacity 0.5→1 pulse, 0.2s sine.out |

**Transition OUT:** Push slide left — outgoing scene x: 0→-120, blur: 15px, 0.3s power3.in

**Depth layers:**
- BG: dark charcoal with radial glow
- MG: Product image with perspective tilt
- FG: Text panel right side

**SFX:** Soft whoosh on product reveal

---

### BEAT 3 — BENEFITS (0:05.5–0:08.5s)

**VO:** "Premium quality, amazing design."

**Concept:** Information density. Four benefits stack in a right-aligned list with icons. Each benefit has a different accent color. The text is the visual — big, bold, impossible to ignore.

**Visual description:**
- Product image (img_3, img_5) in lower-left quadrant, slow zoom
- Benefits list right-aligned with icons:
  - ✨ Premium quality materials (Yellow)
  - 🐶 Adorable design collection (Cyan)
  - ☁️ Cloud-like comfort (Pink)
  - 🎁 Perfect gift idea (Yellow)
- Each line staggers in from right with `back.out(1.3)` overshoot
- Subtle grid pattern in background at 4% opacity

**Mood:** Informative but not boring. List with personality.

**Assets:** img_3.webp, img_5.webp with Ken Burns zoom

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| Benefit 1 | SLIDES | x: 80→0, 0.5s back.out(1.3) @ 0.1s |
| Benefit 2 | DROPS | y: -40→0, 0.45s back.out(1.3) @ 0.2s |
| Benefit 3 | BURSTS | scale 0.8→1, 0.4s elastic.out @ 0.3s |
| Benefit 4 | FILLS | opacity 0→1, 0.35s power2.out @ 0.4s |
| Product img | ZOOMS | scale 1→1.04, 3s sine.inOut |

**Transition OUT:** Hard cut — scene cuts to black, next scene snaps in at full opacity

**Depth layers:**
- BG: grid pattern + radial glow
- MG: benefits list text + icons
- FG: product image lower-left with sparkle accents

**SFX:** No SFX — VO carries the beat

---

### BEAT 4 — SOCIAL PROOF (0:08.5–0:11.5s)

**VO:** "Sarah says five stars."

**Concept:** Trust building. A customer testimonial card appears center-frame with a real quote. Not fake stock — a specific person, specific city. The card has personality and warmth.

**Visual description:**
- Testimonial card: semi-transparent white bg, thin pink border, 20px radius
- Quote: "These are the comfiest slippers I've ever owned." — Inter Italic 32px
- Attribution: "Sarah — London" in Montserrat Bold 28px, Hot Pink
- 5 stars rendered as SVG ★★★★★ in Electric Yellow
- Product image (img_4) as subtle watermark behind card at 15% opacity
- Card has gentle float animation (y: ±6px, sine.inOut, 2s loop)
- Pink accent line draws in from left to right before card appears

**Mood:** Warm, trustworthy. A real human moment.

**Assets:** img_4.webp watermark, testimonial card, star SVGs

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| Testimonial card | FLOATS | y: ±6px, sine.inOut, 2s yoyo loop |
| Card border | DRAWS | scaleX: 0→1, 0.4s power2.out |
| Quote text | TYPES | opacity 0→1, 0.3s |
| Stars | BURST | scale 0→1.2→1, 0.2s elastic.out(1, 0.5) |
| Watermark img | DRIFTS | scale 1→1.06, 3s sine.inOut |

**Transition OUT:** Zoom crossfade — scene scales 1→1.08 + fades as CTA scene scales from 0.9

**Depth layers:**
- BG: product watermark at low opacity
- MG: testimonial card with border
- FG: quote + stars + attribution

**SFX:** Soft, warm chime on star reveal

---

### BEAT 5 — URGENCY + CTA (0:11.5–0:15.5s)

**VO:** "Limited stock available now. You save twenty percent today."

**Concept:** Pressure + value. Two messages land: scarcity ("Limited stock") and savings ("20% off"). The price is BIG and unmissable. The CTA button pulses urgently.

**Visual description:**
- "⏰ LIMITED STOCK" in Montserrat Bold 52px, pulsing opacity
- Price "£25.41" in Montserrat Black 140px, Electric Yellow with glow
- Savings badge: "You save £6.58" in Inter Medium 32px, Bright Green
- Original price strikethrough "£31.99" in Gray 36px
- CTA button "SHOP NOW" bottom-center — Hot Pink gradient, bouncy entrance
- Button has persistent pulse: scale 1→1.06, box-shadow intensifies
- Ghost "TRDEFI" text behind at 6% opacity as brand anchor

**Mood:** Urgent but not desperate. Clear value proposition.

**Assets:** Price text, CTA button, ghost text

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| LIMITED STOCK | FLICKERS | opacity pulse 0.7→1, 0.8s sine.inOut |
| Price | STAMPS | scale 0.85→1, 0.4s expo.out |
| CTA button | BOUNCES | scale 0.6→1, elastic.out(1, 0.4) @ 0.5s |
| CTA pulse | THROBS | scale 1→1.06, box-shadow 0.15s, repeat -1 |

**Transition OUT:** No transition — video ends at 17.2s

**Depth layers:**
- BG: ghost text + radial glow
- MG: price + savings badge
- FG: LIMITED STOCK + CTA button

**SFX:** No SFX — VO closes the deal

---

### BEAT 6 — CTA CLOSE (0:15.5–0:17.2s)

**VO:** "Shop TRDEFI.com now!"

**Concept:** The final push. Brand URL is the star. Everything else fades. The CTA button glows one last time before the video ends.

**Visual description:**
- "TRDEFI.com" in Montserrat Black 72px, centered
- URL pulses with pink glow (scale 1→1.02, text-shadow intensifies)
- CTA button final glow-up then fades
- All other elements fade to 0 opacity
- Fade to black over final 0.5s

**Mood:** Clean, confident close. The URL is the takeaway.

**Animation choreography:**
| Element | Verb | Params |
|---------|------|--------|
| URL | GLOWS | text-shadow pulse, 0.3s sine.inOut, 2 iterations |
| CTA button | RESOLVES | scale 1→1.08, 0.3s |
| Everything else | FADES | opacity→0, 0.5s power2.in |
| Final frame | BLACKOUT | opacity 0, 0.3s power2.in |

---

## Production Architecture

```
hyperframes-project/
├── index.html                    root — VO + beat orchestration
├── DESIGN.md                     brand reference
├── SCRIPT.md                     narration script
├── STORYBOARD.md                 THIS FILE
├── audio/
│   └── narration.mp3             TTS audio (from Step 5)
├── transcript.json               word-level timestamps (from Step 5)
├── product_photos/
│   ├── img_1.webp
│   ├── img_2.webp
│   ├── img_3.webp
│   ├── img_4.webp
│   ├── img_5.webp
│   └── img_6.webp
└── compositions/
    ├── beat-1-hook.html
    ├── beat-2-product.html
    ├── beat-3-benefits.html
    ├── beat-4-reviews.html
    ├── beat-5-cta.html
    └── beat-6-close.html
```
