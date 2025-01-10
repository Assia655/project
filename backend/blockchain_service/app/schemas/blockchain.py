from pydantic import BaseModel

class RegisterUserRequest(BaseModel):
    user_address: str

class LinkWalletRequest(BaseModel):
    user_address: str
    wallet_address: str
