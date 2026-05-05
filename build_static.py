#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from catalog_data import build_catalog_entries


BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "extracted_images"
STATIC_DIR = BASE_DIR / "static"


def render_index_html(hero_src: str) -> str:
    """
    Convert catalog.html (Flask/Jinja) into a standalone index.html for Pages:
    - hero image uses local static file under docs/static/
    - data loads from ./catalog.json (no /api calls)
    """
    template_path = BASE_DIR / "catalog.html"
    html = template_path.read_text(encoding="utf-8")

    # Replace Jinja hero block with plain HTML.
    # Keep the existing hero-bg container/classes so the aesthetic is identical.
    html = html.replace(
        """            {% if hero_img_src %}
            <div class="absolute inset-0 hero-bg">
                <img src="{{ hero_img_src }}" alt="" class="brightness-[0.88] contrast-[1.02]"/>
            </div>
            {% endif %}""",
        f"""            <div class="absolute inset-0 hero-bg">
                <img src="{hero_src}" alt="" class="brightness-[0.88] contrast-[1.02]"/>
            </div>""",
    )

    # Switch API fetches to static JSON (same origin).
    html = html.replace("fetch('/api/catalog')", "fetch('catalog.json')")
    html = html.replace("fetch('/api/categories')", "fetch('categories.json')")

    # Categories.json fetch will remain, but we will also ship categories.json.
    return html


def main() -> None:
    parser = argparse.ArgumentParser(description="Build static GitHub Pages site under docs/.")
    parser.add_argument("--out", type=Path, default=BASE_DIR / "docs", help="Output directory (default: docs/)")
    args = parser.parse_args()

    out_dir: Path = args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    if not IMAGES_DIR.is_dir():
        raise SystemExit(f"Missing images folder: {IMAGES_DIR}")

    # Data: use relative images path inside docs/
    catalog = build_catalog_entries(IMAGES_DIR, "images")
    categories = sorted({item["category"] for item in catalog})

    (out_dir / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False), encoding="utf-8")
    (out_dir / "categories.json").write_text(json.dumps(categories, ensure_ascii=False), encoding="utf-8")

    # Copy hero
    (out_dir / "static").mkdir(parents=True, exist_ok=True)
    hero_src = "static/hero.png"
    hero_file = STATIC_DIR / "hero.png"
    if hero_file.is_file():
        shutil.copy2(hero_file, out_dir / hero_src)

    # Copy images (this is the big part; required for “all photos on Pages”)
    images_out = out_dir / "images"
    images_out.mkdir(parents=True, exist_ok=True)
    for p in IMAGES_DIR.iterdir():
        if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png"}:
            shutil.copy2(p, images_out / p.name)

    # HTML
    (out_dir / "index.html").write_text(render_index_html(hero_src), encoding="utf-8")

    print(f"Built static site into: {out_dir}")
    print(f"- index.html: {(out_dir / 'index.html').resolve()}")
    print(f"- catalog.json: {(out_dir / 'catalog.json').resolve()}")
    print(f"- images/: {images_out.resolve()}")


if __name__ == "__main__":
    main()

