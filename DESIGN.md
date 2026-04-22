# TRDEFI Product Video — Design System

## Style: Maximalist Type (High-Energy Product Showcase)

Bold, loud, kinetic. Text IS the visual. Every frame fills 60-80% with content. No empty space, no "clean and minimal."

---

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Primary Accent** | Hot Pink | `#FF69B4` | Headlines, highlights, CTA buttons, word glow |
| **Secondary Accent** | Electric Yellow | `#FFE600` | Price emphasis, star ratings, urgency elements |
| **Tertiary Accent** | Cyan | `#00D4FF` | Trust badges, sparkles, ambient motion |
| **Background Dark** | Deep Black | `#0A0A0A` | Primary background |
| **Background Gradient** | Dark Purple | `#1A0A2E` | Gradient overlays, scene backgrounds |
| **Surface** | Charcoal | `#1A1A2E` | Cards, panels, subtitle bars |
| **Text Primary** | Pure White | `#FFFFFF` | Body text, subtitles |
| **Text Secondary** | Light Gray | `#B0B0B0` | Muted text, secondary info |
| **Success/CTA** | Bright Green | `#00FF88` | "Buy now", urgency timers |
| **Danger/Urgent** | Red | `#FF3366` | Limited stock, discounts |

---

## Typography

### Font Families
- **Headlines**: Montserrat (700-900 weight) — Bold, modern, high-impact
- **Body/Subtitles**: Inter (400-600 weight) — Clean readability
- **Accent/Price**: Montserrat Black (900) — Maximum emphasis

### Size Scale (1080x1920 Portrait)
| Element | Size | Weight |
|---------|------|--------|
| Hero headlines | 72-96px | 900 |
| Section headlines | 48-64px | 700 |
| Body/subtitles | 36-44px | 600 |
| Price display | 80-120px | 900 |
| Trust badges | 24-32px | 600 |
| CTA buttons | 40-56px | 700 |

### Letter Spacing
- Headlines: `-0.02em` to `-0.05em` (tight)
- Body: `0em` (normal)
- ALL CAPS: `0.1em` to `0.2em` (wide tracking)

---

## Motion Rules

### Easing Personality
| Animation Type | Easing | Why |
|---------------|--------|------|
| **Entrance (default)** | `expo.out` | Fast arrival, confident snap |
| **Soft entrance** | `back.out(1.4)` | Playful overshoot |
| **Exit** | `power2.in` | Accelerates away, urgency |
| **Between positions** | `power3.inOut` | Smooth flow |
| **Scale pop** | `elastic.out(1, 0.5)` | Bouncy, energetic |
| **Drift/ambient** | `sine.inOut` | Slow, dreamy |

**RULE: Never use the same ease twice in a row.**

### Speed Hierarchy
| Speed | Duration | Use Case |
|-------|----------|----------|
| **Instant** | 0.15-0.2s | Micro-interactions, button feedback |
| **Fast** | 0.25-0.35s | Text highlights, small elements |
| **Medium** | 0.4-0.6s | Section transitions, card reveals |
| **Slow** | 0.8-1.2s | Scene transitions, dramatic reveals |
| **Cinematic** | 1.5-2.5s | Emotional moments, product deep-dives |

### Direction Variants
**Entrances MUST vary direction:**
- `y: -30` — from top
- `y: 30` — from bottom  
- `x: -40` — from left
- `x: 40` — from right
- `scale: 0.8, opacity: 0` — from small
- `scale: 1.2, opacity: 0` — from big
- `opacity: 0 only` — fade in place

**RULE: First animation starts at t=0.1s minimum (not t=0).**

### Ambient Motion (Background Layer)
Every scene needs slow, continuous motion:
- Radial glows: `scale: 1.0 → 1.08`, `sine.inOut`, 3-4s loop
- Floating particles: subtle `y: ±10px`, `sine.inOut`, 2-3s loop
- Color shifts: hue rotation 0-10deg, 5-8s loop

---

## Scene Transitions

### Primary Transition: Zoom Crossfade
For product showcases — combines scale with opacity dissolve.

