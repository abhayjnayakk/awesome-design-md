# Free DESIGN.md Prompts

## Create A Visual Thesis

```text
Create an original visual thesis for this product.

Product:
[describe product]

Audience:
[describe audience]

Primary style family:
[technical precision / warm editorial / creator commerce / fintech trust / cinematic premium / documentation clarity]

Contrast style family:
[choose one]

Must feel:
[desired feeling]

Must not feel:
[anti-patterns]

Output:
1. One-sentence visual thesis
2. Color behavior
3. Typography behavior
4. Layout behavior
5. Component behavior
6. Do/don't rules
```

## Create A Starter DESIGN.md

```text
Create a starter DESIGN.md for this product using the visual thesis below.

Use YAML front matter for colors, typography, rounded, spacing, and components. Then write markdown sections for Overview, Colors, Typography, Layout, Elevation & Depth, Shapes, Components, and Do's and Don'ts.

Do not copy a famous brand directly. Create original token names and component rules.

Visual thesis:
[paste thesis]
```

## Apply DESIGN.md In A Codebase

```text
Before editing UI, read DESIGN.md and treat it as the visual source of truth.

Build this screen:
[screen]

Before coding, tell me:
1. Which tokens you will use
2. Which component rules apply
3. What user decision the screen supports
```

## Audit For Style Drift

```text
Audit this UI against DESIGN.md.

Find:
- Invented colors
- Inconsistent spacing
- Weak hierarchy
- Generic SaaS patterns
- Missing states
- Accessibility risks

Then propose the smallest fixes.
```
