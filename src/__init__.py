from flask import Flask
# from flask_migrate import Migrate
# import dataclasses as dc
from flask_sqlalchemy import SQLAlchemy
database_obj = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'faequ227$_M'
# sql alchemy database configuration with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/site.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False;
db = database_obj.init_app(app)
from src import routes


 