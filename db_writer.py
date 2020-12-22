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

    def word_builder(self, line):
        word = ""
        reserve = []
        for character in line:
            if character == ",":
                cleaned = self.clean(word)
                reserve.append(cleaned)
                word = ""
            word += character
        return word
        

    def category_writer(self):
        db_conn = self.connection()
        cursor = db_conn.cursor()
        products = self.list_builder()

        for object in products:
            category_list = set()
            category = self.word_builder(object.categories())
            print(object.categories())
            category_list.update(category)
            category_list = list(category_list)
        
        for category in category_list:
            cursor.execute(f"INSERT INTO category (idcategory, name) VALUES {category_list.index(category), category};")

        # db_conn.commit()
        db_conn.close()
        return category_list


    def db_writer(self):
        all_category = self.category_writer()
        db_conn = self.connection()
        cursor = db_conn.cursor()
        product_id = 1


        for product in self.list_builder:
            store_list = self.word_builder(product.store())

            cursor.execute(f"INSERT INTO product (name, url, nutriscore, store, idproduct) VALUES {product.name(), product.url(), product.nutrition_grade(), product.store(), product_id};")
            for category in product.categories():
                cursor.execute(f"INSERT INTO `category_product` (`category`, `product`) VALUES {product_id, all_category.index(category)};")

            product_id += 1

        db_conn.commit()
        db_conn.close()
