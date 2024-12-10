import scrapy


class BooksMainSpider(scrapy.Spider):
    name = "books_main"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"]

    def parse(self, response):
        title = response.css("article.product_page div.row h1::text").get()
        price = response.css("p.price_color::text ").get()
        stock = response.css("p.instock.availability::text").getall()[1].strip()
        rating = response.css("p.star-rating::attr(class)").get().split()[1]
        #description = response.css("p::text").getall()[-1]
        description = response.css("div#product_description ~ p::text").get()
        table_data = response.css("table.table.table-striped td::text").getall()
        upc = table_data[0]
        product_type = table_data[1]
        price_excl_tax = table_data[2]
        price_incl_tax = table_data[3]
        tax = table_data[4]
        availability = table_data[5]
        number_reviews = table_data[6]    

        print(title, price, stock, rating, description, upc, product_type, price_excl_tax, price_incl_tax, tax, availability, number_reviews)


