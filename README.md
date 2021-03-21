# QA Fundamentals Project - Pepsi Purchases

Pepsi Purchases is a simple CRUD application where people can create a user and order products (namely Pepsi products).

It is my first individual project as part of the QA DevOps training. 

DISCLAIMER: This application has been purely built for educational purposes as part of QA training, and is not to be officially deployed. I do not actually sell Pepsi.

## User Stories:

An 'epic' outlining what functionality different users of the Pepsi Purchases application may require. 

1. As a customer, I want to be able to create a user on Pepsi Purchases, so that I can order Pepsi.
    * Task - Have a user interface for customers to interact.
    * Task - Have create functionality for a user, such as their first name, last name, and contact details. 
2. As a customer, I want to be able to personalise orders, so that I can recieve the particular product in the quantity I want.
    * Task - Have create functionality for products, such as product type and quantity.
3. As a customer, I want to be able to update my user or orders, so that I can edit any mistakes I make when setting up a user or ordering Pepsi.
    * Task - Have update functionality for both users and products.
4. As a customer, I want to be able to delete my registered user and product orders, in case I change my mind comppletely.
    * Task - Have delete functionality for both users and products.
5. As a seller, I want to be able to view the users and what they have ordered, so that I can fulfill those orders.
    * Task - Have tables of users and products, and a table that links the two (a 'purchase' table).
    * Task - Have a databse to store users, products, and purchases.
    * Task - Have read functionality for users, products, and purchases. 

## Risk Assessment:

An outline of some of the potential risks with the Pepsi Purchases application.
 
* Unsecure storage of customers personal information, such as their usernames.
* All users have access to all of the functionality of the application - such as deleting other people's orders.
* Potential cease-and-desist from Pepsi.

## Features:
 
An outline of the current features of the Pepsi Purchases application.
 
* A user interface so that customers/sellers can create, read, update, and delete users, orders, and purchases.
* A database that stores three tables:
    * Customers table - Stores first name and last name of customers.
    * Products table - Stores the 6 available products that customers can choose from, and the quantities they want.
    * Purchases table - Relational table that relates the customers table to the products table by using their IDs.
* Fully designed test suites.
* Code is integrated into a Version Control System and built through a CI server.

## Framework: 
 
The different technologies used for the application.
 
* Cloud Server - GCP VM. 
* Database - GCP SQL server.
* Back-end - Python.
* Testing - Pytest.
* Front-end - Flask and HTML.
* Version Control - Git.
* CI Server - Jenkins.
 
## Usage:

Outlines the structure of the application, and how to use the application from a developer's perspective.
 
* The entirety of the project is stored in the folder 'project_one'.
    * It is recommended to run this application on the virtual environment by executing 'source ./venv/bin/activate'.
* Required technologies are stored in the 'requirements.txt' file.
    * Executing 'pip3 install -r requirements.txt' will install all of the required technologies to run the application.
* The file 'create.py' connects the application to the database.
    * Executing 'python3 create.py' will delete all current tables in the database and create new ones.
* Executing 'python3 app.py' will run the program.
* The 'application' folder stores the back end of the application.
    * 'models.py' defines the tables in the database.
    * 'forms.py' defines the Flask forms that users fill in.
    * 'routes.py' defines the different pages of the application and how they are routed to each others.
    * 'templates' folder stores the html templates for the front-end. 
* The 'tests' folder stores the test suite for the application.
 
## Testing:

Outlines how to test the application, and what has currently been testing.

* To test, one needs to:
    1. cd into project_one/tests.
    2. Execute 'pytest test_app.py --cov=application'
    3. This tests the forms, models, and routes of the application, and returns the test coverage.

* Current test coverage is at 84%.

## Credits:

The application idea was mine, spurred by the QA DevOps Fundamentals project specification.
Whilst the code is entirely my own, I owe a lot to the QA Community website, my trainer Dara Oladapo, and other QA Trainees.
Pepsi and all associated products belong entirely to PepsiCo.