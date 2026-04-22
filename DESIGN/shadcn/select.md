# SELECT — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add select
```

## Usage
```tsx
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
```

## Basic Select
```tsx
<Select>
  <SelectTrigger>
    <SelectValue placeholder="Select a fruit" />
  </SelectTrigger>
  <SelectContent>
    <SelectItem value="apple">Apple</SelectItem>
    <SelectItem value="banana">Banana</SelectItem>
    <SelectItem value="orange">Orange</SelectItem>
  </SelectContent>
</Select>
```

## With Groups
```tsx
<Select>
  <SelectTrigger>
    <SelectValue placeholder="Select a timezone" />
  </SelectTrigger>
  <SelectContent>
    <SelectGroup>
      <SelectLabel>Europe</SelectLabel>
      <SelectItem value="istanbul">Istanbul</SelectItem>
      <SelectItem value="london">London</SelectItem>
    </SelectGroup>
    <SelectGroup>
      <SelectLabel>Asia</SelectLabel>
      <SelectItem value="tokyo">Tokyo</SelectItem>
    </SelectGroup>
  </SelectContent>
</Select>
```

## Disabled Item
```tsx
<SelectItem value="unavailable" disabled>Unavailable</SelectItem>
```

## API Reference

| Component | Description |
|-----------|-------------|
| Select | Root container |
| SelectTrigger | Button that opens dropdown |
| SelectValue | Displays selected value (like placeholder) |
| SelectContent | Dropdown panel |
| SelectItem | Individual option |
| SelectGroup | Groups label + items |
| SelectLabel | Group header text |

### Select Props
| Prop | Type | Default |
|------|------|---------|
| value | string | - |
| onValueChange | (value: string) => void | - |
| defaultValue | string | - |
| disabled | boolean | false |

### SelectItem Props
| Prop | Type | Default |
|------|------|---------|
| value | string | required |
| disabled | boolean | false |
| label | string | uses text content |