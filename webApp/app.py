import numpy as np
import redis
import sqlite3
import cookies
from flask import Flask, render_template, redirect, abort, request, url_for, make_response, session
from markupsafe import escape

from DatabaseStorage.SQLiteStorage import SQLiteStorage
from BusinessRules.CartController  import CartController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLiteStorage()
cartController = CartController()
cartSessionStorage = {}


# Home
@app.route('/')
def home():
    if not cookies.hasCookies(request):
        userSessionId = cookies.getUserSessionId()
        cartController.generateCart(userSessionId)

        resp = make_response(render_template('home.html', title='Home', items_amount=0))
        resp.set_cookie('userid', userSessionId)
    else:
        userSessionId = request.cookies.get('userid')
        cartItemsQuantity = cartController.getCart(userSessionId).itemsQuantity

        resp = make_response(
            render_template(
                'home.html',
                title='Home',
                items_amount=cartItemsQuantity
            )
        )

    return resp


# Collection
@app.route('/collection')
def collection():
    url_args = list(request.args.keys())
    sort_by, gender, categories = 'Sort by', 'forall', 'None'
    if all(i in url_args for i in ['sort', 'gender', 'cats']):
        sort_by = request.args.get('sort')
        gender = request.args.get('gender')
        categories = request.args.getlist('cats')

    data = db.getData(gender, sort_by, categories)

    if not cookies.hasCookies(request):
        userSessionId = cookies.getUserSessionId()
        cartController.generateCart(userSessionId)

        resp = make_response(
            render_template(
                'collection.html',
                title='Collection',
                goods=np.array(data),
                items_amount=0)
        )
        resp.set_cookie('userid', userSessionId)
    else:
        userSessionId = request.cookies.get('userid')
        cartItemsQuantity = cartController.getCart(userSessionId).itemsQuantity

        resp = make_response(
            render_template(
                'collection.html',
                title='Collection',
                goods=np.array(data),
                items_amount=cartItemsQuantity
            )
        )

    return resp


# Cart
@app.route('/cart')
def cart():
    if not cookies.hasCookies(request):
        userSessionId = cookies.getUserSessionId()
        cartController.generateCart(userSessionId)

        resp = make_response(render_template('cart.html', title='Cart', items_amount=0, cart=None))
        resp.set_cookie('userid', userSessionId)
    else:
        userSessionId = request.cookies.get('userid')
        cart = cartController.getCart(userSessionId)

        resp = make_response(
            render_template(
                'cart.html',
                title='Cart',
                items_amount=cart.itemsQuantity,
                cart=cart.items,
                total_price=cart.totalOrderPrice
            )
        )

    return resp


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    userSessionId = request.cookies.get('userid')
    cart = cartController.getCart(userSessionId)
    
    vendor = request.form.get('vendor')
    size = request.form.get('size')
    price = db.getItemPrice(vendor)[0][0]
    
    cart.addItem(vendor, size, price)
    cartItemsQuantity = cart.itemsQuantity

    cartController.updateCart(userSessionId, cart)

    return str(cartItemsQuantity)


@app.route('/remove_item_from_cart/<vendor>/<size>', methods=['POST', 'GET'])
def remove_item_from_cart(vendor, size):
    userSessionId = request.cookies.get('userid')
    cart = cartController.getCart(userSessionId)
    price = db.getItemPrice(vendor)[0][0]
    cart.removeItem(vendor, size, price)
    cartController.updateCart(userSessionId, cart)

    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
