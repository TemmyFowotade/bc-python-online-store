import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import config

app = Flask(__name__)
if os.getenv('HEROKU'):
    app.config.from_object(config['production'])
else:
    app.config.from_object(config['development'])
db = SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)

from app import views, models
