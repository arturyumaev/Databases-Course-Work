from flask import Flask
from flask import render_template

app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('home.html')

# About us
@app.route('/about_us/')
def about_us():
    return render_template('about_us.html')

# Male
@app.route('/male/')
@app.route('/male/<category>/<vendor>')
def male(category=None, vendor=None):
    if category != None and vendor != None:
        return category + '/' + vendor

    return 'Male'

# Female
@app.route('/female/')
def female():
    return 'Female'

if __name__ == '__main__':
    app.run()
