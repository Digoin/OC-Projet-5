import requests

import config

class Category:


    def __init__(self, category):
        self.category = category

    
    def request(self, page):
        url = f"https://fr-en.openfoodfacts.org/category/{self.category}/{page}.json"
        return requests.get(url).json()
    

    def lines_builder(self, page):
        response_get = self.request(page)
        nutriments_page = []
        for product in response_get["products"]:
            try:
                line_list = []
                complete = True
                for search in config.SEARCH_LIST:
                    line_list.append(product[search])
                    if product[search] == "":
                        complete = False
                if complete:
                    line_tuple = tuple(line_list)
                    nutriments_page.append(line_tuple)
                   
            except KeyError:
                pass
        return nutriments_page


    def list_builder(self):
        nutriments = []
        for list in range(1, 4):
            page = self.lines_builder(list)
            nutriments.extend (page)
        print(nutriments, len(nutriments))
        return (nutriments)
