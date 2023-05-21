from .auth.auth import SignUpApi, LoginApi
from .callback.callback import CallbackReciever, GetCallback

def initialize_routes(api):
    api.add_resource(SignUpApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
    api.add_resource(CallbackReciever, '/api/webhook')
    api.add_resource(GetCallback, '/api/find-webhook')