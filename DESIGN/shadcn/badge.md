# Badge — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add badge
```

## Usage
```tsx
import { Badge } from "@/components/ui/badge"
```

## Variants
```tsx
<Badge variant="default">Default</Badge>
<Badge variant="secondary">Secondary</Badge>
<Badge variant="destructive">Destructive</Badge>
<Badge variant="outline">Outline</Badge>
<Badge variant="ghost">Ghost</Badge>
<Badge variant="link">Link</Badge>
```

## With Icon
```tsx
import { BadgeCheck } from "lucide-react"
<Badge data-icon="inline-start">
  <BadgeCheck /> Verified
</Badge>
```

## With Spinner
```tsx
import { Spinner } from "@/components/ui/spinner"
<Badge data-icon="inline-start">
  <Spinner /> Loading
</Badge>
```

## Custom Colors
```tsx
<Badge className="bg-blue-500 text-white">Blue</Badge>
<Badge className="bg-green-500 text-white">Green</Badge>
<Badge className="bg-purple-500 text-white">Purple</Badge>
```

## As Link
```tsx
import { ArrowUpRightIcon } from "lucide-react"
<Badge asChild variant="link">
  <a href="..."><ArrowUpRightIcon /> Open Link</a>
</Badge>
```

## API Reference

| Prop | Type | Default |
|------|------|---------|
| variant | "default" \| "secondary" \| "destructive" \| "outline" \| "ghost" \| "link" | "default" |
| asChild | boolean | false |
| className | string | - |