# Tabs — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add tabs
```

## Usage
```tsx
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@/components/ui/tabs"
```

## Basic Tabs
```tsx
<Tabs defaultValue="overview">
  <TabsList>
    <TabsTrigger value="overview">Overview</TabsTrigger>
    <TabsTrigger value="analytics">Analytics</TabsTrigger>
    <TabsTrigger value="settings">Settings</TabsTrigger>
  </TabsList>
  <TabsContent value="overview">Overview content</TabsContent>
  <TabsContent value="analytics">Analytics content</TabsContent>
  <TabsContent value="settings">Settings content</TabsContent>
</Tabs>
```

## Full Width
```tsx
<TabsList className="w-full">
  <TabsTrigger value="a" className="flex-1">Tab A</TabsTrigger>
  <TabsTrigger value="b" className="flex-1">Tab B</TabsTrigger>
</TabsList>
```

## With Cards
```tsx
<Tabs defaultValue="profile">
  <TabsList>
    <TabsTrigger value="profile">Profile</TabsTrigger>
    <TabsTrigger value="billing">Billing</TabsTrigger>
  </TabsList>
  <TabsContent value="profile">
    <Card><CardHeader><CardTitle>Profile</CardTitle></CardHeader></Card>
  </TabsContent>
  <TabsContent value="billing">
    <Card><CardHeader><CardTitle>Billing</CardTitle></CardHeader></Card>
  </TabsContent>
</Tabs>
```

## Dismiss/Force Render
```tsx
// Use forceMount to control visibility manually
<Tabs defaultValue="tab1" activationMode="automatic">
```

## API Reference

| Component | Description |
|-----------|-------------|
| Tabs | Root container |
| TabsList | Container for trigger buttons |
| TabsTrigger | Clickable tab button |
| TabsContent | Content panel for a tab |

### Tabs Props
| Prop | Type | Default |
|------|------|---------|
| defaultValue | string | - |
| value | string | controlled |
| onValueChange | (value: string) => void | - |
| activationMode | "automatic" \| "manual" | "automatic" |

### TabsList Props
| Prop | Type | Default |
|------|------|---------|
| className | string | - |
| loop | boolean | true |

### TabsTrigger Props
| Prop | Type | Default |
|------|------|---------|
| value | string | required |
| disabled | boolean | false |
| asChild | boolean | false |