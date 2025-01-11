from fastapi import FastAPI, Depends, HTTPException,APIRouter
from sqlalchemy.orm import Session
from services import transaction
from models.transactions import Transaction
from db.session import get_db
import time 
import psycopg2
from schemas.announcement import AnnouncementCreate, AnnouncementResponse, AnnouncementUpdate
from schemas.transaction import TransactionCreate, TransactionResponse
from utils.price_service_api import get_price
from db.initdb import create_tables
from services.announcement import (
    create_announcement,
    get_active_announcements,
    update_announcement,
    delete_announcement,
)
from services.transaction import (
    create_transaction,
    get_all_transactions,
    get_transaction_by_id,
    get_transactions_by_user,
)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Autoriser toutes les origines pour les tests
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Méthodes HTTP autorisées
    allow_headers=["*"],  # En-têtes autorisés
)


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


@app.get("/transactions", response_model=list[TransactionResponse])  # Utiliser List pour une liste de réponses
async def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()  # Récupérer toutes les transactions
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found")
    return transactions  # FastAPI utilisera TransactionResponse pour chaque transaction

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def fetch_transaction_by_id(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return transaction  # FastAPI convertira automatiquement l'objet en un modèle TransactionResponse grâce à 'orm_mode'

# Endpoint pour récupérer les transactions d'un utilisateur
@app.get("/transactions_by/{seller_id}")
def get_transactions_for_user(seller_id: int, db: Session = Depends(get_db)):
    """Récupérer les transactions pour un utilisateur spécifique"""
    transactions = get_transactions_by_user(db, seller_id)  # Vous devez implémenter cette fonction dans les services
    if not transactions:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return transactions

@app.get("/transactions/by_user/{user_id}", response_model=TransactionResponse)
def get_transaction_by_user_id(user_id: int, db: Session = Depends(get_db)):
    """Récupérer une transaction basée sur l'ID de l'acheteur ou du vendeur"""
    transaction = db.query(Transaction).filter(
        (Transaction.buyer_id == user_id) | (Transaction.seller_id == user_id)
    ).first()  # Utilisez `first()` pour obtenir une seule transaction

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return transaction


# @app.get("/transactions/my")
# def get_my_transactions(user_id: int = Depends(get_user_id_from_token), db: Session = Depends(get_db)):
#     # Récupérer les transactions où l'utilisateur est soit buyer_id, soit seller_id
#     transactions = db.query(transaction).filter(
#         (Transaction.buyer_id == user_id) | (Transaction.seller_id == user_id)
#     ).all()
    
#     if not transactions:
#         raise HTTPException(status_code=404, detail="No transactions found")
    
#     return transactions
