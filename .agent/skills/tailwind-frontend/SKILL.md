---
name: tailwind-frontend
description: >
  Best practices and patterns for using Tailwind CSS in the Food Store frontend.
  Trigger: When writing React components, styling the UI, or configuring Tailwind.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## When to Use

- Styling React components in the `frontend` directory.
- Creating reusable UI components in `shared/ui`.
- Implementing responsive layouts and dark mode.
- Configuring the design system in `tailwind.config.js`.

## Critical Patterns

- **Utility-First**: Use Tailwind classes directly in the `className` prop. Avoid custom CSS files.
- **Mobile-First**: Always start styling for mobile and use prefix modifiers (`md:`, `lg:`, etc.) for larger screens.
- **Consistency**: Use the design system tokens for colors and spacing. Never hardcode hex values if a token exists.
- **Encapsulation**: Styles for a specific feature should be contained within that feature's components (Feature-Sliced Design).
- **Avoid @apply**: Do not use `@apply` to create "component classes" (e.g., `.btn-primary`). Prefer creating a React component that encapsulates the classes.

## Code Examples

### Reusable Button Component
```tsx
// src/shared/ui/Button.tsx
interface Props extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary';
}

export const Button = ({ variant = 'primary', className, ...props }: Props) => {
  const baseStyles = "px-4 py-2 rounded-lg font-medium transition-colors duration-200 focus:outline-none focus:ring-2";
  const variants = {
    primary: "bg-orange-600 text-white hover:bg-orange-700 focus:ring-orange-500",
    secondary: "bg-gray-200 text-gray-800 hover:bg-gray-300 focus:ring-gray-400"
  };

  return (
    <button 
      className={`${baseStyles} ${variants[variant]} ${className}`} 
      {...props} 
    />
  );
};
```

### Responsive Grid
```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 p-4">
  {/* Content */}
</div>
```

## Commands

```bash
# Add Tailwind CSS to the project (Vite)
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

## Resources

- **Documentation**: See [Tailwind CSS Official Docs](https://tailwindcss.com/docs)
