from flask import Flask, render_template, redirect, abort, request, url_for, make_response, session
from markupsafe import escape
import sqlite3
from . import db_manager
from . import cookies
import numpy as np


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# Home
@app.route('/')
def home():
    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('home.html', title='Home', items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('home.html', title='Home', items_amount=items_amount))

    return resp


# Collection
@app.route('/collection')
def collection():
    data = db_manager.get_data(request)

    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('collection.html', title='Collection', goods=np.array(data), items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('collection.html', title='Collection', goods=np.array(data), items_amount=items_amount))

    return resp


# About us
@app.route('/about_us')
def about_us():
    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('about_us.html', title='About us', items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('about_us.html', title='About us', items_amount=items_amount))

    return resp


# Cart
@app.route('/cart')
def cart():
    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('cart.html', title='Cart', items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('cart.html', title='Cart', items_amount=items_amount))

    return resp


# Login
@app.route('/login')
def login():
    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('login.html', title='Log in', items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('login.html', title='Log in', items_amount=items_amount))

    return resp


# Item
@app.route('/item/<vendor>')
def item(vendor):    
    if not cookies.has_cookies(request):
        print("No cookies")
        resp = make_response(render_template('item.html', vendor=vendor, items_amount=0))
        resp.set_cookie('userid', cookies.get_userid())
        print("New cookies set, amount of items = 0")
    else:
        userid = request.cookies.get('userid')
        items_amount = db_manager.get_items_amount(userid)
        resp = make_response(render_template('item.html', vendor=vendor, items_amount=items_amount))

    return resp


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    userid = request.cookies.get('userid')
    vendor = request.form.get('vendor')
    size = request.form.get('size')

    print('\nNew request from', userid)
    print(request.form)
    goods_amount = db_manager.insert_into_cart(userid, vendor, size)
    print()

    return str(goods_amount)

if __name__ == '__main__':
    app.run(debug=True)
