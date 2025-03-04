import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.metatft.com/comps")
#print(driver.page_source)
#div_elements = driver.find_elements(By.XPATH, '//div[@class="CompListContainer"]')
div_elements = driver.find_elements(By.XPATH, '//div[@class="CompRow TierA"]')
for div in div_elements:
    print(div.text)
    print("----")
driver.quit()
