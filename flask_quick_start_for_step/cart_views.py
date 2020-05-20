from flask import Blueprint

cart_app = Blueprint('cart', __name__)

@cart_app.route('/')
def cart_page():
  return '<h1>Cart</h1>'

@cart_app.route('/pay/')
def cart_pay():
  return '<h1> Pay </h1>'
