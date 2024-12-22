# Book Scraper

This project demonstrates how to use Scrapy to scrape book data from websites.

## Getting Started

**Prerequisites:**

- Python 3.x (https://www.python.org/downloads/)
- Scrapy (https://scrapy.org/) - `pip install scrapy`

**Project Setup:**

1. Clone the repository:

   ```bash
   git clone https://github.com/rjrizani/scrapy_framework.git

2. (Optional) Create a virtual environment
  
3. Install project dependencies
   ```
   pip install -r requirements.txt

## Running the Scraper
   ```bash
  cd scrapy_framework/bookstoscrape
  scrapy crawl books_main

This will scrape book data and save it to a SQLite database by default.

**Saving to CSV**
    scrapy crawl books_main -o books.csv
