from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app  = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:adminadmin@flask.c9koygdtikwy.ap-south-1.rds.amazonaws.com:3306/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, default=False)