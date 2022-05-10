from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initializing application
app = Flask(__name__)

# Setting up configuration
# app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = 'c2b68daba34ee09a4cdea2f1d76be4e6'
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



from app import routes
# from .config import DevConfig

