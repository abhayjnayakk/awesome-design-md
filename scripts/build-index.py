from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN_ROOT = ROOT / "upstream" / "voltagent-awesome-design-md" / "design-md"
OUT = ROOT / "REFERENCE_INDEX.md"

CATEGORIES = {
    "AI & LLM Platforms": [
        "claude", "cohere", "elevenlabs", "minimax", "mistral.ai", "ollama",
        "opencode.ai", "replicate", "runwayml", "together.ai", "voltagent", "x.ai",
    ],
    "Developer Tools & IDEs": [
        "cursor", "expo", "lovable", "raycast", "superhuman", "vercel", "warp",
    ],
    "Backend, Database & DevOps": [
        "clickhouse", "composio", "hashicorp", "mongodb", "posthog", "sanity", "sentry", "supabase",
    ],
    "Productivity & SaaS": [
        "cal", "intercom", "linear.app", "mintlify", "notion", "resend", "slack", "zapier",
    ],
    "Design & Creative Tools": [
        "airtable", "clay", "figma", "framer", "miro", "webflow",
    ],
    "Fintech & Crypto": [
        "binance", "coinbase", "kraken", "mastercard", "revolut", "stripe", "wise",
    ],
    "E-commerce & Retail": [
        "airbnb", "meta", "nike", "shopify", "starbucks",
    ],
    "Media & Consumer Tech": [
        "apple", "hp", "ibm", "nvidia", "pinterest", "playstation", "spacex",
        "spotify", "theverge", "uber", "vodafone", "wired",
    ],
    "Automotive": [
        "bmw", "bmw-m", "bugatti", "ferrari", "lamborghini", "renault", "tesla",
    ],
}


def titleize(slug: str) -> str:
    special = {
        "bmw": "BMW",
        "cal": "Cal.com",
        "clickhouse": "ClickHouse",
        "elevenlabs": "ElevenLabs",
        "hp": "HP",
        "ibm": "IBM",
        "mongodb": "MongoDB",
        "nvidia": "NVIDIA",
        "playstation": "PlayStation",
        "posthog": "PostHog",
        "spacex": "SpaceX",
        "theverge": "The Verge",
        "voltagent": "VoltAgent",
        "wired": "WIRED",
        "x.ai": "xAI",
        "linear.app": "Linear",
        "bmw-m": "BMW M",
        "opencode.ai": "OpenCode AI",
        "mistral.ai": "Mistral AI",
        "together.ai": "Together AI",
        "runwayml": "Runway",
    }
    if slug in special:
        return special[slug]
    return slug.replace("-", " ").replace(".", " ").title()


def main() -> None:
    available = {}
    for path in sorted(DESIGN_ROOT.iterdir()):
        if not path.is_dir():
            continue
        design = path / "DESIGN.md"
        if design.exists():
            available[path.name] = design

    lines = [
        "# Reference Index",
        "",
        "Generated index of included `DESIGN.md` references.",
        "",
        "Each entry links to a local `DESIGN.md` file copied from the attributed upstream MIT collection.",
        "",
        "## Best Starting Points",
        "",
        "| Building | Start with | Why |",
        "|----------|------------|-----|",
        "| AI agent SaaS | `vercel`, `cursor`, `voltagent` | Developer precision, AI-native surfaces, agent workflow energy |",
        "| AI assistant | `claude`, `notion`, `linear.app` | Warm explanation, calm hierarchy, focused productivity |",
        "| Developer API | `vercel`, `supabase`, `mintlify` | Docs, code blocks, trust, and technical clarity |",
        "| Fintech product | `stripe`, `wise`, `coinbase` | Trust, validation, pricing, and transaction clarity |",
        "| Creator commerce | `shopify`, `airbnb`, `nike` | Product cards, buying confidence, and visual momentum |",
        "| Premium hardware | `apple`, `tesla`, `spacex` | Product focus, cinematic whitespace, and confident restraint |",
        "",
    ]

    seen = set()
    for category, slugs in CATEGORIES.items():
        rows = [(slug, available[slug]) for slug in slugs if slug in available]
        if not rows:
            continue
        lines.extend([f"## {category}", "", "| Name | DESIGN.md |", "|------|-----------|"])
        for slug, design in rows:
            seen.add(slug)
            lines.append(f"| {titleize(slug)} | [`DESIGN.md`]({design.relative_to(ROOT)}) |")
        lines.append("")

    uncategorized = sorted(set(available) - seen)
    if uncategorized:
        lines.extend(["## Other", "", "| Name | DESIGN.md |", "|------|-----------|"])
        for slug in uncategorized:
            design = available[slug]
            lines.append(f"| {titleize(slug)} | [`DESIGN.md`]({design.relative_to(ROOT)}) |")
        lines.append("")

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} with {len(available)} references")


if __name__ == "__main__":
    main()
