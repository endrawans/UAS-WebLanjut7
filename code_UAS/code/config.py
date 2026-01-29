from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://pwl:pwl123@localhost:3306/db_flask_api?charset=utf8mb4&collation=utf8mb4_general_ci'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# JWT
app.config['JWT_SECRET_KEY'] = 'UAS_SECRET_KEY_2026'   # ganti kalau mau
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False  # token tidak expired (biar mudah testing)

db = SQLAlchemy(app)
jwt = JWTManager(app)

app.app_context().push()
