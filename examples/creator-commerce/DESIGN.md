---
version: alpha
name: Creator Commerce Starter
description: A bold, clear design system for creator stores, digital products, marketplaces, and checkout flows.
colors:
  primary: "#111111"
  on-primary: "#FFF8E7"
  accent: "#FFB000"
  on-accent: "#111111"
  secondary: "#EF476F"
  on-secondary: "#111111"
  surface: "#FFF8E7"
  surface-raised: "#FFFFFF"
  border: "#111111"
  text: "#111111"
  text-muted: "#5F574A"
typography:
  h1:
    fontFamily: Archivo Black
    fontSize: 3.5rem
    fontWeight: 900
    lineHeight: 0.98
    letterSpacing: -0.04em
  h2:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: -0.03em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 500
    lineHeight: 1.5
  label:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: 0.06em
rounded:
  sm: 4px
  md: 10px
  lg: 20px
  pill: 999px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 14px
  price-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 8px
  product-card:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  callout:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 24px
---

## Overview

Creator Commerce Starter is for products that help people sell, publish, and package creative work. The interface should feel direct, memorable, and commercially clear.

## Colors

Use black for structure, cream for warmth, yellow for price and commerce energy, and pink only for expressive moments.

## Typography

Use heavy display type for confident headlines. Keep product details and checkout text simple and readable.

## Layout

Buying actions should be close to value, price, and proof. Product cards should feel tangible.

## Elevation & Depth

Use hard borders and layered surfaces rather than soft SaaS shadows.

## Shapes

Pill buttons make buying and publishing feel approachable. Rounded cards add warmth.

## Components

Product cards carry the offer. Price badges must be obvious. Primary buttons should be direct and action-oriented.

## Do's and Don'ts

Do:

- Show price clearly.
- Make the primary action impossible to miss.
- Keep copy human.

Don't:

- Hide commerce behind vague CTAs.
- Use low-contrast pastel text.
- Make every element playful at once.
