# Rotas da aplicação
## endereço padrão: `http://127.0.0.1:8000`

## `/v0/healthcheck - GET`

Retorna um JSON com a mensagem

```json 
{
  "status": "ok"
}
```

## `/v0/user - POST`

Retorna um JSON com os dados do usuário criado. Deve ser enviado um JSON com o seguinte formato:

```json
{
  "username": "string",
  "password": "string",
  "email": "string",
  "phone": "(xx) xxxxx-xxxx",
  "full_name": "Your Full Name Bro"
}
 ``` 

## `/v0/user - GET`

Retorna um JSON com os dados do usuário informado, caso receba o parametro 'conversions' com valor true, retornará um
array com as conversões do usuário.

```json
{
  "email": "seuemail@email.com",
  "username": "seu_username",
  "full_name": "Seu Nome Completo",
  "phone_number": "(xx) xxxxx-xxxx",
  "conversions": [
    {
      "username": "seu_username",
      "id": 1,
      "amount": 100.0,
      "conversion_id": "id_conversion",
      "base_currency": "USD",
      "conversions": {
        "BRL": {
          "amount": 513.45,
          "unit_value": 5.13
        },
        "EUR": {
          "amount": 91.82,
          "unit_value": 0.92
        }
      },
      "request_ip": "127.0.0.1",
      "request_date": "2024-05-16T02:39:13"
    }
  ]
}
```

## `/v0/user/username - PUT`

Atualizar dados do usuário. Deve ser enviado um JSON com os campos EMAIL, PHONE, FULL_NAME

> O único campo obrigatório é o username, os demais são opcionais, caso passados serão atualizados.

```json
{
  "username": "string",
  "email": "string",
  "phone": "(xx) xxxxx-xxxx",
  "full_name": "Your Full Name Bro"
}
```

E irá retornar

```json
{
  "email": "seuemail@email.com",
  "username": "seu_username",
  "full_name": "Seu Nome Completo",
  "phone_number": "(xx) xxxxx-xxxx",
  "conversions": "null"
}
```

## `/v0/user/username - DELETE`

Deleta o usuário informado e retorna um JSON com a mensagem

```json
{
  "status": "success",
  "message": "User seu_user deleted successfully"
}
```

## `/v0/login - POST`

Retorna um token JWT. Deve ser enviado um MultiPart Form com os campos USERNAME e PASSWORD.

```multipart form
  "username"="string",
  "password"="string"
```

retornará um JSON com

```json
{
  "token": "eaYJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6hertCVEWAGFHcCI6MTY0NzQwNzQwMn0.7"
}
```

## `/v0/login - GET`

Retorna um JSON com os dados do usuário logado após receber token bearer.

> Bearer Token: "EyeateTAEGNEABGJVNBJASVAEEATFGAEMKIGN"

retorno:

```json
{
  "username": "username"
}
```

## `/v0/conversion - POST`

body:

```json
{
  "from_currency": "BRL",
  "to_currency": [
    "BRL",
    "EUR",
    "USD"
  ],
  "amount": 100.50
}
```

response:

```json
{
  "base_currency": "BRL",
  "to_currency": [
    "BRL",
    "EUR",
    "USD"
  ],
  "amount": 100.0,
  "conversions": {
    "BRL": {
      "amount": 100.0,
      "unit_value": 1.0
    },
    "EUR": {
      "amount": 17.88,
      "unit_value": 0.18
    },
    "USD": {
      "amount": 19.48,
      "unit_value": 0.19
    }
  }
}
```

## `/v0/conversion/search/id: string - GET`

Retorna um JSON com os dados da conversão informada.

```json
{
  "username": "seu_username",
  "id": 1,
  "amount": 100.0,
  "conversion_id": "id_conversion",
  "base_currency": "USD",
  "conversions": {
    "BRL": {
      "amount": 513.45,
      "unit_value": 5.13
    },
    "EUR": {
      "amount": 91.82,
      "unit_value": 0.92
    }
  },
  "request_ip": "127.0.0.1",
  "request_date": "2024-05-16T02:39:13"
}
```

## `/v0/conversion/currencies - GET`

Caso tenha o parametro 'currencies' com os valores "EUR,USD,BRL" retornará um JSON com as cotações das moedas.

```json
{
  "BRL": {
    "name": "Brazilian Real",
    "name_plural": "Brazilian reals",
    "code": "BRL"
  },
  "EUR": {
    "name": "Euro",
    "name_plural": "Euros",
    "code": "EUR"
  },
  "USD": {
    "name": "US Dollar",
    "name_plural": "US dollars",
    "code": "USD"
  }
}
```
> Caso não tenha o parametro 'currencies' retornará um JSON com TODAS as moedas suportadas.