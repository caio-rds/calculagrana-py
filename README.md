# CalculaGrana

> ## Um simples aplicativo em Python/FastAPI para calcular o valor de conversões de moedas.

### Mais informações sobre a aplicação:

> - A aplicação foi desenvolvida em Python com o framework FastAPI.
> - Possui Autenticação JWT.
> - Utiliza o banco de dados SQLite.
> - Possui ORM com SQLAlchemy.
> - Utiliza o Pydantic para validação de dados.

### Como rodar a aplicação:

> - Clone o repositório.
> - Crie um ambiente virtual.
> - Instale as dependências com o comando `pip install -r requirements.txt`.
> - Rode a aplicação com o comando `uvicorn app.main:app --reload`.

### Rotas da aplicação (endereço padrão: `http://127.0.0.1:8000`):
> - `/v0/healthcheck - GET`: Retorna um JSON com a mensagem `{"health": "check"}`.

> - `/v0/user/ - POST`: Cria um usuário. Deve ser enviado um JSON com o seguinte formato:
> - `{"username": "string", "password": "string", "email": "string"}`.

> `/v0/user/username - GET`: Retorna um JSON com os dados do usuário com o username informado.

> - `/v0/user/username - PUT`: Ainda está sendo implementado.

> - `/v0/user/username - DELETE`: Ainda está sendo implementado.


> - `/v0/login - POST`: Retorna um token JWT. Deve ser enviado um JSON com o seguinte formato:
> - Multipart Form: `{"username": "string", "password": "string"}`.

> - `/v0/login - GET`: Retorna um JSON com os dados do usuário logado após receber token bearer.

> - `v0/conversion - POST`: Retorna um JSON com o valor da conversão. Deve ser enviado um JSON com o seguinte formato:
> - `{"from_currency": "string", "to_currency": "string", "amount": float}`.

### Futuros Updates
> - Rota para Atualizar ou Deletar um usuário.
> - Salvar novas informações do usuário, como número ou telefone e validar esses dados.
> - Salvar novas informações na conversão, como valor das moedas utilizadas na data da conversão.
> - Sistema para alterar senha do usuário.
> - Sistema para buscar conversão por ID.
> - Sistema para buscar conversão por data.
> - Sistema para buscar conversão por usuário.
> - Sistema para buscar conversão por moeda.
> - Sistema para ver quais moedas estão disponíveis para conversão.
> - Consulta de valor de moeda em tempo real ou em uma data específica.

## Ainda em desenvolvimento...
```