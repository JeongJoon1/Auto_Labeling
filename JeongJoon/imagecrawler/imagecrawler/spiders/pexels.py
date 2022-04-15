import scrapy


class PexelsSpider(scrapy.Spider):
    name = 'pexels'
    allowed_domains = ['www.pexels.com']
    def start_requests(self):
        urls = [
            'https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&dpr=3&h=384&w=384',
            'https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        pass
