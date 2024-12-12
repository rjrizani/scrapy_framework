# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

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
        