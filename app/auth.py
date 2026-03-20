from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

fake_tokens = {}
security = HTTPBearer()

def create_token(username: str):
    token = f"token-{username}"
    fake_tokens[token] = username
    return token

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    username = fake_tokens.get(token)

    if not username:
        raise HTTPException(status_code=401, detail="Token inválido")

    return username