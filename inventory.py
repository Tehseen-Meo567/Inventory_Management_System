import csv
from product import Product

# Inventory class Operations: Track Stock Levels,Product search and Filtering
class Inventory:
    FILE_PATH = "products.csv"   # save and update products in database csv file
    LOW_STOCK_THRESHOLD = 5  # Threshold for low stock level-alert

    def __init__(self):
        self.products = self.load_products()
         
        # DATABASE : LOAD AND SAVE PRODUCTS 
    def load_products(self):
        products = {}
        try:                                    #Error Handling
            with open(self.FILE_PATH, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = Product(
                        product_id=row["product_id"],
                        name=row["name"],
                        category=row["category"],
                        price=float(row["price"]),
                        stock_quantity=int(row["stock_quantity"])
                    )
                    products[product.product_id] = product
        except FileNotFoundError:
            print("No products file found, starting with an empty inventory.")
        return products

    def save_products(self):
        with open(self.FILE_PATH, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["product_id", "name", "category", "price", "stock_quantity"])
            for product in self.products.values():
                writer.writerow([product.product_id, product.name, product.category, product.price, product.stock_quantity])

# Inventory System main operations
      # ADD PRODUCTS
    def add_product(self, product):                # child class of Parent class (Inheritance)
        if product.product_id in self.products:    #product_id is attribute of Product class
            print("Product ID already exists.")
        else:
            self.products[product.product_id] = product
            self.save_products()                         # save in database
            print(f"Product '{product.name}' added successfully!")
       
       #EDIT PRODUCTS
    def edit_product(self, product_id, **new_data):
        product = self.products.get(product_id)
        if product:
            product.name = new_data.get("name", product.name)
            product.category = new_data.get("category", product.category)
            product.price = new_data.get("price", product.price)
            product.stock_quantity = new_data.get("stock_quantity", product.stock_quantity)
            self.save_products()
            print(f"Product '{product_id}' updated successfully.")
        else:
            print("Product not found.")
          
          #DELETE PRODUCTS
    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            self.save_products()
            print(f"Product '{product_id}' deleted successfully.")
        else:
            print("Product not found.Cannot delete non-existent product.")
          
          # VIEW INVENTORY (user and Admin)
    def display_inventory(self):
        print("Inventory:")
        for product in self.products.values():
            product.display_product_details()
            # Trigger a low-stock alert if stock is below the threshold
            if product.stock_quantity <= self.LOW_STOCK_THRESHOLD:
                print(f"Warning: '{product.name}' is low in stock. Consider restocking.")  #alert ,track stocks
           
        # ADJUST STOCKS
    def adjust_stock(self, product_id, quantity):
        product = self.products.get(product_id)
        if product:
            product.stock_quantity += quantity       # add new product quantity or we can also append function
            self.save_products()
            print(f"Adjusted stock for '{product.name}' by {quantity}. New stock: {product.stock_quantity}")
        else:
            print("Product not found.")
 
          # SEARCH PRODUCTS BY NAME
    def search_product_by_name(self, name):
        results = [p for p in self.products.values() if p.name.lower() == name.lower()]
        if results:
            for product in results:
                product.display_product_details()
        else:
            print("No products found with that name.")
 
              # SEARCH  PRODUCT BY CATEGORY
    def filter_by_category(self, category):
        results = [p for p in self.products.values() if p.category.lower() == category.lower()]
        if results:
            print(f"Products in category '{category}':")
            for product in results:
                product.display_product_details()
        else:
            print(f"No products found in category '{category}'.")
 
               # FILTER LOW STOCKS
    def filter_low_stock(self):
        low_stock_products = [p for p in self.products.values() if p.stock_quantity <= self.LOW_STOCK_THRESHOLD]
        if low_stock_products:
            print("Low-stock products:")
            for product in low_stock_products:
                product.display_product_details()
        else:
            print("No products are currently low in stock.")

