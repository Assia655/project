import requests

PRICE_SERVICE_URL = "http://127.0.0.1:8002"  # Adresse du service Price Service

def get_price(currency: str):
    """Récupère le prix actuel de la devise ou de l'actif depuis price_service."""
    # if currency != "MCO2":
    #     raise ValueError("Price service only supports MCO2 transactions")
    url = f"{PRICE_SERVICE_URL}/last_price/{currency}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["price"]
        else:
            raise ValueError(f"Failed to fetch price for {currency}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to Price Service: {e}")

