from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_cors import CORS
app = Flask(__name__)
app = Flask(
    __name__,
    static_url_path='',
    static_folder = '../../client/dist',
    template_folder='../../client/dist'
)

# CORS(app)
# app = Flask(__name__, template_folder='templates')




app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tour_db_gt03_user:iAAL9QBpl0DlpEs8etGJwrnWcR7yL69Q@dpg-ckg307eafg7c73dhigq0-a.oregon-postgres.render.com/tour_db_gt03'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


