# Tailwind CSS — Quick Reference & Design Patterns

## Typography Scale
```
text-xs    = 0.75rem  (12px)
text-sm    = 0.875rem (14px)
text-base  = 1rem     (16px)
text-lg    = 1.125rem (18px)
text-xl    = 1.25rem  (20px)
text-2xl   = 1.5rem   (24px)
text-3xl   = 1.875rem (30px)
text-4xl   = 2.25rem  (36px)
text-5xl   = 3rem     (48px)
text-6xl   = 3.75rem  (60px)
text-7xl   = 4.5rem   (72px)
text-8xl   = 6rem     (96px)
text-9xl   = 8rem     (128px)
```

## Font Weight
```
font-thin       = 100
font-extralight = 200
font-light      = 300
font-normal     = 400
font-medium     = 500
font-semibold   = 600
font-bold       = 700
font-extrabold  = 800
font-black      = 900
```

## Letter Spacing
```
tracking-tighter = -0.05em
tracking-tight   = -0.025em
tracking-normal  = 0em
tracking-wide    = 0.025em
tracking-wider   = 0.05em
tracking-widest  = 0.1em
```

## Color System (TRDEFI Dark Theme)
```
Text/Background:
  text-white      = #ffffff
  text-black      = #000000
  text-gray-50    = #fafafa
  text-gray-100   = #f5f5f5
  text-gray-200   = #e5e5e5
  text-gray-300   = #d4d4d4
  text-gray-400   = #a3a3a3
  text-gray-500   = #737373
  text-gray-600   = #525252
  text-gray-700   = #404040
  text-gray-800   = #262626
  text-gray-900   = #1a1a1a
  text-gray-950   = #0d0d0d

Borders:
  border-gray-50    = #fafafa
  border-gray-100   = #f5f5f5
  border-gray-200   = #e5e5e5
  border-gray-300   = #d4d4d4
  border-gray-400   = #a3a3a3
  border-gray-500   = #737373
  border-gray-600   = #525252
  border-gray-700   = #404040
  border-gray-800   = #262626
  border-gray-900   = #1a1a1a
  border-gray-950   = #0d0d0d

Backgrounds:
  bg-black          = #000000
  bg-white          = #ffffff
  bg-gray-950       = #0d0d0d   (card)
  bg-gray-900       = #1a1a1a   (secondary)
  bg-gray-800       = #262626   (muted)
```

## Spacing
```
p-0  = 0px
p-1  = 4px
p-2  = 8px
p-3  = 12px
p-4  = 16px
p-5  = 20px
p-6  = 24px
p-8  = 32px
p-10 = 40px
p-12 = 48px
p-16 = 64px
p-20 = 80px
p-24 = 96px

py-24 = padding-top + padding-bottom = 96px
px-6  = padding-left + padding-right = 24px (mobile)
px-12 = padding-left + padding-right = 48px (desktop)
```

## Flexbox
```
flex              = display: flex
flex-col         = flex-direction: column
flex-row         = flex-direction: row
flex-wrap        = flex-wrap: wrap
flex-1           = flex: 1 1 0%
flex-auto        = flex: 1 1 auto
flex-none        = flex: none
items-center     = align-items: center
items-start      = align-items: flex-start
items-end        = align-items: flex-end
justify-center   = justify-content: center
justify-between  = justify-content: space-between
justify-start    = justify-content: flex-start
justify-end      = justify-content: flex-end
gap-2           = gap: 8px
gap-4           = gap: 16px
gap-6           = gap: 24px
gap-8           = gap: 32px
```

## Grid
```
grid             = display: grid
grid-cols-1      = 1 column (mobile)
grid-cols-2      = 2 columns
grid-cols-3      = 3 columns
grid-cols-4      = 4 columns
grid-cols-6      = 6 columns
grid-cols-12     = 12 columns

col-span-2       = span 2 columns
col-span-3       = span 3 columns
col-span-4       = span 4 columns

md:grid-cols-2   = 2 columns on medium screens (768px+)
lg:grid-cols-3   = 3 columns on large screens (1024px+)
xl:grid-cols-4   = 4 columns on extra large (1280px+)
```

## Sizing
```
w-full    = width: 100%
w-screen  = width: 100vw
h-full    = height: 100%
h-screen  = height: 100vh
min-h-screen = min-height: 100vh
max-w-6xl   = max-width: 72rem (1152px)
max-w-7xl   = max-width: 80rem (1280px)
max-w-8xl   = max-width: 90rem (1440px)
max-w-none  = max-width: none
```

## Border Radius
```
rounded-none   = border-radius: 0    (sharp corners — TRDEFI style)
rounded-sm     = border-radius: 0.125rem (2px)
rounded        = border-radius: 0.25rem (4px)
rounded-md     = border-radius: 0.375rem (6px)
rounded-lg     = border-radius: 0.5rem (8px)
rounded-xl     = border-radius: 0.75rem (12px)
rounded-2xl    = border-radius: 1rem (16px)
rounded-full   = border-radius: 9999px (pill)
```

## Shadows
```
shadow-sm      = box-shadow: 0 1px 2px rgba(0,0,0,0.05)
shadow         = box-shadow: 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06)
shadow-md      = box-shadow: 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06)
shadow-lg      = box-shadow: 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05)
shadow-xl      = box-shadow: 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04)
shadow-2xl     = box-shadow: 0 25px 50px rgba(0,0,0,0.25)
shadow-none    = box-shadow: none
```

