import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
#driver.get("https://www.metatft.com/units/Heimerdinger")
#time.sleep(10) # for loading

def crawl_item(champion_name = "Heimerdinger"):
    driver.get("https://www.metatft.com/units/" + champion_name)
    time.sleep(3)
    div_elements = driver.find_elements(By.XPATH, '//div[@class="UnitDetailStatsItem"]')
    for div in div_elements:
        if "The best items for "in div.text:
            print(div.text.split("\n")[1])
            with open("tft_items_" + champion_name + ".txt", "a") as f:
                f.write(div.text.split("\n")[1])

crawl_item("Heimerdinger")


driver.quit()