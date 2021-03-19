from flask import url_for
from flask_testing import TestCase
from application import db
from application.models import Customers, Products, Purchases
from app import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
            )
        return app
    def setUp(self):
        db.create_all()
        customer = Customers(first_name="Testfirstname", last_name = "Testlastname")
        product = Products(product_name ="Pepsitest", product_quantity = "1")
        purchase = Purchases(customer_id = 1, product_id = 1)
        db.session.add(customer)
        db.session.commit()
        db.session.add(product)
        db.session.commit()
        db.session.add(purchase)
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestAddCustomers(TestBase):
    def test_add_customer(self):
        response = self.client.get(url_for('addcustomer'))
        self.assertEqual(response.status_code, 200)

class TestAddProducts(TestBase):
    def test_add_product(self):
        response = self.client.get(url_for('addproduct', cid=1))
        self.assertEqual(response.status_code, 200)

class TestAddPurchase(TestBase):
    def test_add_Purchase(self):
        response = self.client.get(url_for('add_orders', cid=1, pid=1))
        self.assertEqual(response.status_code, 200)

class TestReadCustomer(TestBase):
    def test_read_customer(self):
        response = self.client.get(url_for('read_customers'))
        self.assertEqual(response.status_code, 200)

class TestReadProducts(TestBase):
    def test_read_products(self):
        response = self.client.get(url_for('read_products'))
        self.assertEqual(response.status_code, 200)

class TestReadPurchases(TestBase):
    def test_read_purchase(self):
        response = self.client.get(url_for('read_purchases'))
        self.assertEqual(response.status_code, 200)

class TestUpdateCustomer(TestBase):
    def test_update_customer(self):
        response = self.client.get(url_for('update_customer', cid=1))
        self.assertEqual(response.status_code, 200)

class TestUpdateProducts(TestBase):
    def test_update_product(self):
        response = self.client.get(url_for('update_product', pid=1))
        self.assertEqual(response.status_code, 200)

class TestDeleteCustomer(TestBase):
    def test_delete_customer(self):
        response = self.client.get(url_for('delete_customer', cid=1))
        self.assertEqual(response.status_code, 302)

class TestDeleteProducts(TestBase):
    def test_delete_product(self):
        response = self.client.get(url_for('delete_product', pid=1))
        self.assertEqual(response.status_code, 302)

class TestDeletePurchase(TestBase):
    def test_delete_purchase(self):
        response = self.client.get(url_for('delete_purchase', rid=1))
        self.assertEqual(response.status_code, 302)

class TestAddCustomerDB(TestBase):
    def test_add_customerDB(self):
        response = self.client.post(url_for('addcustomer'),
            data = dict(first_name="Testfirstname"),
            follow_redirects=True
        )
        self.assertIn(b'Testfirstname', response.data)

class TestAddProductDB(TestBase):
    def test_add_productDB(self):
        response = self.client.post(url_for('addproduct', cid=1),
            data = dict(product_name="Pepsi"),
            follow_redirects=True
        )
        self.assertIn(b'Pepsi', response.data)

class TestAddPurchaseDB(TestBase):
    def test_add_productDB(self):
        response = self.client.post(url_for('add_orders', cid=1, pid=1),
            data = dict(customer_id="1"),
            follow_redirects=True
        )
        self.assertIn(b'1', response.data)

