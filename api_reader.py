import requests

from product_maker import Product


class Category(Product):
    """This class create a list of products based on the given category"""

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
                product = Product(response_get, element)
                if (
                    product.categories_language() == "fr"
                    and product.store() is not None
                    and product.url() is not None
                    and product.store() is not None
                    and product.name() is not None
                    and product.nutrition_grade() is not None
                ):
                    nutriments_page.append(product)
                    test += 1
            except KeyError:
                print("Une clé ne correspond pas")
        return nutriments_page

    def list_builder(self):
        """Iterate lines_builder fuction"""
        products = []
        for iteration in range(1, 4):
            page = self.lines_builder(iteration)
            products.extend(page)
        return products
