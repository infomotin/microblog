from src import app, db, bcrypt
from flask import render_template, request, redirect, url_for
from flask import render_template,redirect,flash
from src.forms import RegistrationForm, LoginForm, ReserPasswordForm, ResetPasswordForm
from src.models import User
from flask_login import login_user, current_user, logout_user, login_required
# home route for the app
@app.route('/')
@app.route('/homepage')
def homepage():
    isAuth = current_user.is_authenticated
    return render_template('home.html', title='Home', isAuth=isAuth)

# about route for the app
@app.route('/about')
def about():
    isAuth = current_user.is_authenticated
    return render_template('About.html', title='About', isAuth=isAuth)

# contact route for the app
@app.route('/contact')
def contact():
    isAuth = current_user.is_authenticated
    return render_template('contact.html', title='Contact', isAuth=isAuth)

#Account route for the app
@app.route('/account')
@login_required
def account():
    isAuth = current_user.is_authenticated
    return render_template('Account.html', title='Account',isAuth=isAuth)
    
# Register the routes in the app
@app.route('/register', methods=['GET', 'POST'])
def register():
    isAuth = current_user.is_authenticated
    print(isAuth)
    # if user already login
    if current_user.is_authenticated:
        flash(
            f'Your Are Alredey Login: {current_user.username}', category='info',)
        return redirect(url_for('account'))
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
    return render_template('register.html', title='Register', form=form, isAuth=isAuth)
# Login the routes in the app
@app.route('/login', methods=['GET', 'POST'])
def login():
    # if user already login
    if current_user.is_authenticated:
        flash(f'Your Are Alredey Login: {current_user.username}', category='info',)
        return redirect(url_for('account'))
    form = LoginForm()
    if form.validate_on_submit():
        
        # if the user is in the database 
        user = User.query.filter_by(email=form.email.data).first()
        # now check if the user and password is in the database
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # impliment the login user
            login_user(user)
            flash(f'Login sucssess {form.email.data}', category='success',)
            return redirect('account')
        else:
            flash(f'Login unsucssess {form.email.data}', category='danger')
            return redirect('register')
    return render_template('Login.html', title='Login',form=form)


@app.route('/resetpassword',methods=['GET', 'POST'])
def resetpassword():
    if current_user.is_authenticated:
        flash( f'Your Are Alredey Login: {current_user.username}', category='info',)
    form = ReserPasswordForm()
    # if form.validate_on_submit():
    if form.validate_on_submit():
        email = User.query.filter_by(email=form.email.data).first()
        # if email is in the database
        if email:
            form1 = ResetPasswordForm()
            flash(f'Send Password Reset Token Code On Your {form.email.data} address', category='success')
            # call a function to send the email
            return render_template(template_name_or_list='submitetoken.html',form=form1)
        else:
            flash(message=f'Email {form.email.data} is not in the database', category='danger')
            return redirect('register')
    return render_template('resetpassword.html', title='Resetpassword', form=form)

@app.route('/submitetoken',methods=['GET', 'POST'])
def submitetoken():
    if form.validate_on_submit():
        print('hello');
    return;


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
