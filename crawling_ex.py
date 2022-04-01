from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

searches = ['자동차']

count = 1
for search in searches:
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 5
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    print(len(images)) # 출력되는 이미지 개수가 너무 적으면 다시 실행
    for image in images:
        print(count)
        try:
            image.click()
            time.sleep(7) # 로딩되는 시간을 짧게 잡으면 화질이 낮은 이미지 저장
            imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        except:
            pass
        count = count + 1
    driver.close()