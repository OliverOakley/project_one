from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, IntegerField, DecimalField, SelectField

class AddCustomerForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    submit = SubmitField('Add User')

class AddProductForm(FlaskForm):
    product_name = SelectField('Product', choices=['Pepsi', 'Pepsi Max', 'Pepsi Max Cherry', 'Pepsi Max Raspberry', 'Pepsi Max Ginger'])
    product_quantity = StringField('Amount')
    submit = SubmitField('Add Product')

class PurchasesForm(FlaskForm):
    customer_id = IntegerField('Customer ID')
    product_id = IntegerField('Product ID')
    submit = SubmitField('Complete Order')