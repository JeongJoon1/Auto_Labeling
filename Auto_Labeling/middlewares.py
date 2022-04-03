# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from time import sleep
 
from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request

class AutoLabelingSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class AutoLabelingDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened, signal=signals.spider_opened)
        return middleware

    def spider_opened(self, spider):
        chrome_options = Options()
        chrome_options.add_argument( "--no-sandbox" )
        chrome_options.add_argument( "--disable-gpu" )

        driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = driver

    def spider_closed(self,spider):
        self.driver.close()

    def process_request(self, request, spider):
        # driver = webdriver.Chrome('chormedriver')
        self.driver.get(request.url)
        # #scroll을 끝까지 내려서 모든 사진을 다 다운받을 수 있게끔함
        # SCROLL_PAUSE_TIME = 3
        # # Get scroll height
        # last_height = driver.execute_script("return document.body.scrollHeight")

        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     # Wait to load page
        #     sleep(SCROLL_PAUSE_TIME)
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height: 
        #         break
        #     last_height = new_height

        # #크롬내에서 이미지 검색 시 작은 이미지들을 검색하는 방법
        # images= driver.find_elements_by_css_selector("._image _listImage")
        # cnt=1
        # for image in images:
        #     try:
        #         image.click()
        #         #큰 이미지 검색
        #         sleep(3)
        #         imgUrl = driver.find_element_by_css_selector("._image").get_attribute("src")
        #         #이미지를 최종적으로 download
        #         urllib.request.urlretrieve(imgUrl,str(cnt)+".jpg")
        #         cnt+=1
        #     except:
        #         pass
        
        body = to_bytes(text=self.driver.page_source)
        sleep(5)
        return HtmlResponse(url=request.url, body=body, encoding='utf-8', request=request )
            
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

