# Awesome DESIGN.md

Copy a `DESIGN.md` into your project, tell your AI agent "build me a page that looks like this" and get UI that actually matches.

![Awesome DESIGN.md cover](assets/design-oss.png)

## What is DESIGN.md?

`DESIGN.md` is a new plain-text design system document that AI agents read to generate consistent UI.

It is just a markdown file. No Figma exports, no JSON schemas, no special tooling. Drop it into your project root and any AI coding agent can understand how your UI should look. Markdown is the format LLMs read best, so there is nothing complicated to parse or configure.

| File | Who reads it | What it defines |
|------|--------------|-----------------|
| `AGENTS.md` | Coding agents | How to build the project |
| `DESIGN.md` | Design agents | How the project should look and feel |

This repo provides a curated `DESIGN.md` style gallery, an included MIT-licensed reference collection, original starter examples, prompts, and workflow guidance for AI builders.

## Why This Exists

Most AI-generated apps look the same because the design prompt is vague: "modern SaaS UI," "clean dashboard," "make it beautiful."

`DESIGN.md` gives agents design memory:

- Color roles
- Typography rules
- Component styling
- Layout principles
- Depth and elevation
- Do's and don'ts
- Agent prompt guidance

## Quick Start

1. Pick a category from the collection below.
2. Open [`style-taxonomy.md`](style-taxonomy.md) to choose a style family.
3. Browse [`REFERENCE_INDEX.md`](REFERENCE_INDEX.md) for ready-to-use references.
4. Try one of the starter files in [`examples/`](examples/).
5. Copy a `DESIGN.md` into your project root.
6. Tell your AI agent to use it.

```text
Before editing UI, read DESIGN.md and treat it as the visual source of truth. Use its colors, typography, spacing, component rules, and do/don't guidance.
```

## Request / Premium Shortcut

Want the faster ready-made workflow?

Get the **73 DESIGN.md Styles Swipe File For AI Builders**: style chooser, remix-not-copy guide, Cursor workflow, launch recipes, full prompt pack, and Gumroad-ready assets.

Limited launch price: `$5` instead of `$29`.

## Included Reference Library

