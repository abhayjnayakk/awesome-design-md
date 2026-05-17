---
version: alpha
name: Editorial SaaS Starter
description: A warm, restrained design system for research tools, writing apps, analytics, and knowledge products.
colors:
  primary: "#1D1B16"
  on-primary: "#FAF7EF"
  accent: "#9F4A2E"
  on-accent: "#FFFFFF"
  surface: "#FAF7EF"
  surface-raised: "#FFFFFF"
  border: "#DDD5C8"
  text: "#1D1B16"
  text-muted: "#766F66"
typography:
  h1:
    fontFamily: Libre Baskerville
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.03em
  h2:
    fontFamily: Public Sans
    fontSize: 1.875rem
    fontWeight: 650
    lineHeight: 1.15
    letterSpacing: -0.025em
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.65
  body-sm:
    fontFamily: Public Sans
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: Public Sans
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.1em
rounded:
  sm: 3px
  md: 6px
  lg: 12px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px
  article-card:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 32px
  metadata:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 8px
  insight-callout:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
---

## Overview

Editorial SaaS Starter is for products where reading, synthesis, and credibility matter. The interface should feel warm, composed, and quietly authoritative.

## Colors

Use paper-like surfaces, deep ink text, and clay accent for important interaction. Keep metadata muted.

## Typography

Use serif type for narrative hierarchy and sans type for controls, data, navigation, and dense UI.

## Layout

Use generous margins and a clear reading path. Dashboards should feel composed, not crowded.

## Elevation & Depth

Depth should feel like paper on paper. Avoid glossy panels and heavy shadows.

## Shapes

Use modest radii. Large rounded cards can make the product too casual.

## Components

Article cards hold ideas or reports. Metadata should stay quiet. Insight callouts are rare and important.

## Do's and Don'ts

Do:

- Make reading comfortable.
- Use accent color sparingly.
- Let whitespace create authority.

Don't:

- Overuse serif type in controls.
- Turn every card into a marketing panel.
- Cram dashboards into dense grids.
