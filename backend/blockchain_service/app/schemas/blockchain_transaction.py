from pydantic import BaseModel
from datetime import datetime

class BlockchainTransactionCreate(BaseModel):
    sender: str
    receiver: str
    amount: float
    currency: str

class BlockchainTransactionResponse(BaseModel):
    tx_hash: str
    sender: str
    receiver: str
    amount: float
    currency: str
    confirmations: int
    timestamp: datetime
