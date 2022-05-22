from msilib.schema import Font
from tkinter import *
import tkinter.font as tkfont
from tkinter import filedialog
import scrapy
from scrapy.crawler import CrawlerProcess 
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote_plus
from urllib.request import urlopen
import urllib.request
import sys
import time
import os

main = Tk()
main.title('Image Auto Labeling Tool')
main.geometry('800x500')
main.resizable(False, False)

#크롤링 창  
def createCrawlpage():
    Crawlpage = Toplevel(main)
    Crawlpage.geometry('700x300') 
    Crawlpage.resizable(False, False)
    
    ctitlesize = tkfont.Font(size=20)
    cpsize = tkfont.Font(size=11)
    crawl_label1 = Label(Crawlpage,text="크롤링", height="3",font=ctitlesize)   
    crawl_label2 = Label(Crawlpage,text="크롤링할 이미지를 검색하세요. ", height="3",font=cpsize)   
    
    search = StringVar() #검색어변수 = search 
    ctextbox = Entry(Crawlpage,width=20,textvariable=search) #검색어 입력부 
    ctextbox.place(x=270, y=150)

    def Gtest():
        #Chrome(spider #1)
        class GcrawlerSpider(scrapy.Spider):
            #Base_URL Setting
            name = 'gcrawler'
            allowed_domains = ['www.google.com']
            start_urls = ['http://www.google.com']

            keyword = search.get()
            if(keyword=='end'):
                sys.exit(0)

            driver = webdriver.Chrome(ChromeDriverManager().install())
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
    def Ntest():
        #Naver(spider #2)
        class ImgcrawlerSpider(scrapy.Spider):
            #Base_URL Setting
            name = 'imgcrawler'
            allowed_domains = ['www.naver.com']
            base = 'https://search.naver.com/search.naver?where=image&section=image&query='

            keyword = search.get()
            if(keyword=='end'):
                sys.exit(0)
                
            search_url = base+quote_plus(keyword)
            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get(search_url)
            
            #scroll_down 구현부(body)
            SCROLL_PAUSE_TIME = 2
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

    search_btn = Button(Crawlpage,text="검색",command="") #검색 클릭 시 크롤링 시작 
    search_btn.place(x=420, y=147)

    Gsearch_btn = Button(Crawlpage,text="구글",command=Gtest) #구글 검색 버튼
    Gsearch_btn.place(x=230, y=193)
    Nsearch_btn = Button(Crawlpage,text="네이버",command=Ntest) #네이버 검색 버튼
    Nsearch_btn.place(x=286, y=193)
    Pexel_btn = Button(Crawlpage,text="Pexel",command="") #Pexel 검색 버튼(미완성)
    Pexel_btn.place(x=350, y=193)
    Pixaby_btn = Button(Crawlpage,text="Pixaby",command="") #Pixaby 검색 버튼(미완성)
    Pixaby_btn.place(x=410, y=193)

    folder_btn = Button(Crawlpage,text="폴더열기",command=folder_open)
    folder_btn.place(x=312, y=253)

    crawl_label1.pack() 
    crawl_label2.pack()

def folder_open():
    filedialog.askopenfilename(initialdir='./img',title='파일선택', filetypes=(('jpg files','*.jpg'),('all files','*.*')))

#초기화면 제목부 
fontsize = tkfont.Font(size=20)
title_label = Label(main,text="Image Auto Labeling Tool", height="3",font=fontsize)

#초기화면 버튼부 
crawl_btn = Button(main, text="크롤링", width="20", height="5",command=createCrawlpage)
crawl_btn.place(x=150, y=100)
label_btn = Button(main, text="자동라벨링", width="20", height="5")
label_btn.place(x=450, y=100)

title_label.pack()
main.mainloop() 