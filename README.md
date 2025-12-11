# Web-Scraping-Scrapy

Projet Scrapy – Books to Scrape
Site à scraper : http://books.toscrape.com

Objectifs :

Créer un projet Scrapy bookstore

Créer un spider "books"

Définir un BookItem avec : title, price, rating, availability

Scraper la première page

Extraire tous les livres avec leurs informations

Exporter les données en JSON et CSV

Pagination sur 3 pages 

Commandes utilisées :

Créer un projet Scrapy :
scrapy startproject exercice_scrapy

Entrer dans le projet :
cd exercice_scrapy

Créer le spider "books" :
scrapy genspider books http://books.toscrape.com

Exécuter le spider :
scrapy crawl books

Exporter les résultats en JSON :
scrapy crawl books -O outputs/books_test0.json

Exporter les résultats en CSV :
scrapy crawl books -O outputs/books_test0.csv
