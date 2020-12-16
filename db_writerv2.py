from typing import List
import requests

class Product:
    

    def __init__(self, raw_product):
        self.raw_product = raw_product

    @property
    def categories(self):
        categories = [category.strip() for category in self.raw_product["categories"].split(",")]
        return categories
        

class Category:


    def __init__(self, category):
        self.category = category

   
    def get_products(self) -> List[Product]:
        current_page = 1
        total_page = 2
        while current_page < 5:
            url = f"https://fr-en.openfoodfacts.org/category/{self.category}/{current_page}.json"
            print(url)
            result = requests.get(url).json()
                
            for raw_product in result["products"]:
                yield Product(raw_product)

            total_page = int(result["count"])//result["page_size"]
            current_page += 1

