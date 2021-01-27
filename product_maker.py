class Product:
    """This class create a product"""

    def __init__(self, json_dic, product_index):
        self.json_dic = json_dic
        self.product_index = product_index

    def search(self, search):
        """Search the given element of the given product"""
        return self.json_dic["products"][self.product_index][search]

    def name(self):
        """Search for name"""
        try:
            if self.search("product_name") != "":
                return self.search("product_name")
            else:
                return None
        except KeyError:
            print("Name not found")
            return None

    def categories(self):
        """Search for categories"""
        try:
            if self.search("categories") != "":
                return [
                    category.strip()
                    for category in self.search("categories").split(",")
                ]
            else:
                return None
        except KeyError:
            print("Category not found")
            return None

    def nutrition_grade(self):
        """Search for nutriscore"""
        try:
            if self.search("nutrition_grades") != "":
                return self.search("nutrition_grades")
            else:
                return None
        except KeyError:
            print("Nutriscore not found")
            return None

    def store(self):
        """Search for stores"""
        try:
            if self.search("stores") != "":
                return self.search("stores")
            else:
                return None
        except KeyError:
            print("Store not found")
            return None

    def url(self):
        """Search for url"""
        try:
            if self.search("url") != "":
                return self.search("url")
            else:
                return None
        except KeyError:
            print("Url not found")
            return None

    def categories_language(self):
        """Search the language of the product"""
        return self.search("categories_lc")
