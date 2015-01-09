from flask.ext.mongoengine import MongoEngine
from flask.ext.restful import Api

__author__ = 'darryl'

from flask import Flask

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'DB': 'boxcraft'
    ''
}
app.debug = True
db = MongoEngine()
api = Api(app)