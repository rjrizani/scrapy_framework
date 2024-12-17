# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class BookstoscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    product_type = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    number_reviews = scrapy.Field()
    img_url = scrapy.Field()

class BookSQLAlchemyItem(Base): 
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = Column(String(255), unique=True, nullable=False)
    price = Column(Float())
    stock = Column(Integer())
    rating = Column(Integer())
    description = Column(String())
    upc = Column(String(255))
    product_type = Column(String())
    price_excl_tax = Column(Float())
    price_incl_tax = Column(Float())
    tax = Column(Float())
    number_reviews = Column(Integer())
    img_url = Column(String())

engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

    
