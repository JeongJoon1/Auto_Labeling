import scrapy
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
from urllib.request import urlopen
import urllib.request
import time
import os

class GcrawlerSpider(scrapy.Spider):
    #Base_URL Setting
    name = 'gcrawler'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com']

    keyword = input("검색어를 입력하세요: ")
    
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    elem = driver.find_element_by_name("q") #google 검색어 입력 부분
    elem.send_keys(keyword) #keyboard입력값을 전송할 수 있음
    elem.send_keys(Keys.RETURN) #enter키를 입력 받음


    #scroll을 끝까지 내려서 모든 사진을 다 다운받을 수 있게끔함
    SCROLL_PAUSE_TIME = 2
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height: 
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
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
    images= driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    cnt=1
    for image in images:
        try:
            image.click()
            imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
            with urllib.request.urlopen(imgUrl) as f:
                with open(save_path + keyword + str(cnt) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
            cnt+=1
        except:
            pass
        
    driver.close()

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, method='GET', encoding='utf-8')
