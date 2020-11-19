import mysql.connector
import config

from api_reader import Category

class Database(Category):

    def __init__(self, category):
        super().__init__(category)

    def connection(self):
        self.off_db = mysql.connector.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            database=config.DB_NAME
        )
        return self.off_db

    def action(self):
        mycursor = self.connection().cursor()
        mycursor.execute("show databases")


category = Database(config.CATEGORY_SEARCH)
category.action()
category.list_builder()