from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import CustomerResponse, CustomerUpdate, CustomerCreate
from typing import List
from crud import (
    insert_customer,
    get_customers,
    get_customer,
    delete_customer,
    update_customer,
)

router = APIRouter()

@router.get("/customers/", response_model=List[CustomerResponse])
def read_all_customers_route(db: Session = Depends(get_db)):
    customers = get_customers(db)
    return customers

@router.get("/customer/{customer_id}", response_model=CustomerResponse)
def read_customer_route(customer_id: int, db: Session = Depends(get_db)):
    db_customer = get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return db_customer

@router.post("/customer/", response_model=CustomerResponse)
def insert_customer_route(customer: CustomerCreate, db: Session = Depends(get_db)):
    return insert_customer(db=db, customer=customer)

@router.delete("/customer/{customer_id}", response_model=CustomerResponse)
def detele_customer_route(customer_id: int, db: Session = Depends(get_db)):
    db_customer = delete_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return db_customer

@router.put("/customer/{customer_id}", response_model=CustomerResponse)
def update_customer_route(
    customer_id: int, customer: CustomerUpdate, db: Session = Depends(get_db)
):
    db_customer = update_customer(db, customer_id=customer_id, customer=customer)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    return db_customer