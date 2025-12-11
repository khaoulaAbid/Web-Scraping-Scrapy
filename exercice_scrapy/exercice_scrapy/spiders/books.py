import scrapy
from exercice_scrapy.items import ExerciceScrapyItem
import re

# scrapy startproject exercice_scrapy                        : créer un projet
# cd exercice_scrapy
# scrapy genspider books http://books.toscrape.com  
# scrapy crawl books                                    : executer le code
# scrapy crawl books -O  outputs/books_test0.json      : output fichier json 
# scrapy crawl books -O  outputs/books_test0.csv    : output csv 


# Site : http://books.toscrape.com

#  1. Créer un projet Scrapy bookstore 
# 2. Créer un spider books 
# 3. Définir un BookItem avec : title, price, rating, availability 
# 4. Scraper la première page 
# 5. Extraire tous les livres avec leurs informations 
# 6. Exporter en JSON et CSV 
# 7. Bonus : Ajouter la pagination (3 pages max)




class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com"]
    
    def parse(self, response):
           books = response.css('article.product_pod')

           for book in books:

            item = ExerciceScrapyItem()
            item['title'] = book.css('a::attr(title)').get() 
            item['price'] = book.css('p.price_color::text').get()

            rating_class = book.xpath('.//p[contains(@class, "star-rating")]/@class').get()
            item['rating'] = rating_class.split()[1]

            availability = book.xpath('.//p[contains(@class, "instock ")]/@class').get()
            item['availability'] = availability.split()[0]

            item['image_url'] = book.css('img::attr(src)').get()

            yield item

        
            # Suivre le lien "Next"
            next_page = response.css('li.next a::attr(href)').get()
            cp=0
            if next_page and cp < 3:

                yield response.follow(next_page,callback=self.parse,meta={'cp': cp + 1}  )       
