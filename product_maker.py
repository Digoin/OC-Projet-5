

class Product:

    def __init__(self, json_dic, product_index):
        self.json_dic = json_dic
        self.product_index = product_index


    def search(self, search):
        search_line = self.json_dic["products"][self.product_index][search]
        return f"{search_line},"

    def name(self):
        return self.search("product_name")

    def categories(self):
        return self.search("categories")

    def nutrition_grade(self):
        return self.search("nutrition_grades")

    def store(self):
        try:
            return self.search("stores")
        except KeyError:
            print("Store not found")
            return None

    def url(self):
        return self.search("url")

    def categories_language(self):
        return self.search("categories_lc")
