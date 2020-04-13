import numpy as np
import sqlite3
from . import cookies
from flask import Flask, render_template, redirect, abort, request, url_for, make_response, session
from markupsafe import escape
from .DatabaseStorage import SQLiteStorage

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

db = SQLiteStorage.SQLiteStorage()

# Home
@app.route('/')
def home():
    if not cookies.has_cookies(request):
        resp = make_response(render_template(
            'home.html', title='Home', items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
    else:
        resp = make_response(
            render_template(
                'home.html',
                title='Home',
                items_amount=db.getItemsAmount(request.cookies.get('userid'))
            )
        )

    return resp


# Collection
@app.route('/collection')
def collection():
    url_args = list(request.args.keys())
    sort_by = 'Sort by'
    gender = 'forall'
    categories = 'None'
    if all(i in url_args for i in ['sort', 'gender', 'cats']):
        sort_by = request.args.get('sort')
        gender = request.args.get('gender')
        categories = request.args.getlist('cats')

    data = db.getData(gender, sort_by, categories)

    if not cookies.has_cookies(request):
        resp = make_response(
            render_template(
                'collection.html',
                title='Collection',
                goods=np.array(data),
                items_amount=0)
        )
        resp.set_cookie('userid', cookies.get_userid())
    else:
        resp = make_response(
            render_template(
                'collection.html',
                title='Collection',
                goods=np.array(data),
                items_amount=db.getItemsAmount(request.cookies.get('userid'))
            )
        )

    return resp


# Cart
@app.route('/cart')
def cart():
    if not cookies.has_cookies(request):
        resp = make_response(render_template(
            'cart.html', title='Cart', items_amount=0, cart=None))
        resp.set_cookie('userid', cookies.get_userid())
    else:
        userid = request.cookies.get('userid')
        cart = db.selectCart(userid)
        # Get total check price
        total_price = sum([item[5] if cart else 0 for item in cart])
        resp = make_response(
            render_template(
                'cart.html',
                title='Cart',
                items_amount=db.getItemsAmount(userid),
                cart=cart,
                total_price=total_price
            )
        )

    return resp


# Item
@app.route('/item/<vendor>')
def item(vendor):
    if not cookies.has_cookies(request):
        resp = make_response(render_template(
            'item.html', vendor=vendor, items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
    else:
        resp = make_response(
            render_template(
                'item.html',
                vendor=vendor,
                items_amount=db.getItemsAmount(request.cookies.get('userid'))
            )
        )

    return resp


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    userid = request.cookies.get('userid')
    vendor = request.form.get('vendor')
    size = request.form.get('size')

    db.insertIntoCart(userid, vendor, size)
    goods_amount = db.getItemsAmount(userid)

    return str(goods_amount)


if __name__ == '__main__':
    app.run(debug=True)
