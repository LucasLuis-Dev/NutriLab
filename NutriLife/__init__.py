from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '0de9118af9affe95588770ed3438bea6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nutrilife.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


DATABASE = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)

from NutriLife import routes