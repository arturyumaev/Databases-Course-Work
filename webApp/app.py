from flask import Flask, render_template, redirect, abort, request, url_for
from markupsafe import escape

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html', title='Home')

# Collection
@app.route('/collection')
def collection():
    
    if len(request.args) != 0:
        sort_by = request.args.get('sort')
        gender = request.args.get('gender')
        categories = request.args.getlist('cats')

        print(sort_by)
        print(gender)
        print(categories)

        return render_template('collection.html', title='Collection', goods='Boogie')
    else:
        return render_template('collection.html', title='Collection')

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
