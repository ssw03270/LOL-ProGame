from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import time

class WebClass:
    #Scroll the entered url(=html) to the bottom and return the source.
    def get_scrolled_html(self, playlist_url):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get(playlist_url)
        #Limit of page
        page_limit = 100
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        while page_limit > 0:
            page_limit -= 1
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);") 
            time.sleep(2.0)

            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
            if new_page_height == last_page_height:
                break
            last_page_height = new_page_height

        html_source = driver.page_source
        driver.quit()

        return html_source
    
    def get_soup(self, html_source):
        return BeautifulSoup(html_source, "html.parser")