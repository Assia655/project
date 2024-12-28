from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.services.transaction import create_transaction

app = FastAPI(title="Transaction Service")

@app.post("/transactions", response_model=TransactionResponse)
def create_new_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    """
    Créer une transaction. Les prix sont récupérés dynamiquement depuis le price_service.
    """
    try:
        return create_transaction(db, transaction)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
