import openpyxl
from bs4 import BeautifulSoup
import requests

url = "https://www.khaasfood.com/?s=chicken&post_type=product&product_cat=0"
response = requests.get(url)
print(response)
soup = BeautifulSoup(response.content, 'html.parser')
# xml
# print(soup.prettify())
# print(soup.title)

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Product price'
sheet.append(['product_name', 'price'])

lists = soup.find_all("div", class_="product-grid-item")
# print(len(lists))
for list in lists:
    productname = list.find("h3", class_="product-title").a.text
    price = list.find("span", class_="price").span.text.split()[1]
    print(productname)
    print(price)
    sheet.append([productname, price])
excel.save('../khassfood.xlsx')
