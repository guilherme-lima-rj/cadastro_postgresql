<div align="center">
  <h1>Criação de um Sistema CRUD</h1>
  <h3>Python | PostgreSQL | FastAPI | SQLAlchemy | Pydantic | Streamlit | Docker</h3>
</div>

## Visão Geral

Este projeto tem como objetivo criar uma aplicação CRUD (create, read, update and delete) utilizando FastAPI para o backend, SQLAlchemy para a interação com o banco de dados PostgreSQL, Pydantic para validação de dados, Streamlit para a interface web e Docker para containerização. FastAPI é um framework moderno e de alta performance para construção de APIs, enquanto Streamlit facilita a criação de dashboards e aplicações web interativas. Docker garante que o ambiente de desenvolvimento seja consistente e facilita a implantação em diferentes ambientes.

## Passo a passo de instalação

### 0. Pré-requisito

Para executar a aplicaçãp, é necessário ter o Docker Desktop instalado em seu computador.
Caso não tenha, baixe o docker em seu site oficial [Docker](https://www.docker.com/). Após baixá-lo, siga o passo a passo de sua instalação: [Como instalar o Docker Desktop](https://docs.docker.com/desktop/).
O Docker será o responsável por iniciar uma instancia do banco de dados PostgreSQL, não sendo necessário a instalação dele localmente. Além isso, será responsável por criar containers para executar o Backend e Frontend da aplicação.

### 1. Clonar o repositório

Para clonar o repositório, execute o seguinte comando no terminal:

```bash
git clone https://github.com/guilherme-lima-rj/cadastro_postgresql.git
```
### 2. Navegar até o diretório do projeto

Entre no diretório do projeto:

```bash
cd cadastro_postgresql
```
### 3. Defina suas variáveis de ambiente

Visando aumentar a **segurança** e a **modularidade** do projeto, cada módulo da aplicação terá seu próprio arquivo de variáveis de ambiente. Isto facilita a manutenção e a atualização de variáveis específicas para cada parte do projeto.

Entre na pasta **Backend** e edite o arquivo "example.env" com suas credenciais do banco de dados PostgreSQL e renomeie para ".env".

Entre na pasta **Frontend** e edite o arquivo "example.env" com o endereço local utilizado pelo **uvicorn** (normalmente o endereço local é http://backend:8000/), e renomeie para ".env".

### 4. Subir o ambiente com Docker Compose

Após instalar as dependências, você pode subir o ambiente com Docker Compose. Execute o seguinte comando:

```bash
docker compose up
```
Isso iniciará os contêineres Docker definidos no arquivo docker-compose.yml.

### 5. Verificar se os contêineres estão rodando
Para verificar se os contêineres estão rodando corretamente, execute:

```bash
docker ps
```

### 6. Acessar a aplicação
Após subir os contêineres, você pode acessar a aplicação no seu navegador. A aplicação estará disponível em http://localhost:8000 para o backend FastAPI e em http://localhost:8501 para a interface Streamlit.

## Ferramentas e Tecnologias

- **Python**: Linguagem de programação principal.
- **FastAPI**: Framework moderno e de alta performance para construção de APIs.
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para gerenciamento do banco de dados.
- **Pydantic**: Biblioteca para validação de dados.
- **PostgreSQL**: Banco de dados relacional robusto e escalável.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **Streamlit**: Biblioteca para criação de interfaces web interativas.
- **Docker**: Plataforma de containerização para criar, implantar e rodar aplicações em containers.