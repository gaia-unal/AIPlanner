import os
import dotenv
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

dotenv.load_dotenv()

client = MongoClient(os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client[os.getenv('DB_NAME')]
collection = db[os.getenv('DB_COLLECTION')]

def save_user(user):
  user_data = get_user_email(user.get('email'))
  if not user_data:
    result = collection.insert_one(user)
    return str(result.inserted_id)
  else:
    return None

def get_user_email(email):
  return collection.find_one({'email': email})

def get_user_id(_id):
  return collection.find_one(ObjectId(_id))

def replace_user(_id, data):
  collection.replace_one({'_id': ObjectId(_id)}, data, False)
  