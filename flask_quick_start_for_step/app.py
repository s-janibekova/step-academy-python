from flask import Flask, request, render_template
from werkzeug.exceptions import NotFound
from cart_views import cart_app
from products_views import products_app



app = Flask(__name__)

app.register_blueprint(products_app, url_prefix='/products/')
app.register_blueprint(cart_app, url_prefix='/cart/')


@app.route('/')
@app.route('/<int:user_id>')
@app.route('/<name>', methods=['GET', 'POST', 'PUT'])
def index_page(name=None, user_id=None):
  if request.method == 'GET':
    # justname = name if name else 'DefaultName'
    justname = name or "DefaultName"
    response =  render_template('index.html',
                                name='World',
                                args=request.args,
                                products=["apple", "banana"],
                                justname=justname,
                                user_id=user_id)
    return response
  return f'hello {request.method} request'


@app.route('/404/')
def not_found():
  raise NotFound


app.run('localhost', 8000, debug=True)
