import requests

USER_SERVICE_URL = "http://127.0.0.1:8004"  # Base URL du service utilisateur

def get_wallet_balance(user_id: int, currency: str):
    """Récupère le solde du portefeuille utilisateur pour une devise spécifique."""
    url = f"{USER_SERVICE_URL}/wallets/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            wallets = response.json()
            for wallet in wallets:
                if wallet["currency"] == currency:
                    return wallet["balance"]
            return None
        elif response.status_code == 404:
            raise ValueError(f"User {user_id} not found or has no wallets")
        else:
            raise ConnectionError(f"Failed to connect to User Service: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to User Service: {e}")

def update_wallet_balance(wallet_id: int, new_balance: float, user_id: int, currency: str):
    """Met à jour le solde d'un portefeuille utilisateur."""
    url = f"{USER_SERVICE_URL}/wallets/{wallet_id}"
    payload = {
        "user_id": user_id,
        "balance": new_balance,
        "currency": currency
    }
    try:
        print(f"Payload envoyé : {payload}")  # Journal pour débogage
        response = requests.put(url, json=payload)
        print(f"Réponse : {response.status_code}, {response.text}")  # Journal pour débogage
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError(f"Wallet with ID {wallet_id} not found")
        else:
            raise ConnectionError(f"Failed to update wallet: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Error updating wallet: {e}")


def validate_user(user_id: int):
    """Valider l'existence d'un utilisateur via l'API du service utilisateur."""
    url = f"{USER_SERVICE_URL}/users/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError(f"User with ID {user_id} not found")
        else:
            raise ConnectionError(f"Failed to connect to User Service: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to User Service: {e}")
