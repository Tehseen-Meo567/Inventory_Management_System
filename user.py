# User Authentication and Role (User & Admin) Management 

                 #USER - PARENT CLASS
class User:                                   
    def __init__(self, username, password, role="User"):    # attributes- username ,password
        self.username = username
        self.password = password
        self.role = role

    def login_auth(self, username, password):  #User Authetication-match username and password
        return self.username == username and self.password == password

    def view_inventory(self, inventory):   # User(Regular user) can only view inventory details
        inventory.display_inventory()

                 # ADMIN - CHILD CLASS
class Admin(User):         # Admin - inherit attributes from parent class
    def __init__(self, username, password):
        super().__init__(username, password, role="Admin")
    
    #Admin has more functionalities- add,edit,delete products, adjust stock
    def add_product(self, inventory, product):  
        inventory.add_product(product)

    def edit_product(self, inventory, product_id, **new_data): #keyword argument- store in dictionary
        inventory.edit_product(product_id, **new_data)

    def delete_product(self, inventory, product_id):
        inventory.delete_product(product_id)

    def adjust_stock(self, inventory, product_id, quantity):   #Adjust stock
        inventory.adjust_stock(product_id, quantity)
