# Card — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add card
```

## Usage
```tsx
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
```

## Structure
```tsx
<Card>
  <CardHeader>
    <CardTitle>Card Title</CardTitle>
    <CardDescription>Card Description</CardDescription>
    <CardAction>Card Action</CardAction>
  </CardHeader>
  <CardContent>
    <p>Card Content</p>
  </CardContent>
  <CardFooter>
    <p>Card Footer</p>
  </CardFooter>
</Card>
```

## Composition Tree
```
Card
├── CardHeader
│   ├── CardTitle
│   ├── CardDescription
│   └── CardAction
├── CardContent
└── CardFooter
```

## Size Variants
```tsx
<Card size="sm">  // Small card with compact spacing
<Card>              // Default size
```

## Image Card Example
```tsx
<Card>
  <img src="..." alt="Cover" />
  <CardHeader>
    <CardAction><Badge>Featured</Badge></CardAction>
    <CardTitle>Event Title</CardTitle>
    <CardDescription>Event description text</CardDescription>
  </CardHeader>
  <CardContent>
    <p>Card body content</p>
  </CardContent>
  <CardFooter>
    <Button>View Event</Button>
  </CardFooter>
</Card>
```

## API Reference

| Component | Prop | Type | Default |
|-----------|------|------|---------|
| Card | size | "default" \| "sm" | "default" |
| Card | className | string | - |
| CardHeader | className | string | - |
| CardTitle | className | string | - |
| CardDescription | className | string | - |
| CardAction | className | string | - |
| CardContent | className | string | - |
| CardFooter | className | string | - |