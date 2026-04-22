# Input — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add input
```

## Usage
```tsx
import { Input } from "@/components/ui/input"
<Input />
```

## With Field (Label + Description)
```tsx
import { Field, FieldLabel, FieldDescription } from "@/components/ui/field"
<Field>
  <FieldLabel>Username</FieldLabel>
  <Input />
  <FieldDescription>Choose a unique username.</FieldDescription>
</Field>
```

## Variants
```tsx
<Input disabled />           // Disabled state
<Input aria-invalid />       // Invalid state  
<Input type="file" />        // File input
<Input required />           // Required field
```

## Field Group (Forms)
```tsx
import { Field, FieldGroup, FieldLabel } from "@/components/ui/field"

<FieldGroup>
  <Field>
    <FieldLabel>Name</FieldLabel>
    <Input />
  </Field>
  <Field>
    <FieldLabel>Email</FieldLabel>
    <Input type="email" />
  </Field>
</FieldGroup>
```

## Grid Layout
```tsx
<div className="grid grid-cols-2 gap-4">
  <Field><FieldLabel>First Name</FieldLabel><Input /></Field>
  <Field><FieldLabel>Last Name</FieldLabel><Input /></Field>
</div>
```

## Inline with Button
```tsx
<div className="flex gap-2">
  <Input placeholder="Search..." />
  <Button>Search</Button>
</div>
```

## API Reference

| Prop | Type |
|------|------|
| type | "text" \| "email" \| "password" \| "file" \| ... |
| disabled | boolean |
| aria-invalid | boolean |
| required | boolean |
| className | string |