# Upl.uz News Parser

**[View Code](./upluz-news-parser/)** A Python-based web scraper designed to extract news categories, article metadata, and full-text descriptions from the [Upl.uz](https://upl.uz) news portal.

## 🚀 Features

- **Category Parsing**: Automatically retrieves available news categories from the site navigation.
- **Deep Scraping**: Extracts article titles, images, publication dates, comment counts, and the **full text** of the articles by navigating to each article's detail page.
- **Structured JSON Output**: Saves the scraped data cleanly into `categories.json` and `posts.json`.
- **OOP Architecture**: Built using an Object-Oriented approach (`BaseParser`, `CategoryParser`, `DetailParser`) making it modular, readable, and easy to scale.

## 📝 Project Structure

```text
Upluz-news-parser/
├── site_parser/
│   ├── __init__.py
│   ├── base.py         # Base parser class with requests and BeautifulSoup setup
│   ├── category.py     # Parser for extracting category links
│   └── detail.py       # Parser for extracting full article details
├── main.py             # Main entry point to run the scraper
├── settings.py         # Global variables (BASE_URL) and helper functions (safe_to_json)
└── requirements.txt    # Python dependencies
```

> **Note:** Files like `categories.json` and `posts.json` are dynamically generated when you run the scraper.

## 🛠️ Prerequisites

- Python 3.x
- `requests`
- `beautifulsoup4`

## ⚙️ Installation

1. **Clone or download the repository.**
2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start scraping, simply run the `main.py` script:

```bash
python main.py
```

### What happens when you run it

1. The script initializes `CategoryParser` and scrapes the main categories, saving them to `categories.json`.
2. It then passes these categories to `DetailParser`, which navigates through each category, extracts the posts, visits each post's detail page for the full description, and compiles the data.
3. The final structured data is saved to `posts.json`.

## ‼️Disclaimer

This project is intended for educational purposes only. Please be respectful of the website's servers and do not overload them with excessive requests.
