import scrapy
import urllib.request
from pexels_api import API
from imagecrawler.items import ImagecrawlerItem

import time
class PexelsSpider(scrapy.Spider):
    name = 'pexels'
    count = 0
    folder_name = 'koala'

    
    image_names = "koala"
    api = API("563492ad6f917000010000018dd8c577fccf43dfb3bcbda35369905d")
    api.search(image_names)
    start_urls = []

    while True:
    # Get all photos in the page
        photos = api.get_entries()
        # For each photo print its properties
        for photo in photos:
            # print("-----------------------------------------------")
            # print("Photo id: ", photo.id)
            # print("Photo width: ", photo.width)
            # print("Photo height: ", photo.height)
            # print("Photo url: ", photo.url)
            # print("Photographer: ", photo.photographer)
            # print("Photo description: ", photo.description)
            # print("Photo extension: ", photo.extension)
            # print("Photo sizes:")
            # print("\toriginal: ", photo.original)
            # print("\tcompressed: ", photo.compressed)
            # print("\tlarge2x: ", photo.large2x)
            # print("\tlarge: ", photo.large)
            # print("\tmedium: ", photo.medium)
            # print("\tsmall: ", photo.small)
            # print("\ttiny: ", photo.tiny)
            # print("\tportrait: ", photo.portrait)
            # print("\tlandscape: ", photo.landscape)
            start_urls.append(photo.original)
        # If there is no next page print the last page and end the loop
        if not api.has_next_page:
            print("Last page: ", api.page)
            break
        # Search next page
        api.search_next_page()
        
    
    #start_urls = url_api()

    # def start_requests(self):
    #     return [scrapy.Request(url=url, callback=self.parse) for url in self.start_urls]

    
    
    print(start_urls)
    def parse(self, response):
        save_url = response.url
        self.count += 1
        i = self.count
        yield ImagecrawlerItem(image_name=[self.folder_name + str(i)], save_folder=[self.folder_name], image_urls=[save_url])
