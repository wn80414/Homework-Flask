import flask
import os
from flask_sqlalchemy import SQLAlchemy

# gives current directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))

mypage_obj = flask.Flask(__name__)
mypage_obj.config.from_mapping(
    SECRET_KEY = 'epic-key',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False)

db = SQLAlchemy(mypage_obj)
from mypage import routes, models
