from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'faequ227$_M'
from src import routes


 