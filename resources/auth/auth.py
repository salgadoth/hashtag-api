import bcrypt
import datetime

from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt

from config.datasource.dbService import DataBaseService
from config import salt

from model.users.user import UserLogIn, UserSignUp, UserCollection

class LoginApi(Resource):

    def post(self):
        secret = DataBaseService().getSecret()
        
        user : UserLogIn = UserLogIn(**request.get_json())

        # user.pwd = bcrypt.hashpw(user.pwd, bcrypt.gensalt(10))
        
        result = DataBaseService().getUser(user.email)

        try:
            userDB = UserCollection(**result)

            user.pwd = user.pwd.encode('utf-8')
        
            userDB.pwd = userDB.pwd.encode('utf-8')

            if bcrypt.checkpw(user.pwd, userDB.pwd):
                expires = datetime.timedelta(hours=3)
                expiresAt = datetime.datetime.now() + expires
                if userDB.token == secret["value"]:
                    additional_claims = {"token": True,
                                        "email": user.email}
                    access_token = create_access_token(identity=str(userDB.name),
                                                    additional_claims= additional_claims,
                                                    expires_delta=expires)
                    return {"token": access_token,
                            "expires_at": str(expiresAt)}, 200
                else:
                    access_token = create_access_token(identity=str(user.name),
                                                    expires_delta=expires)
                    return {"token": access_token,
                            "expires_at": str(expiresAt)}, 200
            else:
                return {"error": "Credenciais incorretas."}, 400
        except TypeError:
            return {"error": "Credenciais incorretas."}, 400
        
class SignUpApi(Resource):
    @jwt_required()
    def post(self):
        user : UserSignUp = UserSignUp(**request.get_json())
        claims = get_jwt()
        count = DataBaseService().getCountUser(user.email)

        if count > 0:
            return {"error": "Usuário já cadastrado."}, 400
        else:
            if claims['token'] == True:
                user.pwd = user.pwd.encode('utf-8')
                user.pwd = bcrypt.hashpw(user.pwd, salt = salt)
                user.pwd = user.pwd.decode('utf-8', 'ignore')
            else:
                return {"error": "Não possui privilégios suficientes."}, 400
            try:
                DataBaseService().insertUser(user.__dict__)
            except Exception as e:
                print(e)
            
            return {"status": "Usuário cadastrado com sucesso."}, 200
            