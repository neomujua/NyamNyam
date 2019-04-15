# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver



def instaCrawl(a):
    url = "https://www.instagram.com/explore/tags/"
    url += a
	
    options = webdriver.ChromeOptions()	
    options.add_argument('headless')	
    options.add_argument('disable-gpu')	
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=options)	

    driver.implicitly_wait(3)

    driver.get(url)

    totalCount = driver.find_element_by_class_name('g47SY').text 
    
    driver.quit()
    
    return totalCount