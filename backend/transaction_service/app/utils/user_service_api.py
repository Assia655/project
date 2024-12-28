import requests

USER_SERVICE_URL = "http://127.0.0.1:8000"  # Base URL du service utilisateur

def validate_user(user_id: int):
    """Valider l'existence d'un utilisateur via l'API du service utilisateur."""
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise ValueError(f"User with ID {user_id} not found")
    else:
        raise ConnectionError(f"Error connecting to User Service: {response.status_code}")

def get_user_wallet(user_id: int, currency: str):
    """Récupérer les informations du wallet d'un utilisateur pour une devise spécifique."""
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}/wallets?currency={currency}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise ValueError(f"No wallet found for user {user_id} with currency {currency}")
    else:
        raise ConnectionError(f"Error connecting to User Service: {response.status_code}")

def get_wallet_balance(user_id: int, currency: str):
    """Récupère le solde du portefeuille utilisateur."""
    url = f"{USER_SERVICE_URL}/users/{user_id}/wallets"
    response = requests.get(url)
    if response.status_code == 200:
        wallets = response.json()
        for wallet in wallets:
            if wallet["currency"] == currency:
                return wallet["balance"]
    return None

def update_wallet_balance(user_id: int, wallet_id: int, new_balance: float):
    """Met à jour le solde du portefeuille utilisateur."""
    url = f"{USER_SERVICE_URL}/users/{user_id}/wallets/{wallet_id}"
    payload = {"balance": new_balance}
    response = requests.put(url, json=payload)
    return response.status_code == 200
