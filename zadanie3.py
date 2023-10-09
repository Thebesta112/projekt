import requests
from bs4 import BeautifulSoup

odpowiedz = requests.get("https://mediamarkt.pl/rtv-i-telewizory/telewizor-samsung-qe65s95bat")
soup = BeautifulSoup(odpowiedz.text, 'html.parser')
cena = soup.find("span", itemprop="whole").text.replace(",", ".")
tv = soup.find("li", itemprop="product-attribute-value").next_element.find("a").text
nazwa = soup.find("h1", string="title is-heading").next_element.find("a").text


print(f"cena: {cena}, rodzaj:{tv}, nazwa: {nazwa}")

tytul = "Telewizor SAMSUNG QE65S95BAT"
url = f"https://www.mediamarkt.pl/search?q={tytul}",
p = {
        "q": tytul
    }
tytul = tytul.lower()
f = requests.get("http://www.mediamarkt.pl/search", params=p)
soup = BeautifulSoup(f.text, 'html.parser')
for znacznik in soup.find_all(class_="product_show_content"):
    tytul_znacznika = znacznik.text.lower()
    if tytul == tytul_znacznika:
        print(tytul_znacznika)
        print(znacznik.parent["href"])
        print(f"https://www.mediamarkt.pl{znacznik.parent['href']}")	
