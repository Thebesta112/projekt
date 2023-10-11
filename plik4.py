import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=books"


page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

product_containers = soup.find_all("div", class_="s-result-item")

for container in product_containers:
    title_element = container.find("span", class_="a-text-normal")
    price_element = container.find("span", class_="a-price")

    if title_element and price_element:
        title = title_element.get_text(strip=True)
        price = price_element.find("span", class_="a-offscreen").get_text()
        
        product_link = title_element.a["href"]
        
        product_page = requests.get("https://www.amazon.com" + product_link)
        product_soup = BeautifulSoup(product_page.content, "html.parser")
        
        description = product_soup.find("meta", attrs={'name': 'description'})['content']
        
        print("Title:", title)
        print("Price:", price)
        print("Description:", description)
        print("----")
