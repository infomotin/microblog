from src import app
from flask import render_template,redirect,flash
from src.forms import RegistrationForm, LoginForm

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
        flash(
            f'Account Create Sucssess {form.username.data}', category='success')
        return redirect('login')
    return render_template('register.html', title='Register', form=form)
# Login the routes in the app
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'motin@gmail.com' and form.password.data =="123456789":
            flash(f'Login sucssess {form.email.data}', category='success')
            return redirect('account')
        else:
            flash(f'Login unsucssess {form.email.data}', category='danger')
            return redirect('register')
    return render_template('Login.html', title='Login',form=form)
