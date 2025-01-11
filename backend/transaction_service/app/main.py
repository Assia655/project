from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import transaction
from app.models.transactions import Transaction
from app.db.session import get_db
import time 
import psycopg2
from app.schemas.announcement import AnnouncementCreate, AnnouncementResponse, AnnouncementUpdate
from app.schemas.transaction import TransactionCreate
from app.utils.price_service_api import get_price
from app.db.initdb import create_tables
from app.services.announcement import (
    create_announcement,
    get_active_announcements,
    update_announcement,
    delete_announcement,
)
from app.services.transaction import (
    create_transaction,
    get_all_transactions,
    get_transaction_by_id,
    get_transactions_by_user,
)

app = FastAPI()
@app.on_event("startup")
async def startup_event():
    create_tables()




@app.get("/health")
def health_check():
    return {"status": "healthy"}


# --- Announcements Endpoints ---
@app.post("/announcements")
def create_new_announcement( announcement_data: AnnouncementCreate, db: Session = Depends(get_db)):
    return create_announcement(db, announcement_data)

@app.get("/announcements")
def fetch_active_announcements(db: Session = Depends(get_db)):
    return get_active_announcements(db)

@app.put("/announcements/{announcement_id}")
def update_existing_announcement(announcement_id: int, update_data: AnnouncementUpdate, db: Session = Depends(get_db)):
    return update_announcement(db, announcement_id, update_data)

@app.delete("/announcements/{announcement_id}")
def delete_existing_announcement(announcement_id: int, db: Session = Depends(get_db)):
    return delete_announcement(db, announcement_id)



# --- Transactions Endpoints ---
@app.post("/transactions", response_model=dict)
def create_new_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, data)


@app.get("/transactions", response_model=list)
def fetch_all_transactions(db: Session = Depends(get_db)):
    return get_all_transactions(db)


@app.get("/transactions/{transaction_id}", response_model=dict)
def fetch_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

# Endpoint pour récupérer les transactions d'un utilisateur
@app.get("/transactions_by/{seller_id}")
def get_transactions_for_user(seller_id: int, db: Session = Depends(get_db)):
    """Récupérer les transactions pour un utilisateur spécifique"""
    transactions = get_transactions_by_user(db, seller_id)  # Vous devez implémenter cette fonction dans les services
    if not transactions:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return transactions


# @app.get("/transactions/my")
# def get_my_transactions(user_id: int = Depends(get_user_id_from_token), db: Session = Depends(get_db)):
#     # Récupérer les transactions où l'utilisateur est soit buyer_id, soit seller_id
#     transactions = db.query(transaction).filter(
#         (Transaction.buyer_id == user_id) | (Transaction.seller_id == user_id)
#     ).all()
    
#     if not transactions:
#         raise HTTPException(status_code=404, detail="No transactions found")
    
#     return transactions
