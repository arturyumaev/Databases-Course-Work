from flask import Flask, render_template, redirect, abort, request, url_for
from markupsafe import escape
import sqlite3
from .db_manager import make_sql_query
import numpy as np

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html', title='Home')

# Collection
@app.route('/collection')
def collection():
    url_args = list(request.args.keys())
    if all(i in url_args for i in ['sort', 'gender', 'cats']):
        sort_by = request.args.get('sort')
        gender = request.args.get('gender')
        categories = request.args.getlist('cats')

    else:
        sort_by = 'Sort by'
        gender = 'forall'
        categories = 'None'

    data = make_sql_query(gender, sort_by, categories)

    for i in data:
        print(i)

    print()
        
    return render_template('collection.html', title='Collection', goods=np.array(data))

# About us
@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About us')

# Cart
@app.route('/cart')
def cart():
    return render_template('cart.html', title='Cart')

# Login
@app.route('/login')
def login():
    return render_template('login.html', title='Log in')

# Item
@app.route('/item/<vendor>')
def item(vendor):
    return render_template('item.html', vendor=vendor)

if __name__ == '__main__':
    app.run(debug=True)
