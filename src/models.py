from src import db
from datetime import datetime

# create User model
class User(db.Model):
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
