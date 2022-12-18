from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.khaasfood.com/?s=chicken&post_type=product&product_cat=0"
response = requests.get(url)
print(response)
data = []
soup = BeautifulSoup(response.content, "html.parser")
lists = soup.find_all("div", class_="product-grid-item")
productName = []
price = []
# for list in lists:
#     product_Name = list.find("h3", class_="product-title").get_text(strip=True).strip(" ")
#     price_ = list.find("span", class_="price").get_text(strip=True).strip("৳")
#     productName.append(product_Name)
#     price.append(price_)
#     print(product_Name, price_)
for list in lists:
    product_Name = list.find("h3", class_="product-title").text
    price_ = list.find("span", class_="price").text
    # price_ = list.find("span", class_="price").get_text(strip=True)
    # productName.append(product_Name)
    # price.append(price_)
    print(product_Name, price_)


# data = pd.DataFrame(
#     {
#         "Product Name": productName,
#         "Price": price
#     }
# )
# print(data)


