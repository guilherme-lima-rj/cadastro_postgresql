from sqlalchemy.orm import Session
from schemas import CustomerUpdate, CustomerCreate
from models import CustomerModel

def get_customers(db: Session):
    """
    funcao que retorna todos os registros.
    """
    return db.query(CustomerModel).all()

def get_customer(db: Session, customer_id: int):
    """
    funcao que recebe um id e retorna suas informações
    """ 
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()   

    if db_customer is None:
        return None
    
    return db_customer

def insert_customer(db: Session, customer:CustomerCreate):
    """
    funcao que grava as informações
    """
    db_customer = CustomerModel(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    """
    funcao que recebe um id e deleta o registro, caso encontrado
    """    
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

    if db_customer is None:
        return None

    db.delete(db_customer)
    db.commit()
    return db_customer    

def update_customer(db: Session, customer_id: int, customer: CustomerUpdate):
    """
    funcao que recebe um id e atualiza qualquer informação suas informações
    """    
    db_customer = db.query(CustomerModel).filter(CustomerModel.id == customer_id).first()

    if db_customer is None:
        return None

    if customer.name is not None:
        db_customer.name = customer.name    
    if customer.surname is not None:
        db_customer.surname = customer.surname
    if customer.email is not None:
        db_customer.email = customer.email
    if customer.phone is not None:
        db_customer.phone = customer.phone

    db.commit()
    return db_customer