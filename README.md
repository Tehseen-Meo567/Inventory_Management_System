# Inventory Management System (IMS)
Inventory Management System (IMS) is a system that manages inventory for a small business. 
This system allows  multiple users with role-based permissions.

### Admin Functionalities:
- Create, Edit, Delete, update Products and View Inventory
- Keep Track of Stock Levels,searching by product name or category, and filtering by stock levels.
- If stock is below threshold, it will send warning to restock and update stocks/products in database(csv) file.

### Regular User Functionalities:
- Only view Inventory details

### Goals of our Inventory Management System 
<img width="575" alt="GOALS" src="https://github.com/user-attachments/assets/488488e3-f850-4163-b0a0-eff3bdc37d05">

### Flowchart of IMS
It gives a small picture how IMS works.

<img width="533" alt="FLOWCHART" src="https://github.com/user-attachments/assets/899b4f23-4bca-4366-b6ce-74e9ab6562a2">

### PRODUCT DATABASE/CSV FILE
It shows product_id, name, category, price, and stock quantity. If stock quantity is less than or equal to 5 (which is threshold), inventory system will give warning/alert regarding restocking. Moreover, Admin can filter out the product through its category or name having less stocks and eventually update products.

![image](https://github.com/user-attachments/assets/eb06a76f-0504-47a8-9042-382402b744c3)

# Implementation of IMS
 - Step 1- 'user.py' contains user authentication and role management,basic login system with username and password validation.
 
 - Step 2- 'product.py' have information related to product;its product_id, name, category, price, and stock_quantity
 
 - Step 3- 'inventory.py' has details about tracking stocks,edit,add,update,view,restock update,search by product name, filter by category and filter low level stocks
 
 - Step 4- 'main.py' has console based display of Inventory management system.

## Make a Docker image of IMS
- Step 5- Use 'Dockerfile' given
  
- Step 6- Write these commands in command line or terminal. 'inventory_management' is name of docker image.

   ```
    docker build -t inventory_management .
   
    docker run -it inventory_management

On Docker Desktop and VS CODE, docker image is built and shown below:

<img width="954" alt="docker desktop ims sytem" src="https://github.com/user-attachments/assets/af40db78-7113-42c0-bae6-3b88e3ff24d2">

<img width="605" alt="docker2" src="https://github.com/user-attachments/assets/9644e297-518b-4f4e-9d02-185204230d87">

## Output of IMS
FOR ADMIN:  (more control)
- username: Manager
- password: Manager567
  
FOR REGULAR USER:  (can only view inventory details)
- username: user
- password: user123 
<img width="602" alt="image" src="https://github.com/user-attachments/assets/870e39bc-7fe7-4f82-bce7-96c45687bcb1">

