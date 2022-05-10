import scrapy
import pixabay.core
from imagecrawler.items import ImagecrawlerItem
import time

API_KEY = '26709291-6e479e87405de6d5773773694'

class PixabaySpider(scrapy.Spider):
    name = 'pixabay'
    allowed_domains = ['pixabay.com']
    start_urls = []
    image_id = [0]
    px = pixabay.core(API_KEY)
    count = 0 
    search_name = "car"
    folder_name = "car"
    image = px.query(search_name, perPage = 200)

    for i in range(85):
        start_urls.append(image[i].getLargeImageURL())
        image_id.append(image[i].getId())

    def parse(self, response):
        save_url = response.url
        self.count += 1
        i = self.count
        yield ImagecrawlerItem(image_name=[self.folder_name + str(i)], save_folder=[self.folder_name], image_urls=[save_url])
