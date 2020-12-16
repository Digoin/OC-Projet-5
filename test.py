import db_writerv2

category = db_writerv2.Category("pizzas")

categories = set()
products = [product for product in category.get_products()]

for product in products:
    categories.update(product.categories)
print(categories)

# for index, product in enumerate(category.get_products()):
#    products.append(product)
#     if index > 50:
#         break

