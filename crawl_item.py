import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#driver.get("https://www.metatft.com/units/Heimerdinger")
#time.sleep(10) # for loading

def crawl_item_by_href(url):
    driver.get(url)
    time.sleep(3)
    div_elements = driver.find_elements(By.XPATH, '//div[@class="UnitDetailStatsItem"]')
    for div in div_elements:
        if "The best items for "in div.text:
            print(div.text.split("\n")[1])
            with open("tft_items_recommand" + ".txt", "a") as f:
                f.write(div.text.split("\n")[1])

def crawl_item(champion_name = "Heimerdinger"):
    driver.get("https://www.metatft.com/units/" + champion_name)
    time.sleep(3)
    div_elements = driver.find_elements(By.XPATH, '//div[@class="UnitDetailStatsItem"]')
    for div in div_elements:
        if "The best items for "in div.text:
            print(div.text.split("\n")[1])
            with open("tft_items_" + champion_name + ".txt", "a") as f:
                f.write(div.text.split("\n")[1])

def crawl_champname():
    driver.get("https://www.metatft.com/units")
    time.sleep(3)
    elements = driver.find_elements("xpath", "//div[@class='StatTableContainer']//a[@class='StatLink']")

# 각 요소에서 href 속성 추출하여 출력
    for element in elements:
        href_value = element.get_attribute("href")
        print("Href:", href_value)
        with open("href_champnames.txt", "a") as f:
            f.write(href_value + "\n")

#crawl_item("Heimerdinger")
#crawl_champname()

with open("href_champnames.txt", "r") as f:
    for line in f:
        crawl_item_by_href(line.strip())
driver.quit()