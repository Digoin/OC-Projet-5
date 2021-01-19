import mysql.connector
import config

def connection():
    db_conn = mysql.connector.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        database=config.DB_NAME
    )
    return db_conn


class User:

    def __init__(self):
        pass


    def connected(self):
        print("Bienvenue, choisissez une option à l'aide des touches 1 et 2. 0 sert à revenir en arrière.")
        fav_db=input("Voulez vous 1 : Accéder à vos produits favoris ou 2 : Accéder à la base de données de tous les produits ? : ")
        if fav_db == "1":
            self.favorite()
        elif fav_db == "2":
            self.db_category()
        else:
            print("Veuillez choisir avec 1 ou 2.")
            self.connected()


    def chose(self, db_list):
        for id in db_list:
            print(id)
        chosed_id = input("Choisisez grace à l'id : ")
        if chosed_id == "0":
            return None
        for id in db_list:
            if id[0] == int(chosed_id):
                return id
        print("L'id choisis ne correspond à rien.")
        self.chose(db_list)


    def add_fav(self, product):
        db_conn = connection()
        cursor = db_conn.cursor()
        fav_choice = input("Voulez vous ajoutez le produit à vos favoris ? 1: Oui 2: Non :")
        if fav_choice == "1":
            try:
                cursor.execute(f"INSERT INTO favorite (idfavorite, name) VALUES {product[0], product[1]};")
            except mysql.connector.Error as err:
                if err.errno == 1062:
                    print("Le produit est déjà dans la base de donnée.")
                else:
                    raise
            db_conn.commit()
            db_conn.close()
            self.db_category()
        elif fav_choice == "0" or "2":
            db_conn.close()
            self.db_category()
        else:
            print("Je n'ai pas compris votre demande.")
            db_conn.close()
            self.add_fav(product)


    def favorite(self):
        db_conn = connection()
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM favorite")
        favorites = cursor.fetchall()
        id = self.chose(favorites)
        if id == None:
            self.connected()
        cursor.execute(f"SELECT * FROM product WHERE idproduct = '{id[0]}'")
        chosed_product = cursor.fetchall()
        print("Voici le détail du produit choisis.")
        print(chosed_product)
        db_conn.close()
        self.favorite()


    def db_category(self):
        db_conn = connection()
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM category")
        result = cursor.fetchall()
        choosed_category = self.chose(result)
        if choosed_category == None:
            self.connected()
        cursor.execute(f"SELECT product FROM category_product WHERE category='{choosed_category[0]}'")
        result = cursor.fetchall()
        db_conn.close()
        self.db_product(result)


    def db_product(self, product_lists):

        db_conn = connection()
        cursor = db_conn.cursor()
        products = []
        better_products = []

        for product in product_lists:
            cursor.execute(f"SELECT * FROM product WHERE idproduct='{product[0]}'")
            product = cursor.fetchall()
            products.append(product[0])
        db_conn.close()

        chosed_product = self.chose(products)
        if chosed_product == None:
            self.db_category()
        print(f"Le nutriscore du produit choisis est {chosed_product[3]}.")
        if chosed_product[3] == "a":
            self.add_fav(chosed_product)
        else:
            for product in products:
                if product[3] == "a":
                    better_products.append(product)
            if better_products == []:
                print("Il n'y a pas de nutriscore de a dans cette catégorie.")
                self.connected()
            else:
                print("Voici une sélection de produit dont le nutriscore est a.")
                chosed_id = self.chose(better_products) 
                print(chosed_id)
                self.add_fav(chosed_id)
