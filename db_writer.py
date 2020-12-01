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

    # def execute_cursor():


    def create_table(self):
        script = open("create_table.sql", "r")
        action = ""
        for characters in script:
            action += str(characters)
        cursor = self.connection().cursor()
        cursor.execute(action, multi=True)
    
    def category_writer(self):
        products = self.list_builder()
        cursor = self.connection().cursor()
        cursor.execute("SELECT name FROM category", multi=False)
        result = cursor.fetchall()
        for db_category in result:
            for product in products:
                for category in product["categories"]:
                    print (category)
                    if db_category != category:
                        cursor.execute(f"INSERT INTO category (name) VALUES ('{category}')")
                        self.db_conn.commit()


category = Database(config.CATEGORY_SEARCH)
category.category_writer()
