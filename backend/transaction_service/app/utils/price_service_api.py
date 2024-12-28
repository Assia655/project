import requests

PRICE_SERVICE_URL = "http://127.0.0.1:8003"  # Adresse du service Price Service

def get_price(currency: str) -> float:

    try:
        response = requests.get(f"{PRICE_SERVICE_URL}/prices/{currency}")
        response.raise_for_status()  # Vérifie les erreurs HTTP
        data = response.json()
        return data["price"]
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Failed to fetch price for {currency}: {e}")
