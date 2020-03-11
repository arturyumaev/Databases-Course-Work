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
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('home.html', title='Home'))
    return resp


# Collection
@app.route('/collection')
def collection():
    data = db_manager.get_data(request)
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('collection.html', title='Collection', goods=np.array(data)))
    return resp


# About us
@app.route('/about_us')
def about_us():
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('about_us.html', title='About us'))
    return resp


# Cart
@app.route('/cart')
def cart():
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('cart.html', title='Cart'))
    return resp


# Login
@app.route('/login')
def login():
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('login.html', title='Log in'))
    return resp


# Item
@app.route('/item/<vendor>')
def item(vendor):
    resp = cookies.validate_cookies(request=request,
                                    resp_obj=render_template('item.html', vendor=vendor))
    return resp

if __name__ == '__main__':
    app.run(debug=True)
