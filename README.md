<div align="center">
  <h1>Criação de um Sistema CRUD</h1>
</div>
<div align="center">
    <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" target="_blank"></a>
    <a href="https://www.postgresql.org/docs/" target="_blank"><img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white" target="_blank"></a>
    <a href="https://fastapi.tiangolo.com/" target="_blank"><img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" target="_blank"></a>
    <a href="https://streamlit.io/" target="_blank"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" target="_blank"></a>
    <a href="https://www.sqlalchemy.org/" target="_blank"><img src="https://img.shields.io/badge/SQLAlchemy-323232?style=for-the-badge&logo=sqlalchemy&logoColor=white" target="_blank"></a>
    <a href="https://pydantic-docs.helpmanual.io/" target="_blank"><img src="https://img.shields.io/badge/Pydantic-3776AB?style=for-the-badge&logo=pydantic&logoColor=white" target="_blank"></a>
    <a href="https://docs.docker.com/" target="_blank"><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" target="_blank"></a>
</div>

## Visão Geral

Este projeto visa desenvolver uma aplicação CRUD (Create, Read, Update, Delete) utilizando tecnologias modernas e eficientes. O backend será construído com FastAPI, um framework de alta performance para criação de APIs. Para a interação com o banco de dados PostgreSQL, utilizaremos SQLAlchemy, enquanto Pydantic será responsável pela validação dos dados.

A interface web será desenvolvida com Streamlit, que facilita a criação de dashboards e aplicações web interativas. Além disso, a aplicação será containerizada com Docker, garantindo um ambiente de desenvolvimento consistente e simplificando a implantação em diferentes ambientes.

### Versão do Python
    3.12.1

### Bibliotecas principais

    - Backend:
        • email_validator
        • fastapi
        • pandas
        • psycopg2-binary
        • pyarrow
        • pydantic
        • python-dotenv
        • SQLAlchemy
        • uvicorn

    - Frontend: 
        • streamlit
        • requests
        • streamlit-option-menu
        • python-dotenv

## Estrutura do projeto

O projeto está divido em duas pastas principais: **backend** e **frontend**. Além delas, existem arquivos de configurações gerais do projeto.

Segue detalhamento:  

- **backend** - contêm os arquivos referentes ao módulo backend.

  
  - **Dockerfile**: contém as  configurações para criação de uma imagem identica ao código original do módulo **backend**.
  - **requirements.txt**: lista todas as dependências de bibliotecas necessárias para a execução do módulo **backend**.
  - **crud.py**: contêm as regras de negócio e o código das funções crud do projeto.
  - **database**: utiliza o SQLAlchemy para criar e definir as configurações do banco de dados.
  - **models**: Define as classes que representam as tabelas do banco de dados.
  - **schemas.py**:  Define a estrutura dos dados que serão validados e serializados. Utilizado para garantir que os dados recebidos e enviados pela API estejam no formato correto
  - **routes**: Define as rotas da API, ou seja, define as funções que respondem às requisições HTTP.
  - **main.py**: arquivo principal do módulo **backend**, utilizado pelo Dockerfile para configurar e iniciar uma aplicação web utilizando toda a estrutura criada nos arquivos descritos acima.
  - **EXEMPLO.env**: EXEMPLO de arquivo de configuração de variáveis de ambiente. É necessário preencher as variáveis com as suas credenciais do banco de dados. Após isto, o arquivo deverá ser renomeado para **.env"".

- **backend** - contêm os arquivos referentes ao módulo backend.

  - **Dockerfile**: contém as  configurações para criação de uma imagem identica ao código original do módulo **frontend**.
  - **requirements.txt**: lista todas as dependências de bibliotecas necessárias para a execução do módulo **frontend**.
  - **app.py**: arquivo que define a página principal do módulo **frontend**, utilizado pelo Dockerfile para configurar e iniciar uma aplicação web via **Streamlit**.
  - **atualizar**: define os componentes do formulário de atualização de dados do cliente.
  - **consultar**: define os componentes do formulário de consulta de dados do cliente.
  - **deletar**: define os componentes do formulário de deleção de dados do cliente.
  - **inserir**: define os componentes do formulário de inclusão de dados do cliente.
  - **EXEMPLO.env**: EXEMPLO de arquivo de configuração de variáveis de ambiente. É necessário preencher a variável com o endereço web gerado pelo backend(normalmente o endereço local é http://backend:8000/). Após isto, o arquivo deverá ser renomeado para **.env"".

- **README.md**: Documentação do projeto.
- **docker-compose.yml**: O arquivo docker-compose.yml é utilizado para definir e gerenciar aplicações que utilizam múltiplos contêineres Docker. Ele permite que você configure todos os serviços necessários para a sua aplicação em um único arquivo YAML. Este arquivo simplifica a orquestração de múltiplos contêineres, garantindo que todos os componentes da sua aplicação sejam configurados e executados de maneira consistente.
- **.python-version**: arquivo que especifica a versão do Python usada no projeto.

## Passo a passo de instalação

### 0. Pré-requisito

Para executar a aplicação, é necessário ter o Docker Desktop instalado em seu computador.
Caso não tenha, baixe o docker em seu [site oficial] (https://www.docker.com/). Após baixá-lo, siga o passo a passo de sua instalação: [Como instalar o Docker Desktop](https://docs.docker.com/desktop/).
O Docker será o responsável por iniciar uma instância do banco de dados PostgreSQL, não sendo necessário a instalação dele localmente. Além disso, será responsável por criar containers para executar o Backend e Frontend da aplicação.

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

## Contatos

Para perguntas, sugestões ou feedbacks:

<div>
    <a href="www.linkedin.com/in/guilherme-limas-rj" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href="mailto:guilherme.lima@ymail.com"><img src="https://img.shields.io/badge/-Yahoo%20Mail!-%237E1FFF?style=for-the-badge&logo=yahoo&logoColor=white" target="_blank"></a>
</div> 