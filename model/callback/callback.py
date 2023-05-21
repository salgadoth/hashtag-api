import datetime as dt

class CallbackDocument:
    def __init__(self, _id, name, email, status, valor, forma_pagamento, parcelas, tratativas, recieved_at):
        self._id = _id
        self.name = name
        self.email = email
        self.status = status
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.parcelas = parcelas
        self.tratativas = tratativas
        self.recieved_at = str(recieved_at)
        
class CallbackGet:
    def __init__(self, email):
        self.email = email

class CallbackReq:
    def __init__(self, name, email, status, valor, forma_pagamento, parcelas, tratativas = '', recieved_at = dt.datetime.now()):
        self.name = name
        self.email = email
        self.status = status
        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.parcelas = parcelas
        self.tratativas = tratativas
        self.recieved_at = str(recieved_at)
