from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"

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