## Transitions
```
duration-150   = 150ms
duration-300   = 300ms  (default for hover)
duration-500   = 500ms  (card zoom)
ease           = ease (default)
ease-in        = ease-in
ease-out       = ease-out
ease-in-out    = ease-in-out
```

## Opacity
```
opacity-0      = 0%
opacity-25     = 25%
opacity-40     = 40%  (labels)
opacity-50     = 50%
opacity-60     = 60%  (subtitles)
opacity-75     = 75%
opacity-100    = 100%
```

## Responsive Breakpoints
```
sm:   = 640px   (small tablets)
md:   = 768px   (tablets/laptops)
lg:   = 1024px  (desktops)
xl:   = 1280px  (large desktops)
2xl:  = 1536px  (extra large)

Mobile-first: default is mobile, sm/md/lg apply larger screens
```

## Custom Transition (TRDEFI Card Hover)
```css
transition: transform 0.5s cubic-bezier(.16,1,.3,1), border-color 0.3s ease;
```
In Tailwind: `transition-all duration-500 ease-expo`

Add to tailwind.config.js:
```js
extend: {
  transitionTimingFunction: {
    'expo': 'cubic-bezier(.16,1,.3,1)',
  }
}
```

## Animations (Tailwind Default)
```
animate-spin      = rotate 360deg over 1s infinite
animate-pulse      = scale 1→1.05→1 over 2s infinite
animate-bounce     = translateY 0→-25%→0 over 1.4s infinite

Custom in tailwind.config.js:
animate-float      = float 3s ease-in-out infinite
animate-pulse-pink  = pulse-pink 4s ease-in-out infinite
```

## Z-Index
```
z-0    = 0
z-10   = 10
z-20   = 20
z-30   = 30
z-40   = 40
z-50   = 50
z-9999 = 9999 (overlay/grain)
```

## Position
```
relative = position: relative
absolute = position: absolute
fixed    = position: fixed
sticky   = position: sticky
inset-0  = top:0; right:0; bottom:0; left:0
top-0    = top: 0
left-0   = left: 0
```

## Text Utilities
```
uppercase    = text-transform: uppercase
lowercase    = text-transform: lowercase
capitalize   = text-transform: capitalize
normal-case  = text-transform: none
underline    = text-decoration: underline
line-clamp-2 = display: -webkit-box; -webkit-line-clamp: 2; overflow: hidden
truncate     = overflow: hidden; text-overflow: ellipsis; white-space: nowrap
```

## Visibility
```
overflow-hidden   = overflow: hidden
overflow-auto     = overflow: auto
overflow-x-auto   = overflow-x: auto (horizontal scroll)
```

## Pointer Events
```
pointer-events-none   = pointer-events: none
pointer-events-auto   = pointer-events: auto
```

## Full-Width Section Trick
```css
section { width: 100vw; margin-left: calc(-50vw + 50%); }
```
Tailwind equivalent: `w-screen -ml-[calc(50vw-50%)]`

## Grain Overlay
```tsx
<svg className="fixed inset-0 w-full h-full pointer-events-none z-[9999]" style={{opacity:0.03}}>
  <filter id="noise">
    <feturbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/>
  </filter>
  <rect width="100%" height="100%" filter="url(#noise)"/>
</svg>
```

## Common Component Patterns

### Navbar
```tsx
<nav className="fixed top-0 inset-x-0 z-50 bg-black/80 backdrop-blur-md border-b border-gray-800">
  <div className="max-w-6xl mx-auto px-6 flex items-center justify-between h-16">
    <div className="text-white font-black text-xl">LOGO</div>
    <div className="hidden md:flex gap-8">
      <a href="#" className="text-gray-400 hover:text-white transition-colors">Link</a>
    </div>
  </div>
</nav>
```

### Hero Section
```tsx
<section className="relative min-h-screen flex items-center justify-center bg-black">
  {/* Watermark */}
  <span className="absolute inset-0 flex items-center justify-center pointer-events-none
    text-[12vw] font-black text-white/[0.02] select-none overflow-hidden">
    WATERMARK
  </span>
  {/* Content */}
  <div className="relative z-10 text-center">
    <h1 className="text-6xl md:text-8xl font-black tracking-tight text-white">
      HEADLINE
    </h1>
  </div>
</section>
```

### Card Component
```tsx
<div className="bg-gray-950 border border-gray-800 overflow-hidden
  transition-all duration-500 ease-expo hover:scale-105 hover:border-pink-500">
  <img className="w-full aspect-square object-cover transition-transform duration-500 group-hover:scale-110" />
  <div className="absolute inset-0 bg-black/80 opacity-0 group-hover:opacity-100 transition-opacity duration-300">
    {/* overlay content */}
  </div>
</div>
```

### Section Label
```tsx
<div className="flex items-center gap-4 mb-8">
  <span className="w-12 h-px bg-pink-500"></span>
  <span className="text-xs font-semibold uppercase tracking-widest text-pink-500">
    Section Label
  </span>
</div>
```

### Primary Button (TRDEFI Pink)
```tsx
<button className="bg-pink-500 text-black font-bold text-sm uppercase tracking-wide
  px-8 py-3 border-none cursor-pointer
  hover:bg-white transition-colors duration-300">
  Call to Action
</button>
```

### Outline Button
```tsx
<button className="bg-transparent text-pink-500 border-2 border-pink-500
  font-bold text-sm uppercase tracking-wide px-8 py-3
  hover:bg-pink-500 hover:text-black transition-all duration-300">
  Learn More
</button>
```