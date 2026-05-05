from __future__ import annotations

from pathlib import Path
from typing import Iterable


def iter_image_files(images_dir: Path) -> list[Path]:
    images = []
    for ext in ("*.jpeg", "*.jpg", "*.png"):
        images.extend(sorted(images_dir.glob(ext)))
    return images


def build_catalog_entries(images_dir: Path, image_base: str) -> list[dict]:
    """
    Build the catalog array used by both Flask (dev) and static JSON (Pages).

    Filenames are assumed like: BRACLET_p1_0.jpg -> category, page, index
    """
    if not images_dir.exists():
        return []

    base = image_base.rstrip("/")
    images = iter_image_files(images_dir)
    catalog: list[dict] = []

    for idx, image_path in enumerate(images, start=1):
        filename = image_path.stem
        parts = filename.split("_")

        if len(parts) >= 2:
            category = "_".join(parts[:-2])
            page_num = parts[-2].replace("p", "")
        else:
            category = filename
            page_num = "1"

        category_display = category.replace("-", " ").replace("dec", "").strip()

        catalog.append(
            {
                "id": idx,
                "filename": image_path.name,
                "src": f"{base}/{image_path.name}" if base else image_path.name,
                "design_number": f"Design {idx:03d}",
                "page": page_num,
                "material": "9-carat gold jewelry",
                "category": category_display,
            }
        )

    return catalog


def hero_from_catalog(catalog: Iterable[dict]) -> str | None:
    """
    Choose a hero image src from catalog entries.
    """
    items = list(catalog)
    if not items:
        return None

    blacklist_keywords = {"logo", "text", "watermark", "page", "p", "cover", "header"}
    for item in items:
        name = str(item.get("filename", "")).lower()
        if not any(keyword in name for keyword in blacklist_keywords):
            return str(item.get("src") or "")

    return str(items[0].get("src") or "")

