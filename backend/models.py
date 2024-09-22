from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

#Criação da tabela no banco e seus atributos
class CustomerModel(Base):
    __tablename__ = "Customers"  # esse será o nome da tabela

    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())