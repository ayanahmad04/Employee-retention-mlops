from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
# uri = "mongodb+srv://ayanahmadkhan1165_db_user:ayan123@cluster0.metp2qs.mongodb.net/Proj0?retryWrites=true&w=majority"
DATABASE_NAME = "Proj0"
COLLECTION_NAME = "Proj0-Data"
# MONGODB_URL_KEY = 'mongodb+srv://ayanahmadkhan1165_db_user:YSGX2XKWKj1MFsvt@cluster0.metp2qs.mongodb.net/Proj0?retryWrites=true&w=majority'

client = MongoClient(os.getenv('MONGODB_URL_KEY'))

print("Databases:", client.list_database_names())

db = client["Proj0"]
print("Collections:", db.list_collection_names())

collection = db["Proj0-Data"]

print("Total docs:", collection.count_documents({}))

doc = collection.find_one()
print("Sample document:", doc)

from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
client = MongoClient(os.getenv('MONGODB_URL_KEY'))
db = client["Proj0"]
collection = db["Proj0-Data"]
print(client)