```js
// Outgoing scene scales UP while fading
tl.to("#scene-1", { scale: 1.1, opacity: 0, duration: 0.4, ease: "power2.in" }, sceneEnd);

// Incoming scene scales FROM 0.9 TO 1.0 while fading in
tl.fromTo("#scene-2", 
  { scale: 0.9, opacity: 0 }, 
  { scale: 1.0, opacity: 1, duration: 0.5, ease: "expo.out" }, 
  sceneEnd + 0.1
);
```

### Accent Transitions (Use 1-2 per video)
| Transition | Duration | Easing | Use When |
|------------|----------|--------|----------|
| **Push slide** | 0.3-0.4s | `power3.out` | Next point, related content |
| **Blur crossfade** | 0.5-0.7s | `sine.inOut` | Emotional drift |
| **Overexposure** | 0.2-0.3s | `power4.out` | High-energy moment |
| **Elastic push** | 0.4-0.5s | `back.out(1.3)` | Playful reveal |

**RULE: Never crossfade everything. Mix transitions.**

---

## Caption System

### Word-by-Word Highlighting

**Base style:**
- Inactive words: `rgba(255,255,255,0.3)` — muted
- Active word: `#FF69B4` with glow `0 0 20px #FF69B4, 0 0 40px rgba(255,105,180,0.5)`
- Active scale: `1.0 → 1.1` (10% pop)

**Emphasis words break the pattern:**
- Brand names: Yellow `#FFE600` + scale `1.15`
- Prices: Green `#00FF88` + scale `1.2`
- ALL CAPS: Extra glow + slight rotation `rotate(-1deg)`

### Marker Highlight Modes (Cycle These)
For variety, rotate between highlight styles every 3-4 caption groups:

1. **Glow pop** — Current (pink glow + scale)
2. **Highlight bar** — Yellow marker sweep behind text
3. **Circle ring** — Hand-drawn ellipse around word
4. **Burst lines** — Radiating lines from center
5. **Scribble underline** — Wavy SVG underline draws in

---

## Visual Layers (Per Scene)

### Minimum 3 Layers Required

**Layer 1 — Background Treatment**
- Radial gradient glow (accent color, 10-20% opacity)
- Oversized ghost text (theme words at 5-8% opacity, very large)
- Subtle grid or pattern (3-5% opacity)

**Layer 2 — Primary Content**
- Product images (full or partial coverage)
- Headline text (60-80% frame width)
- Key information

**Layer 3 — Accent Elements**
- Sparkle/star decorations
- Accent lines (hairline rules, scale in)
- Price badges
- Trust icons

**Layer 4 — Caption/Subtitle Bar**
- Position: Bottom 25-30% of frame
- Background: `linear-gradient(transparent, rgba(0,0,0,0.9))`
- Text centered or left-aligned

---

## Layout Rules

### Portrait (1080x1920) Specifics
- **Headline zone**: Top 15-40% of frame
- **Product zone**: Center 30-60%
- **Subtitle zone**: Bottom 25-30%
- **Never center everything**: Anchor to edges (left-heavy or right-heavy compositions)

### Fill the Frame
- Headlines: 60-80% of frame width
- Product images: Fill available space, no margins
- If text is small, it's wrong — scale up 20%

### Split Compositions
Instead of centered stacks:
- Left: Product visual (60% width)
- Right: Text content (40% width)
- Or: Top/bottom splits for different content types

---

## What NOT to Do

### Anti-Patterns (AI Design Tells)
These scream "AI generated":

1. **❌ Centered everything** — Anchor left or right
2. **❌ Equal spacing** — Vary gaps intentionally  
3. **❌ Same-size elements** — Mix scales deliberately
4. **❌ Gradient text** — Solid colors with shadow/glow
5. **❌ Left-edge accent stripes** — Use different accent shapes
6. **❌ Cyan-on-dark / purple-blue gradient** — Use pink-yellow-cyan triad
7. **❌ Identical card grids** — Each card different or staggered
8. **❌ All elements same opacity** — Layer with depth (0.3 → 1.0)
9. **❌ Pure #000 or #FFF backgrounds** — Tint toward accent hue
10. **❌ Boring fonts** — Montserrat has character, use bold weights

### Color Mistakes
- ❌ Navy blue as primary accent — too corporate
- ❌ Pastel palette for product showcase — too soft
- ❌ Green-for-success always — try pink or yellow for energy
- ❌ Gray gradients — use colored gradients (purple→pink, etc.)

