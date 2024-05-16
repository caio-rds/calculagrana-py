# CalculaGrana

> ## Um simples aplicativo em Python/FastAPI para calcular o valor de conversões de moedas.

### Mais informações sobre a aplicação:

> - A aplicação em Python/FastAPI.
> - DataBase Mysql e SQLAlchemy.

### Como rodar a aplicação:

> - Clone o repositório e Crie um ambiente virtual.
> - Instale as dependências com o comando `pip install -r requirements.txt`.
> - Rode a aplicação com o comando `uvicorn app.main:app --reload`.

### Rotas da aplicação (endereço padrão: `http://127.0.0.1:8000`):
> - `/v0/healthcheck - GET`: Retorna um JSON com a mensagem `{"health": "check"}`.

> - `/v0/user/ - POST`: Cria um usuário. Deve ser enviado um JSON com o seguinte formato:
> - `{"username": "string", "password": "string", "email": "string"}`.

> `/v0/user/username - GET`: Retorna um JSON com os dados do usuário com o username informado, caso receba o parametro
> 'conversions' com valor true, retornará um array com as conversões do usuário.

> - `/v0/user/username - PUT`: Ainda está sendo implementado.

> - `/v0/user/username - DELETE`: Ainda está sendo implementado.

> - `/v0/login - POST`: Retorna um token JWT. Deve ser enviado um JSON com o seguinte formato:
> - Multipart Form: `{"username": "string", "password": "string"}`.

> - `/v0/login - GET`: Retorna um JSON com os dados do usuário logado após receber token bearer.

> - `v0/conversion - POST`: Retorna um JSON com o valor da conversão. Deve ser enviado um JSON com o seguinte formato:
> - `{"from_currency": "string", "to_currency": "string", "amount": float}`.

### Futuros Updates
> - tratar erros e aproximação de inputerror das moedas.
> - Recovery Password with codes

## Ainda em desenvolvimento

> - Ainda em desenvolvimento, a aplicação está sendo feita para estudo e prática de Python/FastAPI.