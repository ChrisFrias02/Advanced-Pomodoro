from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from dotenv import load_dotenv
import os
from flask_cors import CORS
from flask import render_template

from authAPI import UserRegistration, UserLogin
from taskAPI import TaskList
from timerAPI import FocusSessionList, FocusSessionStats, FocusSessionById


# Load .env file
load_dotenv()

app = Flask(__name__)
CORS(app)
# Config from env vars
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

# Init
db.init_app(app)
jwt = JWTManager(app)
api = Api(app)

# Register resources
api.add_resource(UserRegistration, '/api/register')
api.add_resource(UserLogin, '/api/login')
api.add_resource(TaskList, '/api/tasks')
api.add_resource(FocusSessionList, '/api/sessions')
api.add_resource(FocusSessionStats, '/api/sessions/stats')
api.add_resource(FocusSessionById, '/api/sessions/<int:session_id>')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/tasks')
def tasks_pahe():
    return render_template('tasks.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


