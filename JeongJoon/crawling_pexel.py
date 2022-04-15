import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from PIL import Image


search = "car"
photo_url = []
delay = 2

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get(f"https://www.pexels.com/ko-kr/search/{search}")
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

# SCROLL_PAUSE_TIME = 10

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(50)

# while True:
#         # Scroll down to bottom
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)
#         # Calculate new scroll height and compare with last scroll height
#         new_height = driver.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             try:
#                 driver.find_element_by_css_selector(".mye4qd").click()
#             except:
#                 break
#         last_height = new_height

# urls = []
# for i in range(60):
#     urls.append(driver.find_elements_by_css_selector('.photo-item__img')[i].get_attribute("data-large-src"))
# print(len(urls))

# url = driver.find_elements_by_css_selector('.photo-item__img')[0].get_attribute("data-large-src")
# urllib.request.urlretrieve(url, "1" + '.jpg')

# print(photo_url)
# time.sleep(10))()