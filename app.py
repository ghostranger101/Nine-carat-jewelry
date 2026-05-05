"""
Jewelry Catalog Web App
A Flask application to display extracted jewelry images in a luxury catalog format.
"""

import os

from flask import Flask, jsonify, render_template_string, send_from_directory
from pathlib import Path

from catalog_data import build_catalog_entries, hero_from_catalog

app = Flask(__name__)

# Configuration
BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "extracted_images"
CATALOG_TITLE = "Nine carat jewelry"
HERO_IMAGE_PATH = BASE_DIR / "static" / "hero.png"
HERO_IMAGE_URL = "/static/hero.png"


def get_catalog_data():
    """Extract metadata from image filenames and return structured data."""
    return build_catalog_entries(IMAGES_DIR, "/images")


def get_hero_image_src(catalog):
    """Choose a hero image from extracted catalog images, avoiding filenames that imply text or logos."""
    return hero_from_catalog(catalog)


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
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "").strip() == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
