# Jewelry Catalog Web App

A responsive web application to display extracted jewelry catalog images with a luxury, modern aesthetic. Works on desktop, tablet, and mobile devices.

## Features

- **Responsive Design** — Optimized for all screen sizes (mobile, tablet, desktop)
- **Luxury Aesthetic** — Premium dark theme with gold accents
- **Fast Loading** — Lazy-loaded image grid with pagination
- **REST API** — JSON API endpoint for catalog data
- **Self-Contained** — Minimal dependencies, easy to deploy

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python app.py
```

Then open your browser to:
```
http://localhost:5000
```

Or for mobile/other devices on your network:
```
http://<your-ip>:5000
```

## File Structure

```
Catalouge/
├── app.py              Flask web server
├── catalog.html      Frontend (Tailwind CDN)
├── static/             Static assets (e.g. hero image)
├── extracted_images/   Local JPEG/PNG catalog (not in git; add your own)
└── requirements.txt
```

Place catalog images in `extracted_images/` on the machine that runs the app. That folder is listed in `.gitignore` so clones stay small and `git push` stays reliable.

## API Endpoints

- `GET /` — Main catalog page
- `GET /api/catalog` — JSON catalog data with all images
- `GET /images/<filename>` — Individual image file

## Catalog Data Structure

Each catalog item includes:
- `id` — Design identifier
- `filename` — Image filename
- `src` — Image URL
- `design_number` — Formatted design number
- `material` — Material description
- `price` — Price display
- `category` — Product category

## Customization

Edit `app.py` to modify:
- Catalog title: `CATALOG_TITLE = "AURELIAN"`
- Items per page: `itemsPerPage = 12` (in catalog.html)
- Price calculation: See `get_catalog_data()`
- Gold theme color: `#D4AF37`

## Adding designs

Export or copy JPEG/PNG files into `extracted_images/`. The app reads filenames to build categories and listing metadata.
