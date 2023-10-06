from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)
app = Flask(
    __name__,
    static_url_path='',
    static_folder = '../client/build',
    template_folder='../client/build'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tour.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