### Motion Mistakes
- ❌ All animations 0.4-0.5s — vary speeds
- ❌ All entrances from bottom (`y: 30`) — vary direction
- ❌ All eases `power2.out` — vary personality
- ❌ Animations at t=0 — always offset 0.1s minimum
- ❌ Fade-only transitions — use scale + position changes

---

## Decorative Elements

### Sparkle Animation (Use Sparingly)
```css
@keyframes sparkle {
  0%, 100% { 
    opacity: 0.3; 
    transform: scale(1) rotate(0deg); 
  }
  50% { 
    opacity: 1; 
    transform: scale(1.4) rotate(15deg); 
  }
}
```
- Position: Near product, not over text
- Size: 24-48px
- Count: 3-5 per scene, not uniform
- Color: Yellow or cyan with drop-shadow

### Radial Glow
```css
background: radial-gradient(ellipse at center, 
  rgba(255,105,180,0.15) 0%, 
  transparent 70%);
```
- Accent-tinted (pink/purple)
- 15-25% opacity maximum
- Breathing animation: scale 1.0 → 1.1, 4s sine.inOut loop

### Ghost Text
- Very large words (200-400px)
- 4-8% opacity
- Slow drift animation
- Positioned to bleed off-frame

---

## 🎯 Video Research Intelligence — Round 2 (2026-04-22)

**Tam kapsam:** 18 video, 54 frame analizi, ~4000+ fps tarandı.
**İlk set:** 9 video (27 frame) + **Yeni set:** 9 video (27 frame)

### Yeni Eklenen Video Setleri

| Video | Tip | Bulgu Skoru |
|-------|-----|------------|
| `prada_paradoxe` | Lüks parfüm film | 9/10 — Chiaroscuro ışık, minimalist kadraj |
| `cinematic_architectural` | Mimari film | 9/10 — Low-angle, malzeme detayı, altın saat ışık |
| `hilton_gold` | Otel reklamı | 8.5/10 — Komedi+havuz, sıcak doku контрастı |
| `art_of_selling_feeling` | Reklamcılık hikayesi | 8/10 — Arşiv görüntü + modern ürün sunumu |
| `beauty_products_home` | Ev tipi güzellik | 7/10 — Organik apothecary estetik |
| `aesthetic_unboxing_camera` | Kamera unboxing | 8/10 — DIY+zanaatkar detay, temiz sunum |
| `iphone_unboxing_asmr` | ASMR unboxing | 8.5/10 — Telefon koruma camı uygulaması |
| `judebellingham_unboxing` | Kart collection | 7/10 — Açıklama/review, izleyici etkileşimi |
| `phone_closeup_scroll` | Telefon scroll | 8/10 — Screen glow ışık, dramatik alt-üst perspektif |

---

## 🎯 Video Research Intelligence — Round 1 (2026-04-22)

9 video, 27 frame analizi. Toplam referans: ~2000+ fps incelendi.

---

### 📌 Ortak Kalıplar (Tüm Videolarda Görülen)

| Öğe | Bulgu | Action |
|-----|-------|--------|
| **Arka plan** | Koyu, low-key, derin gölgeli | Karanlık atmosfer = premium his |
| **Renk paleti** | 3-4 renk max, biri warm accent | Karmaşık palet = amateur |
| **Depth** | Her başarılı karede 3 katman (fore/mid/background) | Her zaman 3+ layer planla |
| **Işık** | Soft key + sharp accent rim light | Tek kaynak değil, iki-dual lighting |
| **Hareket** | Shallow DOF, bokeh, drone shot | Statik kare = boring |
| **Renk sıcaklığı** | Warm tones (amber/gold) against cool dark bg | Sıcak/soğuk kontrast = profesyonel |
| **Tipografi** | Bold sans-serif (lifestyle) veya elegant serif (luxury) | Tipografi = marka sesi |
| **Hikaye** | "The modern creator" veya "premium craftsmanship" | Ürünü değil deneyimi sat |

---

### 🎬 Scene-Specific Bulgu Setleri

