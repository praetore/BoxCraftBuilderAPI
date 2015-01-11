from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'darryl'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)
manager = APIManager(app, flask_sqlalchemy_db=db)

from app.models.models import Motherboard, Gpu, Cpu, Memory, Psu, Hdd, Case, Configuraties

models = [Motherboard, Gpu, Cpu, Memory, Psu, Hdd, Case]
for m in models:
    manager.create_api(m, methods=['GET', 'POST'])
manager.create_api(Configuraties, methods=['GET', 'POST', 'PUT', 'DELETE'])

db.create_all()
