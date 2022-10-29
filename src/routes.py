from src import app, db, bcrypt
from flask import render_template, request, redirect, url_for
from flask import render_template,redirect,flash
from src.forms import RegistrationForm, LoginForm
from src.models import User

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
    
# Register the routes in the app
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # to insert data into the database using try and except
        encripted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        try:
            user = User(email=form.email.data,
                        username=form.username.data, 
                        password=encripted_password)
            # insert the user into the database
            db.session.add(user)
            db.session.commit()
            flash(f'Account Create Sucssess {form.username.data}', category='success')
            return redirect('login')
        except:
            flash(f'Account Create Failed {form.username.data}', category='danger')
    return render_template('register.html', title='Register', form=form)
# Login the routes in the app
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # if the user is in the database 
        user = User.query.filter_by(email=form.email.data).first()
        # now check if the user and password is in the database
        if user and user.password == form.password.data:
            flash(f'Login sucssess {form.email.data}', category='success',)
            return redirect('account')
        else:
            flash(f'Login unsucssess {form.email.data}', category='danger')
            return redirect('register')
    return render_template('Login.html', title='Login',form=form)
