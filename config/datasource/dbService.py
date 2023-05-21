from ..datasource import db
from model.users.user import UserCollection

class DataBaseService:
    def __init__(self):
        self.users = db.users
        self.config = db.config
        self.callbacks = db.callbacks
    
    def getSecret(self):
        try:
            return self.config.find_one({"name" : "secret"}, {'_id': False})
        except Exception as e:
            print(e)
    
    def getUser(self, email) -> UserCollection:
        try:
            return self.users.find_one({"email" : email})
        except Exception as e:
            print(e)
        
    def getCountUser(self, email):
        try:
            return self.users.count_documents({"email" : email})
        except Exception as e:
            print(e)
    
    def insertUser(self, user):
        try:
            return self.users.insert_one(user)
        except Exception as e:
            print(e)
    
    def insertCallback(self, callback):
        try:
            return self.callbacks.insert_one(callback)
        except Exception as e:
            print(e)
            
    def getCallbacks(self):
        try:
            return self.callbacks.find()
        except Exception as e:
            print(e)

    def getCallbacksFiltered(self, email = ''):
        try:
            return self.callbacks.find({"email" : str(email)})
        except Exception as e:
            print(e)