How to run this project: 

cd bookstoscrape
scrapy crawl books_main

it will direcly saving data to sqlite database. but if you want to save data to csv type this in commanline
scrapy crawl books_main -o books.csv
