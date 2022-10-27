
from src import app
from flask import render_template

# home route for the app
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('home.html', title='Home')

# about route for the app
@app.route('/about')
def about():
    return render_template('About.html', title='About')

# contact route for the app
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

#Account route for the app
@app.route('/account')
def account():
    return render_template('Account.html', title='Account')


