from src import db, login_manager, bcrypt, app
from datetime import datetime
from flask_login import UserMixin
from flask import redirect, url_for, flash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
# unathorized login handler
@login_manager.unauthorized_handler
def unauthorized():
    flash('You are not authorized to view that page', category='danger')
    return redirect(url_for('login'))


# To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations for all of these properties and methods. (It’s not required, though.)
# create User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(120), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    # return a string when we add a new user
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.date_created.strftime('%d-%m-%Y, %H:%M:%S')}')"
    # constructor
    # def __init__(self, username, password, email, image):
    #     self.username = username
    #     self.password = password
    #     self.email = email
    #     self.image = image
