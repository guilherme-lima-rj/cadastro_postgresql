from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Carrega o arquivo .env usando um caminho relativo
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# Configurações da conexão
host_name = os.getenv('HOST_NAME')
database_name = os.getenv('DATABASE_NAME')
user_name = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')
service = os.getenv('SERVICE')

# Monta a url de conexão
SQLALCHEMY_DATABASE_URL = f"{service}://{user_name}:{password}@{host_name}/{database_name}"

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