from pydantic import BaseModel
from datetime import datetime

class SmartContractCreate(BaseModel):
    type: str
    metadata: dict

class SmartContractResponse(BaseModel):
    contract_hash: str
    type: str
    status: str
    metadata: dict
    created_at: datetime
