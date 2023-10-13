from selenium import webdriver
from selenium.webdriver.common.by import By

def pobranie_danych(produkt):
    url = "https://mediamarkt.pl/"
    driver.get(url)

    produkt = "klawiatura"
    driver = webdriver.Chrome

    lokali_pasku_wyszuki = driver.find(By.ID, "text")
    lokali_pasku_wyszuki.send_keys(produkt)

    przycisk_wyszuki = driver.find(By.CLASS_NAME, "icon search-icon icon-search")
    przycisk_wyszuki.click()

    baza_wyszuki = driver.find(By.CLASS_NAME, "offer")

    for info in baza_wyszuki:
        title_info = info.find(By.CSS_SELECTOR, "h2.title")
        price_info = info.find(By.CSS_SELECTOR, "span.whole")
        

        title = title_info.text.strip()
        price = price_info.text.strip()

        print(f"Title: {title}")
        print(f"Price: {price}")
