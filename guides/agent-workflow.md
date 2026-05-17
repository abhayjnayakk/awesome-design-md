# Agent Workflow

This is the fastest workflow for getting better UI from a coding agent.

## 1. Copy A DESIGN.md

Copy one file into your project root:

```text
your-project/
  DESIGN.md
  package.json
  src/
```

Use a starter example or a reference from:

```text
upstream/voltagent-awesome-design-md/design-md/
```

## 2. Ask For A Token Plan

Before code:

```text
Read DESIGN.md and summarize the tokens and component rules you will use for this screen. Do not write code yet.
```

## 3. Implement One Screen

```text
Build the [screen name] using DESIGN.md as the visual source of truth. Use existing tokens and component rules. Do not invent new colors, radii, spacing, typography, or shadows unless you explain why DESIGN.md is missing a necessary token.
```

## 4. Audit Drift

```text
Review the UI against DESIGN.md. Find invented styles, weak hierarchy, inconsistent spacing, missing states, and accessibility issues. Fix only the highest-impact problems.
```

## 5. Encode Learnings

If the agent repeatedly invents the same thing, add it to `DESIGN.md`:

- A color token
- A spacing token
- A component rule
- A do/don't rule
- A responsive behavior rule

## Cursor-Specific Prompt

```text
Before editing UI, read DESIGN.md. Treat it as the visual source of truth. Use its colors, typography, spacing, radius, component rules, and do/don't guidance. If something is missing, propose a DESIGN.md update before inventing new styles.
```

## Claude Code Prompt

```text
Use DESIGN.md as the design system for this task. First inspect it, then implement the requested UI using the existing tokens and component guidance. Keep changes scoped and explain any design-system gaps you find.
```
