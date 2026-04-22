# DESIGN SYSTEM — TRDEFI Design Documentation

Bu klasör, tüm tasarım ve yaratım işleri için referans dokumentasyon içerir.
Her yeni proje veya redesign çalışmasında bu dosyalar referans alınır.

---

## Klasör Yapısı

```
DESIGN/
├── shadcn/          # shadcn/ui component dokümantasyonu
├── tailwind/        # Tailwind CSS dokümantasyonu
├── components/      # Örnek component kodları (React + Tailwind)
├── blueprints/     # Proje bazlı tasarım spesifikasyonları
│   └── trdefi/     # TRDEFI.com Blueprint (ana referans)
└── references/      # Genel tasarım referansları, makaleler
```

---

## Kullanım Kuralları

### Her Tasarım İşi Öncesinde:
1. `DESIGN/blueprints/trdefi/blueprint.md` — Mevcut proje blueprint'ini oku
2. `DESIGN/shadcn/` — shadcn/ui komponent dokümantasyonunu kontrol et
3. `DESIGN/tailwind/` — Tailwind CSS class'larını doğrula

### Kod Yazım Standartları:
- **Framework:** React (Next.js App Router) + TypeScript
- **Styling:** Tailwind CSS (custom CSS only when absolutely necessary)
- **Components:** shadcn/ui base components + Lucide Icons
- **Font:** Montserrat (display/headings) + Open Sans (body)
- **Color:** Pink accent `#ff73c3` — tüm projelerde tutarlı

### Tasarım Vibe & Aesthetics ( Lovelable/v0 tarzı):
- Modern, minimalist, clean aesthetic
- Ample whitespace, subtle borders (border-border)
- Soft shadows
- High contrast text
- Clear typographic hierarchy
- Mobile-first responsive design
- Dark theme dominant (background: #000)

### Renk Sistemi (TRDEFI):
```
--pink:        #ff73c3  (Primary accent)
--background: #000000  (Sayfa arka planı)
--foreground: #ffffff  (Ana metin)
--card:       #0d0d0d  (Kart arka planı)
--secondary:  #1a1a1a  (İkincil yüzeyler)
--muted:      #262626  (Gri yüzeyler)
--border:     #333333  (Kenarlıklar)
```

### Animasyonlar:
```
@keyframes float        — 3s ease-in-out infinite, translateY(0 → -20px)
@keyframes pulse-pink  — 4s ease-in-out infinite, scale(1 → 1.05)
@keyframes glitch      — 5s ease-in-out infinite, translate jitter
@keyframes ping        — 1s cubic-bezier, scale(2) + fade
@keyframes reveal-up  — 0.8s cubic-bezier(.16,1,.3,1), fade + translateY(60px)
@keyframes flip-in    — rotateX(90deg → 0deg), 1.2s
@keyframes breathe     — 10s ease-in-out, scale(1 → 1.02)
```

### Typographic Scale:
```
Display/Headings: Montserrat, weight 900, uppercase, tracking tight
Body: Open Sans, weight 400, normal case
Size scale: text-6xl → text-9xl (headings), text-lg (body), text-sm (captions)
Letter-spacing: tracking-tight (-0.05em) headings, tracking-widest (0.1em) labels
```

---

## Önemli Notlar

### CSS Yazarken:
- `custom.css` dosyası Shopify Liquid theme'ler için kullanılır
- Next.js/React projeleri için Tailwind CSS inline utilities tercih et
- CSS variable'lar (`--pink`, `--background`) yalnızca `custom.css` içinde tanımla
- Blueprint renkleri her zaman `blueprints/trdefi/blueprint.md`'den alınır

### Animasyon Efektleri:
- Scroll-triggered animasyonlar için `IntersectionObserver` kullan
- Continuous animasyonlar için `@keyframes` tanımla
- Hover transition'lar için `duration-300` (0.3s ease) default

### Grain Overlay (DARK THEME):
```html
<svg style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999;pointer-events:none;opacity:0.03">
  <filter id="noise"><feturbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/></filter>
  <rect width="100%" height="100%" filter="url(#noise)"/>
</svg>
```

### Full-Width Sections:
```css
section { width: 100vw; margin-left: calc(-50vw + 50%); }
section { min-height: 100vh; }
```

### Watermark Pattern:
```css
.hero-banner__watermark {
  font-size: clamp(4rem, 12vw, 10rem);
  color: rgba(255,255,255,0.02);
  pointer-events: none;
}
```

---

## Kaynaklar

### shadcn/ui Docs:
- GitHub: `https://github.com/shadcn-ui/ui/tree/main/apps/www/content/docs`
- Web: `https://ui.shadcn.com/docs`
- Jina Reader: `https://r.jina.ai/https://ui.shadcn.com/docs`

### Tailwind CSS:
- GitHub: `https://github.com/tailwindlabs/tailwindcss.com/tree/master/src/pages/docs`
- Web: `https://tailwindcss.com/docs`
- Jina Reader: `https://r.jina.ai/https://tailwindcss.com/docs`

### Radix UI:
- GitHub: `https://github.com/radix-ui/website/tree/main/data`
- Web: `https://radix-ui.com/docs`

### Lovable/v0 Pattern:
- Referans site: `https://effortless-puffpuff-66e283.netlify.app/`
- Blueprint: `DESIGN/blueprints/trdefi/blueprint.md`
