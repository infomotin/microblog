from flask import Flask
# from flask_migrate import Migrate
# import flask_login
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
# add secret key to the app
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# mysql connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager
login_manager = LoginManager(app)

# with app.app_context():
#     db.create_all()
#     db.session.commit()
# show all tables in the database
def show_tables():
    with app.app_context():
        # db.create_all()
        tables = db.engine.execute("SHOW TABLES;")
        for table in tables:
            print(table)
            return tables
        # db.session.commit()
        
# show all columns in a table in the database


show_tables()
# show all columns in a table



from src import routes

# baghorbari
# Kulsum123
# 161235150480
# Emp_job_card_comp_part1_all.rep
# Emp_job_card_comp_part2_all.rep
# EmpJobCardCmpFormatAll.rpt
# EmpCompJobCardAll.rpt
