# CalculaGrana

## Uma aplicação para calcular o valor de conversões de moedas.

### Aplicação RESTFUL usando Python/FastAPI, MySQL/SQLAlchemy e JWT.

### Como rodar a aplicação:

> - Clone o repositório e Crie um ambiente
    virtual. <a href="https://www.alura.com.br/artigos/ambientes-virtuais-em-python">Como criar um ambiente
    virtual?</a>.
> - Instale as dependências com o comando `pip install -r requirements.txt`.
> - Rode a aplicação com o comando `uvicorn app.main:app --reload`.
> - Criar o banco de dados você pode instalar localmente o MySQL ou usar o Docker.
> - Para criar o banco de dados, rode o
    comando `docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag`.
> - Para instalar o MySQL localmente, siga o tutorial do site oficial do <a href="https://www.mysql.com/downloads/">
    MySQL</a>.


### Futuros Updates
> - Migrations
> - tratar erros e aproximação de inputerror das moedas.
> - Recovery Password with codes