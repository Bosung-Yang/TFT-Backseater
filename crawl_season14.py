from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# 기본 시너지 정보 및 챔피언 스킬 정보를 크롤링합니다.
def crawl_basicInfo():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    url = 'https://lolchess.gg/tft/14/'
    driver.get(url)
    time.sleep(3)

    div_elements = driver.find_elements(By.XPATH, '//div[@class="css-0 en8xiz52"]')

    for div in div_elements:
        print(div.text)
        with open("./data_season14/tft14_basicInfo" + ".txt", "a") as f:
            f.write(div.text)
    driver.quit()

def crawl_synerge():
    # TraitCard css-1afmdj5 e3gcvde0
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = "https://lolchess.gg/synergies/set14"
    driver.get(url)
    time.sleep(3)

    div_elements = driver.find_elements(By.XPATH, '//div[@class="TraitCard css-1afmdj5 e3gcvde0"]')
    for div in div_elements:
        print(div.text)
        with open("./data_season14/tft14_synerge" + ".txt", "a") as f:
            f.write(div.text + "\n")
    driver.quit()
    

#crawl_basicInfo()
crawl_synerge()