#### 1. Unboxing/Product Reveal (ekGdPHlhcPM)
- **Mood**: "Cozy-tech", focused creator
- **Palette**: `#1F292B` dark charcoal wall + `#8B5A2B` warm walnut desk + `#FF5E3A` ember accent light
- **Lighting**: LED strip rim light (top-right), soft key from left, deep shadows on desk underside
- **Composition**: Rule of thirds, diagonal leading lines from desk → subject
- **Dekor**: C-stand, hex panel wall art, botanical monitor wallpaper
- **Story**: "Preparation and curation" — creator setting up, not selling
- **Rating**: 8.5/10

#### 2. Beauty/Skincare Commercial (otej7WLdPh0)
- **Mood**: Ethereal, weightless, "dream-like"
- **Palette**: `#F49AC1` rose pink + `#E87EA1` soft magenta + `#FFFFFF` white + `#D1D1E0` pale lavender
- **Lighting**: High-key soft-box, even highlights, no harsh shadows
- **Composition**: Diagonal "V" formation (two products crossing)
- **Dekor**: Floating rose petals + water bubbles/bokeh (varying sizes)
- **Story**: "Floral infusion and hydration" — product is natural, weightless
- **Yeni Teknik**: Organik elementler (petals, bubbles) floating in foreground/background = premium beauty standard
- **Rating**: 8.5/10

#### 3. Luxury Jewelry (CKHheIsL02U)
- **Mood**: Intimate, sophisticated, alluring (hotel-luxe)
- **Palette**: `#E8E9EB` silver/satin + `#C9A693` warm skin/bronze + `#4D3A31` deep espresso + `#2B2521` charcoal shadow
- **Lighting**: Glamour soft key from camera-left + high contrast dark background
- **Composition**: Rule of thirds, raised hand creates leading line toward jewelry
- **Dekor**: Statement jewelry (Bvlgari Serpenti-style), silk/satin blouse, ornate wall mirror
- **Story**: "Private, high-end elegance" — OTS gaze creates personal connection
- **Yeni Teknik**: Blurred foreground mirror + sharp subject = depth without bokeh generic
- **Rating**: 9/10

#### 4. Ultra-Modern Interior / Luxury Real Estate (zGRU_o90bBM)
- **Mood**: Clinical, pristine, "near-future" minimalist
- **Palette**: `#F7F7F7` cool white + `#BC8E5B` tan leather + `#1A1A1A` carbon black + `#9DA2A6` brushed steel
- **Lighting**: Recessed ceiling spotlights, soft even ambient, high reflectivity on glossy surfaces
- **Composition**: Wide-angle, strong linear perspective, one-point perspective converging to vanishing point
- **Dekor**: Abstract monochromatic wall art, designer leather swivel stools, handle-less cabinetry, chrome gooseneck faucet
- **Story**: "Extreme wealth, controlled aesthetic purity" — tech-bro luxury
- **Yeni Teknik**: Kontrastlı furniture (organic wooden stools vs. clinical white cabinets) = warmth injection
- **Rating**: 9/10

#### 5. High-Fashion / Brand Film (W5PRZuaQ3VM — Bulgari style)
- **Mood**: Surreal, whimsical, aristocratic, enchanted
- **Palette**: `#D9C5A3` marble beige + `#6B7243` olive green + `#6D3D8E` deep purple + `#F7F3E9` cream
- **Lighting**: High-key natural diffused light from large windows (right side), soft shadows
- **Composition**: Symmetrical one-point perspective centered on mirror + chandelier
- **Dekor**: Crystal chandelier, marble inlaid floors, olive velvet drapes, classical busts, **suspended colorful flower blooms** (key!)
- **Story**: "Magic invading rigid high-society tradition" — nature vs. aristocracy
- **Yeni Teknik**: Floating/disappearing organic elements (flowers breaking from arrangement) = surrealist luxury
- **Rating**: 9/10

#### 6. Fashion/Lifestyle Close-up (t2LMvk7CKJ0 — Mohair)
- **Mood**: Intimate, contemplative, "confessional"
- **Palette**: `#35232B` deep plum jacket + `#7E2E1C` rust armchair + `#EAE7D6` off-white shirt + `#2A4340` cool ambient
- **Lighting**: Low-key, warm key from front-left + cool screen ambient from right (color temperature contrast)
- **Composition**: Tight medium close-up, shallow DOF, subject slightly off-center
- **Dekor**: Wingback chair (heavy textured upholstery), corduroy jacket, velvet textures
- **Story**: "Private study, emotional processing" — character isolated in thought
- **Yeni Teknik**: Color temperature contrast (warm front + cool back) = depth without lighting equipment
- **Rating**: 8/10

