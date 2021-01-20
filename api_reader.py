import requests

from product_maker import Product


class Category(Product):
    def __init__(self, category):
        self.category = category

    def request(self, page):
        """Search the given page in the given category on the API"""
        url = f"https://fr-en.openfoodfacts.org/category/{self.category}/{page}.json"
        return requests.get(url).json()

    def lines_builder(self, page):
        """Use the json dict to search the products"""
        response_get = dict(self.request(page))
        nutriments_page = []
        test = 1
        for element in range(len(response_get["products"])):
            try:
                object = Product(response_get, element)
                if (
                    object.categories_language() == "fr"
                    and object.store() is not None
                    and object.url() is not None
                    and object.store() is not None
                    and object.name() is not None
                    and object.nutrition_grade() is not None
                ):
                    nutriments_page.append(object)
                    test += 1
            except KeyError:
                print("Une clé ne correspond pas")
        return nutriments_page

    def list_builder(self):
        """Iterate lines_builder fuction"""
        products = []
        for list in range(1, 4):
            page = self.lines_builder(list)
            products.extend(page)
        return products
