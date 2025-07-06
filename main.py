from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from models import db
from dotenv import load_dotenv
import os

from authAPI import UserRegistration, UserLogin
from taskAPI import TaskList


# Load .env file
load_dotenv()

app = Flask(__name__)

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


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


