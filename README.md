# Book Scraper

This project demonstrates how to use Scrapy to scrape book data from websites.

## Getting Started

**Prerequisites:**

- Python 3.x (https://www.python.org/downloads/)
- Scrapy (https://scrapy.org/) - `pip install scrapy`

**Project Setup:**

1. Clone the repository:

   ```bash
   git clone [https://github.com/your-username/bookstoscrape.git](https://github.com/your-username/bookstoscrape.git)

2. (Optional) Create a virtual environment
   ```bash
    python -m venv venv  # Using venv
    source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
    venv\Scripts\activate.bat  # Activate on Windows
3. Install project dependencies
   ```
   pip freeze > requirements.txt

## Running the Scraper
   ```bash
  cd bookstoscrape
  scrapy crawl books_main

This will scrape book data and save it to a SQLite database by default.

**Saving to CSV**
    scrapy crawl books_main -o books.csv
