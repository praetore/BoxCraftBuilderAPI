from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'darryl'

app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.environ['OPENSHIFT_POSTGRESQL_DB_URL']
except KeyError:
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

from app.models.models import Motherboard, Gpu, Cpu, Memory, Psu, Hdd, Case, Configs

models = [Motherboard, Gpu, Cpu, Memory, Psu, Hdd, Case]
for m in models:
    manager.create_api(m, methods=['GET', 'POST'])
manager.create_api(Configs, methods=['GET', 'POST', 'PUT', 'DELETE'])

db.create_all()