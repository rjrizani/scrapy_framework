# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

from .items import BookSQLAlchemyItem, session

class BookstoscrapePipeline:
    def process_item(self, item, spider):
        item['price'] = float(item['price'].replace('£', ''))
        item['price_excl_tax'] = float(item['price_excl_tax'].replace('£', ''))
        item['price_incl_tax'] = float(item['price_incl_tax'].replace('£', ''))
        item['tax'] = float(item['tax'].replace('£', ''))
        item['rating'] = self.process_rating(item['rating'])
        item["stock"] = self.extract_number(item['stock'])
        item["number_reviews"] = int(item['number_reviews'])
        item["img_url"] =  item["img_url"].replace('../../', 'https://books.toscrape.com/')
        return item

    def process_rating(self, value):
        match value:
            case 'One':
                return 1
            case 'Two':
                return 2
            case 'Three':
                return 3
            case 'Four':
                return 4
            case 'Five':
                return 5
            
    def extract_number(self, text):
        match = re.search(r'\d+', text)
        if match:
            return int(match.group())
        return None
        

class SqlAlchemyPipeline:
    def __init__(self):
        self.session = session

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        book = BookSQLAlchemyItem(
            title=item['title'],
            price=item['price'],
            stock=item['stock'],
            rating=item['rating'],
            description=item['description'],
            upc=item['upc'],
            product_type=item['product_type'],
            price_excl_tax=item['price_excl_tax'],
            price_incl_tax=item['price_incl_tax'],
            tax=item['tax'],
            number_reviews=item['number_reviews'],
            img_url=item['img_url']
        )
        book_exists = self.session.query(BookSQLAlchemyItem).filter_by(title=book.title).first()
        if book_exists:
            print(f"Book {book.title} already exists in the database, skipping.")
        else:
            self.session.add(book)
            print(f"Book {book.title} added to the database.")
        self.session.commit()
        return item
    