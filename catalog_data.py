from __future__ import annotations

from pathlib import Path
from typing import Iterable


def _pretty_title(token: str) -> str:
    """
    Title-case a token while preserving known abbreviations.
    """
    keep_upper = {"LR", "ITLR", "ITLRF", "ST", "TM", "PS", "GR"}
    t = token.strip()
    if not t:
        return t
    if t.upper() in keep_upper:
        return t.upper()
    # Normal title casing, but keep apostrophes sane.
    return t[:1].upper() + t[1:].lower()


def normalize_category(raw: str) -> str:
    """
    Convert filename-derived category strings into meaningful, consistent titles.
    Examples:
      BRACLET -> Bracelets
      N SET 1 -> Necklace Sets — Series 1
      COCKTAIL RING -> Cocktail Rings
    """
    s = str(raw or "")
    s = s.replace("_", " ").replace("-", " ").replace("dec", " ")
    s = " ".join(s.split())  # collapse whitespace
    if not s:
        return s

    upper = s.upper()

    # Fast-path for obvious typos / singular/plural normalization + curated labels
    direct = {
        "BRACLET": "Bracelets",
        "BRACELET": "Bracelets",
        "CHAIN SET": "Chain Sets",
        "COCKTAIL RING": "Cocktail Rings",
        "COCKTAIL RINGS": "Cocktail Rings",
        "COUPLE BAND": "Couple Bands",
        "DANGLER": "Danglers",
        "GENTS RING": "Gents Rings",
        "IT KADA": "Italian Kada",
        "KADA": "Kada",
        "N SET": "Necklace Sets",
        "P SET": "Pendant Sets",
        "P SETS": "Pendant Sets",
        "R RING": "Rings",
        "TOPS": "Earrings (Tops)",
        # Abbreviation-heavy buckets (best-effort interpretation for a polished site)
        "LR": "Ladies Rings",
        "LR VOL": "Ladies Rings — Vol.",
        "R KADA": "Rings — Kada",
        "TM": "Traditional Motifs",
        "TM SET": "Traditional Motifs — Sets",
        "ST": "Stone Collection",
        "ST LR": "Stone Collection — Ladies Rings",
        "ST PS": "Stone Collection — Pendant Sets",
        "ST TOPS": "Stone Collection — Stud Earrings",
        "ST GR YELLOW": "Stone Collection — Yellow Gold",
        "ITLR FINAL": "Italian Collection — Ladies Rings",
        "ITLRF FINAL": "Italian Collection — Ladies Rings",
    }

    # Handle "XYZ 1" style variants as series/volume labels.
    parts = s.split()
    if parts and parts[-1].isdigit():
        base = " ".join(parts[:-1]).strip()
        num = parts[-1]
        base_upper = base.upper()

        # Prefer nicer labels for known patterns.
        if base_upper == "LR VOL":
            return f"Ladies Rings — Vol. {num}"

        base_norm = direct.get(base_upper, None)
        if base_norm is None:
            base_norm = " ".join(_pretty_title(t) for t in base.split())

        # If base already has a structured label, treat the digit as a series.
        return f"{base_norm} — Series {num}"

    if upper in direct:
        return direct[upper]

    # Normalize "Final" suffixes into a cleaner collection label.
    # e.g. "ITLR Final" (unknown) -> "Itlr Collection"
    if upper.endswith(" FINAL"):
        base = s[:-6].strip()
        # If it's a known base, use it; otherwise create a clean "… Collection" label.
        base_norm = direct.get(base.upper(), None)
        if base_norm is None:
            base_norm = " ".join(_pretty_title(t) for t in base.split())
        # Avoid duplicating "Collection" if base_norm already includes it.
        return base_norm if "Collection" in base_norm else f"{base_norm} Collection"

    # Default: nice casing while keeping abbreviations like LR / ST / TM.
    return " ".join(_pretty_title(t) for t in s.split())


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

        category_display = normalize_category(category)

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

