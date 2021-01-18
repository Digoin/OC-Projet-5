import mysql.connector

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


    def delete_table(self):
        db_conn = self.connection()
        cursor = db_conn.cursor()
        cursor.execute("DELETE FROM category_product;")
        cursor.execute("DELETE FROM category;")
        cursor.execute("DELETE FROM product;")
        cursor.execute("DELETE FROM favorite;")
        db_conn.commit()
        db_conn.close()


    def create_table(self):
        script = open("create_table.sql", "r")
        action = ""
        for characters in script:
            action += str(characters)
        cursor = self.connection().cursor()
        cursor.execute(action, multi=True) #Switch True, False
  

    def category_writer(self):
        products = self.list_builder()
        category_list = set()

        for object_categories in products:
            category_list.update(object_categories.categories())
            
        category_list = list(category_list)
 
        
        return category_list


    def db_writer(self):
        self.create_table()
        all_category = self.category_writer()
        db_conn = self.connection()
        cursor = db_conn.cursor()
        db_categories = []

        cursor.execute("SELECT idproduct FROM product ORDER BY idproduct")
        result = cursor.fetchall()
        try:
            product_id = result[-1][0]
        except IndexError:
            product_id = 0
            print("Première fois que le programme tourne.")


        cursor.execute("SELECT * from category ORDER BY idcategory")
        result = cursor.fetchall()
        for object in result:
            db_categories.append(object[1])

        for category in all_category:
            if category not in db_categories:
                db_categories.append(category)
        print(db_categories)

        
        for category in db_categories:
            try:
                cursor.execute(f"INSERT INTO category (idcategory, name) VALUES {db_categories.index(category), category};")
            except mysql.connector.Error as err:
                if err.errno == 1062 or 1406:
                    print("La catégorie existe déjà ou est trop longue.")
                else:
                    raise


        for product in self.list_builder():
            try:
                cursor.execute(f"INSERT INTO product (name, url, nutriscore, store, idproduct) VALUES {product.name(), product.url(), product.nutrition_grade(), product.store(), product_id};")
                for category in product.categories():
                    print(product_id, db_categories.index(category))
                    cursor.execute(f"INSERT INTO `category_product` (`category`, `product`) VALUES {db_categories.index(category), product_id};")
            except mysql.connector.Error as err:
                if err.errno == 1062 or 1406:
                    print("L'une des caractéristiques du produit existe déjà ou est trop longue.")
                else:
                    raise
            

            product_id += 1

        db_conn.commit()
        db_conn.close()
    

    def delete_short_category(self):
        db_conn = self.connection()
        cursor = db_conn.cursor()
        countdown = 0
        last_link = 0

        cursor.execute("SELECT category FROM category_product ORDER BY category")
        category_link = cursor.fetchall()
        for link in category_link:
            diff = link[0] - last_link
            if diff > 1:
                for id in range(1, diff-1):
                    print(id)
                    cursor.execute(f"DELETE FROM category WHERE idcategory = {last_link + id}")
            elif diff == 1:
                print(countdown)
                if countdown < 4:
                    cursor.execute(f"DELETE FROM category_product WHERE category = {link[0]-1}")
                    cursor.execute(f"DELETE FROM category WHERE idcategory = {link[0]-1}")
                countdown = 0
            elif diff == 0:
                countdown += 1
            last_link = link[0]
        db_conn.commit()
        db_conn.close()