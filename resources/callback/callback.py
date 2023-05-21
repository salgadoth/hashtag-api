import json
from bson import json_util
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse

from config.datasource.dbService import DataBaseService

from model.callback.callback import CallbackDocument, CallbackReq

class CallbackReciever(Resource):

    def post(self):
        callback : CallbackReq = CallbackReq(**request.get_json())
        print('---🔍---TRATATIVAS---🔎---')
        
        if(callback.status == 'aprovado'):
            response = {'status': 'Callback recebido.',
                'desc' : 'Cliente liberado acesso, mensagem enviada.'}
        elif(callback.status == 'reprovado'):
            response = {'status' : 'Callback recebido.',
                'desc' : 'Pagamento reprovado.'}
        elif(callback.status == 'reembolsado'):
            response =  {'status' : 'Callback recebido.',
                'desc' : 'Acesso ao curso revogado.'}
        else:
            response = {'status' : 'Callback recebido.',
                'desc' : 'Status incorreto.'}

        callback.tratativas = json.dumps(response)

        DataBaseService().insertCallback(callback.__dict__)
        
        return response, 200
    
class GetCallback(Resource):
    @jwt_required()
    def get(self):
        # callback : CallbackGet = CallbackGet(**request.get_json())
        args = request.args
        if args:
            result = DataBaseService().getCallbacksFiltered(args.get('email'))
        else:
            result = DataBaseService().getCallbacks()
        
        results = []

        for document in result:
            callback : CallbackDocument = CallbackDocument(**document)
            results.append(callback.__dict__)

        return json_util.dumps({'data' : results}), 200

