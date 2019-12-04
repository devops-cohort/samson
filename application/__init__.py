from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.228.138.102/solo-project'
app.config['SECRET_KEY:']

db = SQLAlchemy(app)

from application import routes
