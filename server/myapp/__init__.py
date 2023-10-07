from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app = Flask(__name__)
app = Flask(
    __name__,
    static_url_path='',
    static_folder = '../client/dist',
    template_folder='../client/dist'
)
# app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/<int:id>')
def home(id=0):
    return render_template("index.html")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tour.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
migrate = Migrate(app, db)


