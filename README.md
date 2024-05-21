# CalculaGrana

## Uma aplicação para calcular o valor de conversões de moedas.
> Aplicação RESTFUL usando <b>Python/FastAPI</b>, <b>MySQL/SQLAlchemy</b> e <b>JWT</b>.

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

### Variáveis de Ambiente
> - Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```.env
URI_DB=mysql://root:my-secret-pw@localhost:3306/CalculaGrana
SECRET=SuaSecret
SENDGRID_KEY=SuaKey
FREECURRENCY_KEY=SuaKey
TEMPLATE_ID=SuaTemplate
``` 

### Serviços Externos
> - Para as conversão de moedas, foi utilizado a <a href="https://app.freecurrencyapi.com">Free Currency API</a>.
> - Para enviar os emails foi usado a <a href="https://app.sendgrid.com">SendGrid</a>.
> - Recomendo se cadastrar e criar suas próprias Keys, todos os serviços são gratuitos.

### Funcionalidades
> - Cadastro de Usuários com validação de Email, Telefone e Nome Completo.
> - Login de Usuários.
> - Autenticação de Usuários via JWT.
> - Conversão de moedas podem ser feitas logadas (gera histórico) ou anonimamente.
> - Consulta de conversões com base no ID.
> - Consulta possíveis moedas para conversão.
> - Recuperação de senha via código ou via semelhança.
> - Envio de email para recuperação de senha com o código.

### Futuros Updates
> - Adicionar testes unitários.
> - Adicionar testes de integração.
> - Adicionar Novos templates para o envio de emails.
> - tratar erros e aproximação de inputerror das moedas.