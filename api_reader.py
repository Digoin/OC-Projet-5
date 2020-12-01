import requests

import config
from product_maker import Product

class Category(Product):


    def __init__(self, category):
        self.category = category

    
    def request(self, page):
        url = f"https://fr-en.openfoodfacts.org/category/{self.category}/{page}.json"
        return requests.get(url).json()
    

    def lines_builder(self, page):
        response_get = dict(self.request(page))
        nutriments_page = []
        for compteur in range(len(response_get["products"])):
            try:
                temporaire = Product(response_get, compteur)
                nutriments_page.append(temporaire)
                print (temporaire.name(), temporaire.categories(), temporaire.nutrition_grade(), temporaire.store(), temporaire.url())
            except KeyError:
                ("Une clé ne correspond pas")
        return nutriments_page


    def list_builder(self):
        products = []
        for list in range(1, 4): 
            page = self.lines_builder(list)
            products.extend (page)    
        return (products)

thing = Category("pizzas")

thing.list_builder()