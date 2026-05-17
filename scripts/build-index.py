from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DESIGN_ROOT = ROOT / "upstream" / "voltagent-awesome-design-md" / "design-md"
OUT = ROOT / "REFERENCE_INDEX.md"


def titleize(slug: str) -> str:
    special = {
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
    rows = []
    for path in sorted(DESIGN_ROOT.iterdir()):
        if not path.is_dir():
            continue
        design = path / "DESIGN.md"
        preview = path / "preview.html"
        preview_dark = path / "preview-dark.html"
        if design.exists():
            rows.append((path.name, design, preview, preview_dark))

    lines = [
        "# Reference Index",
        "",
        "Generated index of included DESIGN.md references.",
        "",
        "| Name | DESIGN.md | Preview | Dark Preview |",
        "|------|-----------|---------|--------------|",
    ]

    for slug, design, preview, preview_dark in rows:
        name = titleize(slug)
        design_link = design.relative_to(ROOT)
        preview_link = preview.relative_to(ROOT) if preview.exists() else ""
        preview_dark_link = preview_dark.relative_to(ROOT) if preview_dark.exists() else ""
        lines.append(
            f"| {name} | [`DESIGN.md`]({design_link}) | "
            f"{f'[`preview.html`]({preview_link})' if preview_link else '-'} | "
            f"{f'[`preview-dark.html`]({preview_dark_link})' if preview_dark_link else '-'} |"
        )

    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} with {len(rows)} references")


if __name__ == "__main__":
    main()
