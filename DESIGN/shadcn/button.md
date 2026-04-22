# Button — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add button
```

## Usage
```tsx
import { Button } from "@/components/ui/button"
```

## Variants
```tsx
<Button variant="default">Default</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="outline">Outline</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="link">Link</Button>
```

## Sizes
```tsx
<Button size="default">Default</Button>
<Button size="sm">Small</Button>
<Button size="lg">Large</Button>
<Button size="icon">Icon</Button>
<Button size="icon-xs">Icon XS</Button>
<Button size="icon-sm">Icon SM</Button>
<Button size="icon-lg">Icon LG</Button>
```

## With Icon
```tsx
import { PlusIcon } from "lucide-react"
<Button data-icon="inline-start"><PlusIcon /> New Branch</Button>
```

## Rounded
```tsx
<Button rounded-full>Round</Button>
```

## Spinner
```tsx
import { Spinner } from "@/components/ui/spinner"
<Button><Spinner data-icon="inline-start"/>Loading</Button>
```

## As Child
```tsx
import Link from "next/link"
<Button asChild><Link href="/login">Login</Link></Button>
```

## API Reference

| Prop | Type | Default |
|------|------|---------|
| variant | "default" \| "outline" \| "ghost" \| "destructive" \| "secondary" \| "link" | "default" |
| size | "default" \| "xs" \| "sm" \| "lg" \| "icon" \| "icon-xs" \| "icon-sm" \| "icon-lg" | "default" |
| asChild | boolean | false |

## Cursor Fix (Tailwind v4)
```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```