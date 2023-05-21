# hashtag-api
Practical Project designed and developed for job application. 

## Getting Started
For running locally:

```bash
pip install -r requirements.txt
# then
flask run
```
## Available endpoints:

* => JWT Token obtained from login endpoint required 

-> POST -> User Login
```bash
/api/auth/login
```
-> BODY:
```json
{
    "email" : "user email",
    "pwd" : "user password"
}
```

-> POST -> (*) -> User SignUp 
```bash
/api/auth/signup
```
-> BODY:
```json
{
    "name": "user name",
    "email": "user email",
    "pwd": "user password",
    "token": "user clearence token"
}
```

-> POST -> Webhook for recieving callbacks
```bash
/api/webhook
```
-> BODY:
```json
{
    "name" : "Client Name",
    "email" : "Client Email",
    "status" : "Status of payment (aprovado | reporvado | reembolsado)",
    "valor" : "Total payment value",
    "forma_pagamento" : "Payment type",
    "parcelas" : "Number of installments"
}
```

-> GET -> (*) -> Find all webhooks
```bash
/api/find-webhook
```

-> GET -> (*) -> Find specific webhook
```bash
/api/find-webhook?email=param
```