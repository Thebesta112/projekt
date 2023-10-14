from selenium import webdriver
from selenium.webdriver.common.by import By

def pobranie_danych(search_query):
    url = "https://mediamarkt.pl/"
    driver.get(url)

    search_query = "klawiatura" 

    lokali_pasku_wyszuki = driver.find(By.ID, "text")
    lokali_pasku_wyszuki.send_keys(search_query)

    przycisk_wyszuki = driver.find(By.CLASS_NAME, "icon search-icon icon-search")
    przycisk_wyszuki.click()


    driver = webdriver.GoogleChrome

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "Users/krzys/AppData/Local/Programs/Opera/launcher.exe"



#wypis
    baza_wyszuki = driver.find(By.CLASS_NAME, "offer")

    for product_info in baza_wyszuki:
        title_info = product_info.find(By.CSS_SELECTOR, "h2.title")
        price_info = product_info.find(By.CSS_SELECTOR, "span.whole")
        

        title = title_info.text.strip()
        price = price_info.text.strip()

        print(f"Title: {title}")
        print(f"Price: {price}")

    driver.quit()

        print(f"Price: {price}")
