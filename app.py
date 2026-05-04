"""
Jewelry Catalog Web App
A Flask application to display extracted jewelry images in a luxury catalog format.
"""

from flask import Flask, render_template_string, jsonify, send_from_directory
from pathlib import Path
import json

app = Flask(__name__)

# Configuration
BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = Path("extracted_images")
CATALOG_TITLE = "Nine carat jewelry"
HERO_IMAGE_PATH = BASE_DIR / "static" / "hero.png"
HERO_IMAGE_URL = "/static/hero.png"


def get_catalog_data():
    """Extract metadata from image filenames and return structured data."""
    if not IMAGES_DIR.exists():
        return []

    catalog = []
    images = sorted(IMAGES_DIR.glob("*.jpeg")) + sorted(IMAGES_DIR.glob("*.jpg")) + sorted(IMAGES_DIR.glob("*.png"))

    for idx, image_path in enumerate(images, start=1):
        filename = image_path.stem
        parts = filename.split("_")
        
        # Parse filename: BRACLET_p1_0 -> category, page, index
        if len(parts) >= 2:
            category = "_".join(parts[:-2])  # e.g., "BRACLET", "P SET"
            page_num = parts[-2].replace("p", "")  # e.g., "1"
            img_index = parts[-1]  # e.g., "0"
        else:
            category = filename
            page_num = "1"
            img_index = "0"

        # Clean up category names for display
        category_display = category.replace("-", " ").replace("dec", "").strip()
        
        catalog.append({
            "id": idx,
            "filename": image_path.name,
            "src": f"/images/{image_path.name}",
            "design_number": f"Design {idx:03d}",
            "page": page_num,
            "material": "9-carat gold jewelry",
            "category": category_display,
        })

    return catalog


def get_hero_image_src(catalog):
    """Choose a hero image from extracted catalog images, avoiding filenames that imply text or logos."""
    if not catalog:
        return None

    blacklist_keywords = {"logo", "text", "watermark", "page", "p", "cover", "header"}
    for item in catalog:
        name = item["filename"].lower()
        if not any(keyword in name for keyword in blacklist_keywords):
            return item["src"]

    return catalog[0]["src"]


@app.route("/")
def index():
    catalog = get_catalog_data()
    if HERO_IMAGE_PATH.is_file():
        hero_img_src = HERO_IMAGE_URL
    else:
        hero_img_src = get_hero_image_src(catalog)
    with open("catalog.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return render_template_string(html_content, hero_img_src=hero_img_src or "")


@app.route("/api/categories")
def api_categories():
    catalog = get_catalog_data()
    categories = sorted(set(item["category"] for item in catalog))
    return jsonify(categories)


@app.route("/api/catalog")
def api_catalog():
    return jsonify(get_catalog_data())


@app.route("/images/<path:filename>")
def serve_image(filename):
    return send_from_directory(IMAGES_DIR, filename)


if __name__ == "__main__":
    print(f"Starting {CATALOG_TITLE} Catalog Web App...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host="0.0.0.0", port=5000)
