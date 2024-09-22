from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da conexão
host_name = os.getenv('HOST_NAME')
database_name = os.getenv('DATABASE_NAME')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
service = os.getenv('SERVICE')

SQLALCHEMY_DATABASE_URL = f"{service}://{user_name}:{password}@{host_name}/{database_name}"
#SQLALCHEMY_DATABASE_URL="postgresql://user123:xiasxTUgTYHJcX7zWsBmniWgr68UAg1F@dpg-cro1aeg8fa8c738m6sh0-a.oregon-postgres.render.com/database_glxz"
#engine = create_engine(POSTGRES_DATABASE_URL)


#SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

# Cria o motor do banco de dados, é o conecta com o banco
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Sessão de banco de dados, é quem vai executar as queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos declarativos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





        
# import sqlite3

# def criar_banco():
#     conexao = sqlite3.connect('clientes.db')
#     c = conexao.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS clientes (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     nome TEXT NOT NULL,
#                     sobrenome TEXT NOT NULL,
#                     email TEXT NOT NULL,
#                     telefone TEXT NOT NULL)''')
#     conexao.commit()
#     conexao.close()

