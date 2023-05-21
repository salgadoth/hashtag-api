from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from resources.routes import initialize_routes

app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
cors = CORS(app)
api = Api(app)
jwt = JWTManager(app)

initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)