from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

USER_SERVICE_URL = "http://user_service:8004"
TRANSACTION_SERVICE_URL = "http://transaction_service:8003"
PRICE_SERVICE_URL = "http://price_service:8002"
@app.get("/users/{user_id}")
def get_user(user_id: int):
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())

@app.post("/transactions/")
def create_transaction(transaction_data: dict):
    response = requests.post(f"{TRANSACTION_SERVICE_URL}/transactions/", json=transaction_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.json())
    

    
