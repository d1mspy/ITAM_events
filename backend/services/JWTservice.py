from fastapi import status, HTTPException
from jwt import decode, encode 
from jwt.exceptions import InvalidTokenError
from config.config import JWT_SECRET

async def check_access_token(authorization_header: str) -> dict:
    if authorization_header is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="пользователь не авторизован")

    elif 'Bearer ' not in authorization_header:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="некорректный authorization header")
    
    token = encode(payload={"header": str(authorization_header.replace('Bearer ', '')).strip()}, key=JWT_SECRET, algorithm="HS256")
    
    try:
        payload = decode(jwt=token, key=JWT_SECRET, algorithms=["HS256"])
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="токен не валиден")

    data = {"id": payload.get("id"), "is_admin": payload.get("is_admin")}
    
    return data
