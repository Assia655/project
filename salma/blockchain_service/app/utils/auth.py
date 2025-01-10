from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

# Configuration JWT (doit correspondre à celle de user_service)
SECRET_KEY = "b779b4c3ad2446f1b93c1e37dd1d8e3a49bc345635234d2a9ec5f95bcd2f6d19" 
ALGORITHM = "HS256"

# OAuth2 schema pour récupérer le token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8004/token")

def verify_access_token(token: str):
    """Vérifier et décoder un token JWT."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Retourne les données du token
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """Récupérer l'utilisateur courant à partir du token."""
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    return payload  # Retourne les détails utilisateur (ex. username, exp)
