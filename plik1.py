import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=gaming+keyboard&_encoding=UTF8&content-id=amzn1.sym.12129333-2117-4490-9c17-6d31baf0582a&pd_rd_r=a8d4640c-2be0-420e-b6aa-7b90e5803aa0&pd_rd_w=B0Jmp&pd_rd_wg=Fbqno&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=BTSCAZ59TPZTX018NVZC&ref=pd_gw_unk"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

book_containers = soup.find_all("article", class_="product_pod")

for container in  book_containers:
    title = container.a.span[""]
    price = container.select(".a-price-whole")[0].get_text()
    book_link = container.h2.a["href"]
    book_page = requests.get(url + book_link)
    book_soup = BeautifulSoup(book_page.content, "html.parser")
    description = book_soup.find("meta", attrs={'name': 'description'})['content']
    print("Title:", title)
    print("Price:", price)
    print("Description:", description)