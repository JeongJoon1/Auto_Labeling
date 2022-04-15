from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


driver = webdriver.Chrome()
driver.get("https://pixabay.com/ko/")
elem = driver.find_element_by_name("q")
elem.send_keys("car")
elem.send_keys(Keys.RETURN)
time.sleep(10)