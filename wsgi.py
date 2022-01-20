# wsgi.py
# pylint: disable=missing-docstring
# import os
# import logging
# logging.warn(os.environ["DUMMY"])
# wsgi.py
# pylint: disable=missing-docstring

BASE_URL = '/api/v1'

from flask import abort, request
from flask_migrate import Migrate
from flask import Flask
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
migrate = Migrate(app, db)

from schemas import ProductSchema, many_product_schema, one_product_schema

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_many_product():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['GET'])
def read_one_product(product_id):
    products = db.session.query(Product).get(int(product_id))   

    if products is None:
        abort(404)

    return one_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/delete/<int:product_id>', methods=['GET'])
def delete_one_product(product_id):
 
    product=db.session.query(Product).get(product_id)
    db.session.delete(product)
    db.session.commit()
    
    products = db.session.query(Product).all()

    return many_product_schema.jsonify(products), 200

@app.route(f'{BASE_URL}/products/create/<name>', methods=['GET'])
def create_one_product(name):
    
    product=Product()
    product.name=name
    db.session.add(product)
    db.session.commit()
    products = db.session.query(Product).all()

 
    return many_product_schema.jsonify(products), 200  # Créé

@app.route(f'{BASE_URL}/products/update/<int:product_id>/<name>', methods=['GET'])
def update_one_product(product_id,name):
   
    product=db.session.query(Product).get(product_id)    

    if product is None:
        abort(404)

    product.name=name
    db.session.commit()
#    PRODUCTS[product_id]['name'] = name
    products = db.session.query(Product).all()
    return many_product_schema.jsonify(products), 200  # Créé
    # Action de mise à jour (méthode UPDATE) pas besoin de retourner l'entité puisque nous savons ce que nous avons modifié.
    return '', 204