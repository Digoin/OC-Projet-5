import requests

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
        for element in range(len(response_get["products"])):
            try:
                object = Product(response_get, element)
                if object.categories_language() == "fr," and object.store() != None and object.store() != ",":
                    nutriments_page.append(object)
            except KeyError:
                print("Une clé ne correspond pas")
        return nutriments_page


    def list_builder(self):
        products = []
        for list in range(1, 4): 
            page = self.lines_builder(list)
            products.extend (page)    
        return (products)
    


thing = Category("pizzas")

thing.list_builder()