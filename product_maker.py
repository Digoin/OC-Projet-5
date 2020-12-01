import requests

import config


class Product:

    def __init__(self, json_dic, product_index):
        self.json_dic = json_dic
        self.product_index = product_index


    def search(self, search):
        return self.json_dic["products"][self.product_index][search]

    def name(self):
        return self.search("product_name")

    def categories(self):
        return self.search("categories")

    def nutrition_grade(self):
        return self.search("nutrition_grades")

    def store(self):
        return self.search("stores")

    def url(self):
        return self.search("url")
