from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

USER = os.environ.get("DB_USERNAME")
PWD = os.environ.get("DB_PASSWORD")
client = MongoClient('mongodb+srv://'+ USER +':'+ PWD +'@hashtag-cluster.xgytxwn.mongodb.net/?retryWrites=true&w=majority', server_api=ServerApi('1'))
db = client.api

try:
    client.admin.command('ping')
    print("🚀 Successfully connected to datasource!")
except Exception as e:
    print(e)