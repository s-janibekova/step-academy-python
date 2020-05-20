from flask import Blueprint

products_app = Blueprint('products', __name__)

@products_app.route('/')
def products_list():
  return '<h1>Products all</h1>'

@products_app.route('/<int:product_id>/')
def product_detail(product_id):
  return f'<h1> Product {product_id}</h1>'
