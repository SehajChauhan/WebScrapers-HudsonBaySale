import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

BrandC = []
DescC = []
OpriceC = []
FpriceC = []

x = input("Enter the url: ")

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
i = 0
while(True):
    try:
        if i == 0:
            URL = x + '?Nao=0'
        else:
            URL = x + '?Nao={}'.format(i)
        page = requests.get(URL, headers=headers)
        soup  = BeautifulSoup(page.content, 'html.parser')

        def retrieve_brand():
            brand_tags = soup('span', class_='product-designer-name')
            for tag in brand_tags:
                brand = tag.contents[0]
                BrandC.append(brand)

        def retrieve_product_description():
            desc_tags = soup('p', class_='product-description')
            for tag in desc_tags:
                desc = tag.contents[0]
                DescC.append(desc)


        def retrieve_oprice():
            oprice_tags = soup('span', class_='product-price line-through')
            for tag in oprice_tags:
                oprice = tag.contents[0]
                OpriceC.append(oprice)


        def retrieve_fprice():
            fprice_tags = soup('span', class_='product-sale-price')
            for tag in fprice_tags:
                fprice = tag.contents[0]
                FpriceC.append(fprice)


        retrieve_brand()
        retrieve_product_description()
        retrieve_oprice()
        retrieve_fprice()

        df = pd.DataFrame(list(zip(*[BrandC, DescC, OpriceC, FpriceC])))
        df.columns = ['Brand', 'Description', 'OriginalPrice', 'FinalPrice']
        df.to_csv('scrape2.csv', index=False)

        i += 150
        if i>1000:
            break

    except:
        break
