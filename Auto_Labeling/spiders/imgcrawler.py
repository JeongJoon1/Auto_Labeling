import scrapy
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import urllib.request
import time
import os

class ImgcrawlerSpider(scrapy.Spider):
    #Base_URL Setting
    name = 'imgcrawler'
    allowed_domains = ['www.naver.com']
    # start_urls = ['http://www.naver.com']
    base = 'https://search.naver.com/search.naver?where=image&section=image&query='

    keyword = input("검색어를 입력하세요: ")
    search_url = base+quote_plus(keyword)
    driver = webdriver.Chrome()
    driver.get(search_url)
    
    #scroll_down 구현부
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height: 
            break
        last_height = new_height

    #디렉토리 생성
    def create_folder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print("Error : Creating Directory. "+directory)
    
    save_path = './img/'+keyword+"/"
    crawl_file = create_folder(save_path)

    #이미지를 긁어오기(Crawling)
    images = driver.find_elements_by_class_name("_image")
    cnt=1
    for image in images:
        try:
            imgUrl= image.get_attribute('src')
            with urllib.request.urlopen(imgUrl) as f:
                with open(save_path + keyword + str(cnt) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
            cnt+=1
        except:
            pass    
        
    driver.close()
    #이미지 다운로드 

    # custom_settings = {
    #     'DOWNLOADER_MIDDLEWARES': { 
    #         'Auto_Labeling.middlewares.AutoLabelingDownloaderMiddleware': 100 
    #     }
    # }

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