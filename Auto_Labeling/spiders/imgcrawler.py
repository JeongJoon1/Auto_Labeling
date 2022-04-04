import scrapy
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen

class ImgcrawlerSpider(scrapy.Spider):
    name = 'imgcrawler'
    allowed_domains = ['www.naver.com']
    # start_urls = ['http://www.naver.com']
    base = 'https://search.naver.com/search.naver?where=image&section=image&query='

    keyword = input("검색어를 입력하세요: ")
    search_url = base+quote_plus(keyword)
    driver = webdriver.Chrome()
    driver.get(search_url)

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': { 
            'Auto_Labeling.middlewares.AutoLabelingDownloaderMiddleware': 100 
        }
    }

    # def __init__(self, *args, **kargs):
        
        

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, method='GET', encoding='utf-8')


    def parse(self, response):
        contents = response.xpath('//*[@id="main_pack"]/section[2]/div')
        for content in contents:
            small_img = content.xpath('div[1]/div[1]/div[1]/div/div[1]/a/img').extract_first()
            big_img = content.xpath('div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/img').extract_first()
            item = {
                'small_img' : small_img.strip() if small_img else small_img
                ,'big_img' : big_img.strip() if big_img else big_img
            }
            print(item)

            yield item 
        #  print(response.url, response.body)