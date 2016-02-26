import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

app = Flask(__name__)

"""Tests if app is being deployed locally or on HEROKU"""
if os.getenv('HEROKU'):
    app.config.from_object(config['production'])
else:
    app.config.from_object(config['development'])
db = SQLAlchemy(app)

"""Initiates login manager from flask login"""
lm = LoginManager()
lm.init_app(app)

from app import views, models
