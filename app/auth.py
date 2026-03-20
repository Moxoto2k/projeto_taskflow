from fastapi import Header, HTTPException

fake_tokens = {}

def create_token(username: str):
    token = f"token-{username}"
    fake_tokens[token] = username
    return token

def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token não enviado")

    token = authorization.replace("Bearer ", "")
    username = fake_tokens.get(token)

    if not username:
        raise HTTPException(status_code=401, detail="Token inválido")

    return username