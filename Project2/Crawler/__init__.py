from bs4 import BeautifulSoup
from selenium import webdriver
from GeocodingAPI import geocoding
import json

class Crawler(object):
    def __init__(self, driver_path, save_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        import os
        url_file_path = os.path.join(save_path, "urls")
        self.url_file = open(url_file_path, 'a')

    def crawl(self):
        self.driver.get("https://www.corcoran.com/nyc/Search/Listings?SaleType=Rent")
        self.driver.implicitly_wait(20)
        next_url = self.__scrapOnePage__(self.driver.page_source)
        while len(next_url) > 0:
            self.driver.find_elements_by_xpath("//a[@title='Go to next page']")[0].click()
            self.driver.implicitly_wait(20)
            next_url= self.__scrapOnePage__(self.driver.page_source)

    def __scrapOnePage__(self, page_source):
        soup = BeautifulSoup(page_source, "html.parser")
        listings = soup.select(".listing")
        for list in listings:
            address = list.find("span", {"class" : "address"}).find("a")['title']
            address = address + ", NY, USA"
            print(address)
            address_split = address.split(',')

            geo_details = geocoding(address[0] + ', ' + address[2])
            print(geo_details)
            geo_details['addr'] = address
            self.url_file.write(json.dumps(geo_details) + ',\n')

        next_url = ''
        try:
            next_url = soup.find("a",{"title": "Go to next page"})['href']
        except:
            print("end of all pages")

        finally:
            return next_url
