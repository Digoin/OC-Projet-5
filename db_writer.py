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
        script = open("create_table.txt", "r")
        action = ""
        for characters in script:
            action += str(characters)
        cursor = self.connection().cursor()
        cursor.execute(action, multi=True)
    
    def category_writer(self):
        exist = False
        cursor = self.connection().cursor()
        cursor.execute("SELECT name FROM category", multi=False)
        result = cursor.fetchall()
        for category in result:
            if category == config.CATEGORY_SEARCH:
                exist = True
        if not exist:
            cursor.execute(f"INSERT INTO category (name) VALUES ('{config.CATEGORY_SEARCH}')")
            self.db_conn.commit()
        


category = Database(config.CATEGORY_SEARCH)
category.create_table()
category.nutriment_writer()