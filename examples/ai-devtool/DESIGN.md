---
version: alpha
name: AI Devtool Starter
description: A precise, readable design system for AI developer tools, agent dashboards, and infrastructure products.
colors:
  primary: "#0B1020"
  on-primary: "#F8FAFC"
  accent: "#22C55E"
  on-accent: "#06120A"
  surface: "#F8FAFC"
  surface-raised: "#FFFFFF"
  surface-inverse: "#111827"
  border: "#CBD5E1"
  text: "#0F172A"
  text-muted: "#64748B"
typography:
  h1:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.04em
  h2:
    fontFamily: Inter
    fontSize: 1.75rem
    fontWeight: 650
    lineHeight: 1.15
    letterSpacing: -0.025em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  mono-sm:
    fontFamily: JetBrains Mono
    fontSize: 0.8125rem
    fontWeight: 450
    lineHeight: 1.45
  label:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
rounded:
  sm: 4px
  md: 8px
  lg: 14px
spacing:
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px
  status-active:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 8px
  panel:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 24px
  code-block:
    backgroundColor: "{colors.surface-inverse}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-sm}"
    rounded: "{rounded.md}"
    padding: 16px
---

## Overview

AI Devtool Starter is for products that help builders configure, observe, or operate AI systems. The interface should feel precise, calm, inspectable, and useful under pressure.

## Colors

Use graphite for authority, white surfaces for inspection, and green accent for active or successful system state. Do not use accent color as decoration.

## Typography

Use Inter for product UI and JetBrains Mono for logs, code, IDs, traces, and agent output.

## Layout

Prefer persistent workspaces, side navigation, panels, and inspector surfaces. Keep the primary action close to the system state it affects.

## Elevation & Depth

Use subtle border and surface changes before shadows. Depth should show active work areas and overlays.

## Shapes

Small radii communicate technical precision. Use `lg` only for major panels.

## Components

Buttons should feel operational. Panels should contain real system artifacts. Code blocks should be readable and copy-friendly.

## Do's and Don'ts

Do:

- Label state clearly.
- Make agent actions inspectable.
- Keep code and logs legible.

Don't:

- Add generic AI gradients.
- Center the whole product around a chat bubble.
- Hide failure or waiting states.