This repo includes a copy of the MIT-licensed `design-md` collection from [`VoltAgent/awesome-design-md`](https://github.com/VoltAgent/awesome-design-md), preserved under:

```text
upstream/voltagent-awesome-design-md/
```

Browse the generated reference index:

[`REFERENCE_INDEX.md`](REFERENCE_INDEX.md)

Each reference may include:

| File | Purpose |
|------|---------|
| `DESIGN.md` | The design system agents read |
| `preview.html` | Visual catalog showing colors, type, buttons, and cards |
| `preview-dark.html` | Same catalog with dark surfaces |

This repo adds selection guidance, prompts, starter examples, and workflow docs on top of the upstream collection.

## Collection

### AI & LLM Platforms

- **Claude** — Warm terracotta accent, clean editorial layout.
- **Cohere** — Enterprise AI platform with vibrant gradients and data-rich dashboard energy.
- **ElevenLabs** — Dark cinematic UI with audio-waveform aesthetics.
- **Minimax** — Bold dark interface with neon accents.
- **Mistral AI** — French-engineered minimalism, purple-toned.
- **Ollama** — Terminal-first, monochrome simplicity.
- **OpenCode AI** — Developer-centric dark theme.
- **Replicate** — Clean white canvas, code-forward.
- **Runway** — Cinematic dark heroes, paper-white reading bands, pure black pill CTAs.
- **Together AI** — Technical, blueprint-style AI infrastructure.
- **VoltAgent** — Void-black canvas, emerald accent, terminal-native.
- **xAI** — Stark monochrome, futuristic minimalism.

### Developer Tools & IDEs

- **Cursor** — AI-first code editor with sleek dark interface and gradient accents.
- **Expo** — Dark theme, tight letter-spacing, code-centric.
- **Lovable** — Playful gradients, friendly dev aesthetic.
- **Raycast** — Sleek dark chrome, vibrant gradient accents.
- **Superhuman** — Premium dark UI, keyboard-first, purple glow.
- **Vercel** — Black and white precision, Geist-like developer clarity.
- **Warp** — Modern terminal with dark IDE-like interface and block-based command UI.

### Backend, Database & DevOps

- **ClickHouse** — Yellow-accented, technical documentation style.
- **Composio** — Modern dark interface with colorful integration icons.
- **HashiCorp** — Enterprise-clean, black and white.
- **MongoDB** — Green branding, developer documentation focus.
- **PostHog** — Playful product analytics with developer-friendly dark UI.
- **Sanity** — Dark-first editorial marketing surface with coral-red highest-priority CTA.
- **Sentry** — Dark dashboard, data-dense, pink-purple accent.
- **Supabase** — Dark emerald theme, code-first.

### Productivity & SaaS

- **Cal.com** — Clean neutral UI, developer-oriented simplicity.
- **Intercom** — Friendly blue palette, conversational UI patterns.
- **Linear** — Ultra-minimal, precise, purple accent.
- **Mintlify** — Clean, green-accented, reading-optimized.
- **Notion** — Warm minimalism, serif headings, soft surfaces.
- **Resend** — Minimal dark theme, monospace accents.
- **Zapier** — Warm orange, friendly automation aesthetic.

### Design & Creative Tools

- **Airtable** — Colorful, friendly, structured data aesthetic.
- **Clay** — Organic shapes, soft gradients, art-directed layout.
- **Figma** — Vibrant multi-color, playful yet professional.
- **Framer** — Bold black and blue, motion-first, design-forward.
- **Miro** — Bright yellow accent, infinite canvas aesthetic.
- **Webflow** — Blue-accented, polished marketing site aesthetic.

### Fintech & Crypto

- **Binance** — Bold yellow on monochrome, trading-floor urgency.
- **Coinbase** — Clean blue identity, trust-focused, institutional feel.
- **Kraken** — Purple-accented dark UI, data-dense dashboards.
- **Mastercard** — Warm cream canvas, orbital pill shapes, editorial warmth.
- **Revolut** — Sleek dark interface, gradient cards, fintech precision.
- **Stripe** — Signature purple gradients, infrastructure polish.
- **Wise** — Bright green accent, friendly and clear.

### E-commerce & Retail

- **Airbnb** — Warm coral accent, photography-driven, rounded UI.
- **Meta** — Photography-first, binary light/dark surfaces, blue CTAs.
- **Nike** — Monochrome UI, massive uppercase display, full-bleed photography.
- **Shopify** — Dark-first cinematic, neon green accent, ultra-light display type.
- **Starbucks** — Earth-green system, warm cream canvas, retail warmth.

### Media & Consumer Tech

- **Apple** — Premium white space, SF Pro-style clarity, cinematic imagery.
- **HP** — Pure white canvas, electric blue signal CTA, geometric decoration.
- **IBM** — Carbon-like structure, enterprise blue palette.
- **NVIDIA** — Green-black energy, technical power aesthetic.
- **Pinterest** — Red accent, masonry grid, image-first.
- **PlayStation** — Three-surface channel layout, cyan hover-scale interaction.
- **SpaceX** — Stark black and white, full-bleed imagery, futuristic confidence.
- **Spotify** — Vibrant green on dark, bold type, album-art-driven.
- **The Verge** — Acid-mint and ultraviolet accents, high-energy editorial.
- **Uber** — Bold black and white, tight type, urban energy.
- **Vodafone** — Monumental uppercase display, red chapter bands.
- **WIRED** — Paper-white broadsheet density, custom serif feel, ink-blue links.

### Automotive

- **BMW** — Dark premium surfaces, precise German engineering aesthetic.
- **BMW M** — Motorsport contrast, M color accents, precision-driven layout.
- **Bugatti** — Cinema-black canvas, monochrome austerity, monumental display type.
- **Ferrari** — Chiaroscuro black-white editorial, red with extreme sparseness.
- **Lamborghini** — True black cathedral, gold accent, neo-grotesk luxury.
- **Renault** — Vivid aurora gradients, zero-radius buttons.
- **Tesla** — Radical subtraction, cinematic full-viewport photography.

## Free Starter DESIGN.md Files

This repo includes original starter systems you can use immediately:

| File | Use case |
|------|----------|
| [`examples/ai-devtool/DESIGN.md`](examples/ai-devtool/DESIGN.md) | AI tools, agent dashboards, developer infrastructure |
| [`examples/creator-commerce/DESIGN.md`](examples/creator-commerce/DESIGN.md) | Creator stores, digital products, marketplaces |
| [`examples/editorial-saas/DESIGN.md`](examples/editorial-saas/DESIGN.md) | Research tools, writing apps, knowledge products |

These examples lint with `npx @google/design.md lint` with zero errors. Some warnings are expected because starter palettes include useful roles that small sample component sets may not reference yet.

## Guides

- [`guides/choose-a-style.md`](guides/choose-a-style.md) — pick a style based on what you are building.
- [`guides/agent-workflow.md`](guides/agent-workflow.md) — apply `DESIGN.md` with Cursor, Claude Code, or another coding agent.
- [`guides/remix-safely.md`](guides/remix-safely.md) — use references without cloning brands.
- [`prompts/free-prompts.md`](prompts/free-prompts.md) — free prompts for creating, applying, and auditing `DESIGN.md`.

## What's Inside Each DESIGN.md

Every strong `DESIGN.md` should capture:

| # | Section | What it captures |
|---|---------|------------------|
| 1 | Visual Theme & Atmosphere | Mood, density, design philosophy |
| 2 | Color Palette & Roles | Semantic name, hex value, functional role |
| 3 | Typography Rules | Font families, hierarchy, rhythm |
| 4 | Component Stylings | Buttons, cards, inputs, navigation, states |
| 5 | Layout Principles | Spacing scale, grid, whitespace philosophy |
| 6 | Depth & Elevation | Shadow system, surface hierarchy |
| 7 | Do's and Don'ts | Design guardrails and anti-patterns |
| 8 | Responsive Behavior | Breakpoints, touch targets, collapsing strategy |
| 9 | Agent Prompt Guide | Quick reference and ready-to-use prompts |

## How to Use

1. Copy a `DESIGN.md` into your project root.
2. Tell your AI agent to use it.
3. Ask for a token plan before code.
4. Review the generated UI for style drift.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines.

- Improve taxonomy and prompts.
- Add original starter examples.
- Report weak descriptions or missing guidance.
- Open an issue before large changes.

## License

MIT License. See [`LICENSE`](LICENSE).

This repository includes original workflow guidance and starter `DESIGN.md` files plus an attributed MIT-licensed upstream reference collection. Brand names mentioned in the collection are descriptive references only. We do not claim ownership of any company's visual identity. See [`ATTRIBUTION.md`](ATTRIBUTION.md) and [`UPSTREAM_NOTICE.md`](UPSTREAM_NOTICE.md).
