import requests

import config

    def request(self, page):
        url = f"https://fr-en.openfoodfacts.org/category/{self.category}/{page}.json"
        return requests.get(url).json()

class Product:

    def __init__(self, product):
        self.product = product

    def request(self, page):
        url = "https://fr-en.openfoodfacts.org/category/1.json"
        return requests.get(url).json()
    
    def lines_builder(self, product, key):
        try:
            line_list = []
            complete = True
            for search in config.SEARCH_LIST:
                line_list.append(product[search])
                if product[search] == "":
                    complete = False
            if complete:
                return line_list
        except KeyError:
            pass
        return None

    def name(product):
        return self.lines_builer(product, "product_name")
        
    def category(product):
        return lines_builer(product, "categories")

    def nutriscore(product):
        return lines_builer(product, "nutrition_grades")

    def store(product):
        return lines_builer(product, "stores")

    def url(product):
        return lines_builer(product, "url")
    

class Category(Product):


    def __init__(self, category):
        self.category = category
    


    def list_builder(self):
        nutriments = []
        for list in range(1, 4):
            page = self.lines_builder(list)
            nutriments.extend (page)
        print(nutriments, len(nutriments))
        return (nutriments)
