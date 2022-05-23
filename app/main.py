import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.slack_sender import SlackSender


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import routes