from application import app, db

class Purchases(db.Model):
    __tablename__ = "Purchases"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column('Customers_id', db.Integer, db.ForeignKey('Customers.id'))
    product_id = db.Column('Products_id', db.Integer, db.ForeignKey('Products.id'))

class Customers(db.Model):
    __tablename__ = "Customers"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    Purchases = db.relationship('Purchases', backref='Customers')

class Products(db.Model):
    __tablename__ = "Products"
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(30), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    Purchases = db.relationship('Purchases', backref='Products')