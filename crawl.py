import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.metatft.com/comps")
time.sleep(10) # for loading

def crawl_comp(target_rank = "S"):
    div_elements = driver.find_elements(By.XPATH, '//div[@class="CompRow Tier'+target_rank+'"]')
    ranks = []
    deck_names = []
    champion_lists = []
    average_places = []
    pick_rates = []
    win_rates = []
    for div in div_elements:
        print(div.text)
        print("----")
        rank = div.text.split("\n")[0]
        deck_name = div.text.split("\n")[1]
        contents = div.text.split("\n")[4:]
        champion_list = []
        for content in contents:
            if content.isdigit():
                continue
            if "Avg Place" in content:
                break
            #print(content)
            champion_list.append(content)
        average_place = div.text.split('Avg Place')[1].split('Pick Rate')[0].replace('\n','')
        #print(average_place)
        pick_rate = div.text.split('Pick Rate')[1].split('Win Rate')[0].replace('\n','')
        win_rate = div.text.split('Win Rate')[1].replace('\n','')
        ranks.append(rank)
        deck_names.append(deck_name)
        champion_lists.append(champion_list)
        average_places.append(average_place)
        pick_rates.append(pick_rate)
        win_rates.append(win_rate)
    df = pd.DataFrame({
        "Rank": ranks,
        "Deck Name": deck_names,
        "Champion List": champion_lists,
        "Average Place": average_places,
        "Pick Rate": pick_rates,
        "Win Rate": win_rates
    })
    print(df)
    df.to_csv("tft_comps_"+target_rank+".csv", index=False)

crawl_comp("S")
crawl_comp("A")
driver.quit()