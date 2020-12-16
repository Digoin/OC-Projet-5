import mysql.connector
from mysql.connector.cursor import MySQLCursor

import config
from api_reader import Category

class Database(Category):

    def __init__(self, category):
        super().__init__(category)

    def connection(self):
        self.db_conn = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        return self.db_conn


    def create_table(self):
        script = open("create_table.sql", "r")
        action = ""
        for characters in script:
            action += str(characters)
        cursor = self.connection().cursor()
        cursor.execute(action, multi=True)
    
    def clean(self, word):
        cleaned = word.replace(", ", "")
        cleaned = word.replace(",", "")
        if cleaned.find(' ') == 0:
            cleaned = cleaned[1:]
        return cleaned
    

    def word_builder(self, line, list):
        word = ""
        reserve = []
        for character in line:
            if character == ",":
                cleaned = self.clean(word)
                reserve.append(cleaned)
                word = ""
            word += character
        list.append(reserve)
        return list


    def db_writer(self):
        db_conn = self.connection()
        products = self.list_builder()
        cursor = db_conn.cursor()
        name_list = []
        url_list = []
        nutriscore_list = []
        store_list = []
        category_list = []
        index = 0
        category_index = 1
        category_dict = {}
        already_exist = []
        fk_index = 0

        for object in products:
            print(object.name())
            name_list = self.word_builder(object.name(), name_list)
            url_list = self.word_builder(object.url(), url_list)
            nutriscore_list = self.word_builder(object.nutrition_grade(), nutriscore_list)
            store_list = self.word_builder(object.store(), store_list)
            category_list = self.word_builder(object.categories(), category_list)
            
        for category_per_product in category_list:
            for category in category_per_product:
                if category not in already_exist:
                    already_exist.append(category)
                    category_dict[category_index] = category
                    category_index += 1
        

        for category in category_dict:
            cursor.execute(f"INSERT INTO category (idcategory, name) VALUES {category, category_dict[category]};")

            

        for product in name_list:
            for thing in category_list:
                for category in thing:              
                    temporaire = list(category_dict.keys())[list(category_dict.values()).index(category)]

        for product_categories in category_list:
            fk_list = []
            for value in category_dict.values():
                if value in product_categories:
                    fk_list.append(list(category_dict.keys())[list(category_dict.values()).index(value)])
            fk_index += 1

            cursor.execute(f"INSERT INTO product (name, url, nutriscore, store, idproduct) VALUES {name_list[index][0], url_list[index][0], nutriscore_list[index][0], store_list[index][0], fk_index};")
            for id in fk_list:
                cursor.execute(f"INSERT INTO `category_product` (`category`, `product`) VALUES {id, fk_index};")

            index += 1
        db_conn.commit()
        db_conn.close()


