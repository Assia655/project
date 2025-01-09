import requests
from fastapi import HTTPException

PRICE_SERVICE_URL = "http://127.0.0.1:8005" ''

def get_market_price(currency: str):
    """Récupérer le prix actuel d'un actif depuis le service de prix."""
    try:
        response = requests.get(f"{PRICE_SERVICE_URL}/prices/{currency}")
        response.raise_for_status()
        return response.json().get("price")
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch market price: {str(e)}")