#### 7. Luxury Product (Coffee/Artisan) (_GFlR5e1ueY)
- **Mood**: Dark, luxurious, cinematic, intimate
- **Palette**: `#000000` rich black + `#1A1A1A` dark charcoal + `#D4AF37` metallic gold + `#3E2723` deep umber
- **Lighting**: Low-key dramatic side-lighting + strong back rim light on glass = sharp rim highlights, deep shadows
- **Composition**: Close-up shallow DOF, hand enters from top-right for movement, foreground bokeh glassware
- **Dekor**: Crystal glassware, matte black bottle with gold label, scattered coffee beans/botanicals
- **Story**: "Premium artisan preparation" — sensory, tactile, craftsmanship
- **Yeni Teknik**: Dark product + gold accent = luxury baseline. Foreground bokeh glassware framing = professional touch
- **Rating**: 9/10

#### 8. Lifestyle/Authentic UGC (SpJHb9v3vrY)
- **Mood**: Authentic, relatable, "aspirational yet attainable"
- **Palette**: Neutral grays + warm accents (#F9E220 yellow text, #D2B48C tan wood)
- **Lighting**: Large window soft diffused light from right, low-contrast natural
- **Composition**: Medium close-up shallow DOF, laptop foreground framing, rule of thirds
- **Dekor**: Visible camera gear (lenses), subway tile backsplash, floating wood shelves, gold hardware on black cabinets
- **Story**: "Creator blending professional + personal authenticity" — lifestyle as marketing
- **Yeni Teknik**: "Lived-in professional" setting (organized but personal) = aspirational authenticity
- **Rating**: 8/10

---

### 🔑 Critical Insights for Hyperframes Production

#### EN YENİ TEKNİKLER (Round 1 — 27 Frame)

1. **Dual Lighting Setup**: Soft diffused key light + sharp accent rim light (ayrı kaynaklar)
   - Bizim videolar: sadece 1 ışık kaynağı kullanıyoruz → flat görünüyor

2. **Color Temperature Contrast**: Warm front-light + cool back-light = 3D depth without extra equipment
   - Bizim videolar: tek renk sıcaklıkları → monolithic

3. **Organic Floating Elements**: Rose petals, bubbles, floating flowers = premium beauty standard
   - Bizim videolar: sadece sparkles → yetersiz

4. **Surrealist Elements in Luxury**: Classical setting + floating organic elements = Bulgari/Signer-style cinematography
   - Bizim videolar: literally realistic → eksik element

5. **Shallow DOF Foreground Framing**: Bokeh glassware/products in foreground → professional depth
   - Bizim videolar: flat compositions → sadece mid/background layers

6. **"Process" Storytelling**: Show the CREATION/CRAFT, not the product
   - Bizim videolar: product showcase → product reveal → CTA → sürekli aynı

7. **Authentic vs. Production Contrast**: "UGC-style" with professional quality = trust + aspiration
   - Aşırı clean = AI-generated tell, aşırı raw = amateur

#### EN YENİ TEKNİKLER (Round 2 — 27 Frame Ek)

8. **Chiaroscuro Lighting**: Tek kaynak, yüksek kontrast, derin gölgeler — lüks parfüm/aksesuar standardı
   - `#040607` obsidyen arka plan + `#C6BDB4` gümüş highlight = dramatik derinlik
   - Bizim videolar: çoklu kaynak olmadan tek güçlü ışık denemiyoruz

9. **Screen/Device as Light Source**: Telefon ekranı, monitor, LED strip = hem ışık hem de konu
   - Phone glow: `#31538A` cool blue + `#C8E6C9` screen green
   - Monitor ambient: `#424B54` cool slate + `#E87E04` amber accent
   - Bizim videolar: sadece CSS radial gradient → yetersiz

10. **Low-Angle Worm's Eye Perspective**: Yer seviyesinden yukarı bakan kamera = monumentallik
    - Ürün daha güçlü, daha "devasa" görünüyor
    - Mimari: `#141414` kar art + `#A8B1B8` mist gray = dramatik siluet

11. **Golden Hour / Blue Hour Timing**: Architecture/nature = sıcak/soğuk kontrastın en doğal hali
    - `#161D2E` deep midnight blue (sky) + `#A8895C` golden amber (iç mekan ışık)
    - En etkili luxury real estate sahneleri

12. **Komedi+Ürün Karışımı**: Humor + premium product = viral potential
    - Hilton reklamı: `#2c6b5e` yeşil takım elbise + `#9c844d` altın saat + komik sahne
    - Yüksek engagement = izleyici hem eğleniyor hem de markayı hatırlıyor

13. **Texture Contrast**: Matte + Metallic/Glossy aynı karede = premium algı
    - `#2B1911` dark wood (matte) + `#F2F2EC` beyaz obje (glossy) + `#B2945D` altın emblem
    - Bizim videolar: tek doku = flat

14. **Grain/Noise Overlay**: Arşiv/retro his için film grain effect
    - `#2B2B2B` charcoal + `#5E5E5E` slate grey + grain = gritty realism
    - Storytelling'e "gerçeklik" katıyor

15. **PiP (Picture-in-Picture) Layout**: Ana görüntü + küçük "creator" penceresi
    - Tutorial/review formatlarında standart
    - İzleyici ile bağlantı kuruyor (insan yüzü görünce güven artıyor)

16. **Tilt/Dutch Angle**: Hafif eğik kadraj = dinamik, hareketli his
    - `#121212` siyah + tilt = "cinematic" hissiyat
    - Sadece 5-10 derece yeterli

17. **Hands as Protagonist**: Ürün yerine eller karede — daha organik, kişisel
    - `#E0B397` flesh tone + `#4D2F1F` dark walnut = doğal kontrast
    - "Yapım aşaması" hissi — izleyici kendini yerine koyuyor

18. **Subscribe/CTA Watermark**: Video içinde sabit CTA overlay = dönüşüm
    - `%8` -sane sans-serif + glow shadow = her karede görünür ama dominant değil

---

### ❌ AI-Generated Tells (Tespit Edilen)

| Pattern | Why It's Wrong |
|---------|---------------|
| Sadece CSS/HTML backgrounds | Real video locations/storytelling eksik → fake hissiyat |
| Centered composition | Rule of thirds kullanmamak = amateur composition |
| Tek renk paleti | 3-4 renk contrast yok = flat, boring |
| Sparkle-only decorative | Petals, bubbles, organic elements eksik → missing premium texture |
| Product-focused narration | "Craft/process" yok → sadece satış tonu |
| Yüksek tutarlı tipografi | Font variety eksik (serif vs sans-serif contrast) |

---

### ✅ Yeni Benchmark Standards

**Minimum for Viral-Capable Video:**
- [ ] Real photography (Unsplash/Pexels) + CSS atmosphere layer
- [ ] Dual lighting (soft key + accent rim)
- [ ] 3-layer depth (min)
- [ ] 3-4 renk paleti (warm + cool contrast)
- [ ] Organic decorative elements (petals/bubbles/etc.)
- [ ] Process/craft storytelling (not just product showcase)
- [ ] Shallow DOF with foreground framing
- [ ] Color temperature contrast in lighting

---

## Audio Synchronization

### Bass → Scale Pulse
When narration mentions product, pulse scale 1.0 → 1.05

### Treble → Glow Intensity  
Active word glow strengthens on syllable peaks

### Silence → Ambient Motion
During pauses, background decorations continue moving

---

## Quality Checklist

Before any render:
- [ ] Frame filled 60-80% with content
- [ ] Minimum 3 visual layers
- [ ] Captions use marker highlight mode (not just color)
- [ ] Transitions mix of types (not all crossfade)
- [ ] Easings varied (not all power2.out)
- [ ] Entrance directions varied
- [ ] Speed hierarchy: 0.15s → 2.5s range used
- [ ] First animation offset t≥0.1s
- [ ] Decorative ambient motion in background
- [ ] Price/brand emphasis in accent colors
- [ ] No centered-only compositions
