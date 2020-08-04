import os
from app import app
from dotenv import load_dotenv
from flask_pymongo import PyMongo
# MongoDB config
app.config["MONGO_DBNAME"] = os.environ.get('db')
app.config["MONGO_URI"] = os.environ.get('client', 'mongodb://localhost')

# Secret Key
app.secret_key = os.environ.get("SECRET", "randomstring")

# Constant Variables
admin_password = os.environ.get('admin_password')
admin_user = os.environ.get('admin_user')

MONGO = PyMongo(app)
DB_GAME_LIST = MONGO.db.game_list
DB_USERS = MONGO.db.users
DB_REVIEWS = MONGO.db.reviews