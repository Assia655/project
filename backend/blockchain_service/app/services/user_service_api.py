import requests
from fastapi import HTTPException, Depends
from app.auth import oauth2_scheme  # Chemin vers votre implémentation OAuth2

USER_SERVICE_URL = "http://127.0.0.1:8004"  # URL du service utilisateur

def validate_user(token: str = Depends(oauth2_scheme)):
    """Valider l'utilisateur à l'aide de /users/me dans user_service."""
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users/me", headers=headers)
        response.raise_for_status()
        return response.json()  # Retourne les détails de l'utilisateur
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
