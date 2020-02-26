import os
import functools
import json
from flask import Blueprint, request, jsonify, make_response, current_app
from flask.views import MethodView
from .. import db


bp = Blueprint('products', __name__, '/')

def login_required(f):
    @functools.wraps(f)
    def wrapped_view(*args, **kwargs):
        print("hola")

        return f(*args, **kwargs)

    return wrapped_view

class ProductView(MethodView):

    @login_required
    def get(self):
        cur = db.connection.cursor()
        cur.execute('SELECT * FROM Product')
        row_headers=[x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data=[]

        for result in rv:
            json_data.append(dict(zip(row_headers,result)))

        return json.dumps(json_data)

    @login_required
    def post(self):
        data = request.get_json()

        if data:
            nombre = data['nombre']
            descripcion = data['descripcion']
            precio = data['precio']
            product_owner = data['product_owner']
            try:
                cur = db.connection.cursor()
                cur.execute('INSERT INTO Product (NAME, DESCRIPTION, PRICE , PRODUCT_OWNER) VALUES (%s,%s,%s,%s)',(nombre, descripcion, precio, product_owner))
                db.connection.commit()
                return make_response(jsonify({'message': 'Product registered'}))
            except Exception as e:
                return make_response(jsonify({'error': str(e)}))
        return make_response(jsonify({"message": "Introduce algun producto"}))


products_view = ProductView.as_view('product')
bp.add_url_rule('/products', view_func=products_view, methods=['GET', 'POST'])