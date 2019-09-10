from . import app
from flask_pymongo import PyMongo as pm

mongo = pm(app)