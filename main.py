from user import User, Admin
from product import Product
from inventory import Inventory

def main():
    print("Welcome to Ethnic Inventory Management System")

    # By Default Login Credentials - User & Admin
    admin_user = Admin("Manager", "Manager567")
    regular_user = User("user", "user123")

    # Login Page
    username = input("Enter username: ")
    password = input("Enter password: ")

    user = None
    if admin_user.login_auth(username, password):         # check if user is admin or regular user
        user = admin_user
    elif regular_user.login_auth(username, password):
        user = regular_user

    if not user:
        print("Invalid credentials!")
        return

    # Initialize inventory
    inventory = Inventory()

    if isinstance(user, Admin):         # operations display on console
        while True:
            print("\n1. Add Product\n2. Edit Product\n3. Delete Product\n4. View Inventory\n5. Adjust Stock\n6. Search by Name\n7. Filter by Category\n8. View Low Stock\n9. Logout")
            choice = input("Choose an option: ")

            if choice == "1":                 # Add new product to IMS
                product_id = input("Product ID: ")
                name = input("Name: ")
                category = input("Category: ")
                price = int(input("Price: "))
                stock_quantity = int(input("Stock Quantity: "))
                product = Product(product_id, name, category, price, stock_quantity)
                user.add_product(inventory, product)    #add_product method

            elif choice == "2":                   #Edit existing product in IMS
                product_id = input("Product ID to edit: ")
                name = input("New Name (leave blank to skip): ")
                category = input("New Category (leave blank to skip): ")
                price = input("New Price (leave blank to skip): ")
                stock_quantity = input("New Stock Quantity (leave blank to skip): ")
                user.edit_product(inventory,product_id,      #edit_product method
                    name=name if name else None,
                    category=category if category else None,
                    price=float(price) if price else None,
                    stock_quantity=int(stock_quantity) if stock_quantity else None
                )

            elif choice == "3":       #Delete product from database(csv file)
                product_id = input("Product ID to delete: ")
                user.delete_product(inventory, product_id)   #delete_product method 

            elif choice == "4":       #View Inventory
                user.view_inventory(inventory)

            elif choice == "5":        #Adjust & Track Stocks
                product_id = input("Product ID to adjust stock: ")
                quantity = int(input("Enter quantity (add, reduce): "))
                user.adjust_stock(inventory, product_id, quantity)
            
            elif choice == "6":            # Search by product name 
                name = input("Enter product name to search: ")
                inventory.search_product_by_name(name)

            elif choice == "7":             # Search by category
                category = input("Enter category to filter by: ")
                inventory.filter_by_category(category)

            elif choice == "8":
                inventory.filter_low_stock()

            elif choice == "9":      #Logout- leave IMS/ console based application
                print("Thank you for visiting our system")
                break

            else:
                print("Invalid option.")
    else: 
        user.view_inventory(inventory)   # User role can only view inventory

if __name__ == "__main__":
    main()
