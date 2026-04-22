# Dialog — shadcn/ui

## Installation
```
pnpm dlx shadcn@latest add dialog
```

## Usage
```tsx
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogFooter,
  DialogClose,
} from "@/components/ui/dialog"
```

## Basic Dialog
```tsx
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Edit Profile</DialogTitle>
      <DialogDescription>Make changes to your profile.</DialogDescription>
    </DialogHeader>
    <div className="py-4">{/* content */}</div>
    <DialogFooter>
      <DialogClose asChild>
        <Button variant="outline">Cancel</Button>
      </DialogClose>
      <Button type="submit">Save changes</Button>
    </DialogFooter>
  </DialogContent>
</Dialog>
```

## Alert Dialog (Destructive)
```tsx
<AlertDialog>
  <AlertDialogTrigger>Delete</AlertDialogTrigger>
  <AlertDialogContent>
    <AlertDialogHeader>
      <AlertDialogTitle>Delete Account</AlertDialogTitle>
      <AlertDialogDescription>
        This action cannot be undone.
      </AlertDialogDescription>
    </AlertDialogHeader>
    <AlertDialogFooter>
      <AlertDialogCancel>Cancel</AlertDialogCancel>
      <AlertDialogAction asChild>
        <Button variant="destructive">Delete</Button>
      </AlertDialogAction>
    </AlertDialogFooter>
  </AlertDialogContent>
</AlertDialog>
```

## Custom Size
```tsx
<DialogContent className="max-w-2xl">  {/* wide dialog */}</DialogContent>
<DialogContent className="max-w-sm">  {/* narrow dialog */}</DialogContent>
```

## API Reference

| Component | Description |
|-----------|-------------|
| Dialog | Root container |
| DialogTrigger | Wraps the button that opens dialog |
| DialogContent | Modal content (replaces native dialog) |
| DialogHeader | Header block with title + description |
| DialogTitle | Title heading |
| DialogDescription | Description text |
| DialogFooter | Bottom actions |
| DialogClose | Close button (asChild supported) |

### Dialog Props
| Prop | Type | Default |
|------|------|---------|
| open | boolean | - |
| onOpenChange | (open: boolean) => void | - |
| modal | boolean | true |