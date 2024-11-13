# PRODUCT MANAGEMENT

class Product:                      # Product class 
    # Attributes: product_id, name, category, price, stock_quantity
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
  
    def display_product_details(self):
        print(f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}")

# methods(add,edit,delete and save) products are added in inventory class - which act as controller in IMS.