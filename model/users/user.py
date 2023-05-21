import datetime as dt

from marshmallow import Schema, fields

class UserSignUp(object):
    def __init__(self, name, email, pwd, token):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.token = token
        self.created_at = str(dt.datetime.now())

class UserLogIn(object):
    def __init__(self, email, pwd):
        self.email = email
        self.pwd = pwd

class UserCollection(object):
    def __init__(self, _id, name, email, pwd, token, created_at):
        self._id = _id
        self.name = name
        self.email = email
        self.pwd = pwd
        self.token = token
        self.created_at = created_at

class UserSchema(Schema):
    _id = fields.Str()
    email = fields.Str()
    pwd = fields.Str()
    token = fields.Str()
    created_at = fields.Str()