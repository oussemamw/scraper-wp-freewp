from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get('https://freewp.cc/themes/')
driver1 = webdriver.Chrome()






def carawl(link):

    driver1.get(link)
    time.sleep(4)

    download_link = driver1.find_element_by_class_name("ext-link").get_attribute("href")
    
    driver1.get(download_link)
    time.sleep(30)
    element = driver1.find_element_by_xpath('//div[@class="col-sm centered extra-top"]')
    #driver1.find_element_by_class_name('larger').click()
    element=element.find_element_by_tag_name("a").get_attribute("href")
    driver1.get(element)
    time.sleep(6)
   # driver1.find_element_by_id("dismiss-button").click()
    time.sleep(5)
    # open file in write mode
    name=random.randrange(20, 5000, 3)
    f = open(str(name)+".txt", "a")
    for i in driver1.find_elements_by_css_selector("tr a"):
        # write each item on a new line
        if 'javascript' in i.get_attribute("href"):
            pass
        else:
            f.write("%s\n" % i.get_attribute("href"))
    f.close()
    
    
    print('Done')
    


while True:
    links = driver.find_elements_by_class_name("gb-headline-1a700f75")
    for i in links:
        try:
            carawl(i.find_element_by_tag_name('a').get_attribute("href"))
            time.sleep(5)
        except:
            print(i.find_element_by_tag_name('a').get_attribute("href"))



    driver.find_element_by_class_name("gb-button-0ad05550").click()
    time.sleep(5)
