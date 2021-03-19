from application import app, db, forms 
from application.models import Purchases, Customers, Products
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/addcustomer', methods=['GET', 'POST'])
def addcustomer():
    form=forms.AddCustomerForm()
    if request.method=='POST':
        first_name=form.first_name.data
        last_name=form.last_name.data 
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            customer_to_add=Customers(first_name= form.first_name.data, last_name=form.last_name.data)
            db.session.add(customer_to_add)
            cid = db.session.query(Customers).order_by(Customers.id.desc()).first().id
            db.session.commit()
            return redirect(url_for('addproduct', cid=cid))
    return render_template('addcustomer.html',form=form)

@app.route('/addproduct/<cid>', methods=['GET', 'POST'])
def addproduct(cid):
    form=forms.AddProductForm()
    if request.method=='POST':
        product_name=form.product_name.data
        product_quantity=form.product_quantity.data
        if len(product_quantity) == 0:
            error = "Please supply at least 1 product purchase"
        else:
            product_to_add=Products(product_name= form.product_name.data, product_quantity=form.product_quantity.data)
            db.session.add(product_to_add)
            cid = db.session.query(Customers).order_by(Customers.id.desc()).first().id
            pid = db.session.query(Products).order_by(Products.id.desc()).first().id
            db.session.commit()
            return redirect(url_for('add_orders',cid=cid, pid=pid))
    return render_template('addproduct.html',form=form)

@app.route('/addpurchases/<cid>/<pid>', methods=['GET', 'POST'])
def add_orders(cid, pid):
    form=forms.PurchasesForm()
    form.customer_id.data = cid
    form.product_id.data = pid
    if request.method=='POST':
        customer_id=form.customer_id.data
        product_id=form.product_id.data
        if product_id == 0 or customer_id == 0:
            error = "IDs are Incorrect"
        else:
            purchases_to_add=Purchases(customer_id= form.customer_id.data, product_id=form.product_id.data)
            db.session.add(purchases_to_add)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('addpurchase.html',form=form)

@app.route('/readcustomers', methods=['GET','POST'])
def read_customers():
    customer=Customers.query.all()
    return render_template('readcustomers.html', customer=customer)

@app.route('/updatecustomer/<int:cid>', methods=['GET','POST'])
def update_customer(cid):
    customer_to_update = Customers.query.filter_by(id=cid).first()
    error = ""
    form = forms.AddCustomerForm()

    if request.method == 'POST':
        customer_to_update.first_name = form.first_name.data
        customer_to_update.last_name = form.last_name.data

        if len(str(form.first_name.data)) == 0 or len(str(form.last_name.data)) == 0:
            error = "Please enter your name"
            
        else:
            db.session.commit()
            return redirect('/readcustomers')

    else:
        form.first_name.data = customer_to_update.first_name
        form.last_name.data = customer_to_update.last_name
    

    return render_template('addcustomer.html', form=form, message=error)

@app.route('/deletecustomer/<cid>')
def delete_customer(cid):
    customer_to_delete = Customers.query.filter_by(id=cid).first()
    db.session.delete(customer_to_delete)
    db.session.commit()
    return redirect("/readcustomers")

@app.route('/readproducts', methods=['GET','POST'])
def read_products():
    product=Products.query.all()
    return render_template('readproducts.html', product=product)

@app.route('/updateproduct/<int:pid>', methods=['GET','POST'])
def update_product(pid):
    product_to_update = Products.query.filter_by(id=pid).first()
    error = ""
    form = forms.AddProductForm()

    if request.method == 'POST':
        product_to_update.product_name = form.product_name.data
        product_to_update.product_quantity = form.product_quantity.data

        if len(form.product_quantity.data) == 0:
            error = "Please supply at least 1 product purchase"
            
        else:
            db.session.commit()
            return redirect('/readproducts')

    else:
        form.product_name.data = product_to_update.product_name
        form.product_quantity.data = product_to_update.product_quantity

    return render_template('addproduct.html', form=form, message=error)

@app.route('/deleteproduct/<pid>')
def delete_product(pid):
    product_to_delete = Products.query.filter_by(id=pid).first()
    db.session.delete(product_to_delete)
    db.session.commit()
    return redirect("/readproducts")

@app.route('/readpurchases', methods=['GET','POST'])
def read_purchases():
    purchase=Purchases.query.all()
    return render_template('readpurchases.html', purchase=purchase)

@app.route('/deletepurchase/<rid>')
def delete_purchase(rid):
    purchase_to_delete = Purchases.query.filter_by(id=rid).first()
    db.session.delete(purchase_to_delete)
    db.session.commit()
    return redirect("/readpurchases")