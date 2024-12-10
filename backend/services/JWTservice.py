from fastapi import Request, Security, status, HTTPException
from fastapi.security import APIKeyHeader
from jwt import decode
from jwt.exceptions import InvalidTokenError
from config.config import JWT_SECRET
from pydantic import BaseModel

class TokenValidationResult(BaseModel):
    is_valid: bool
    data: dict | None
    exception: Exception | None

async def check_access_token(authorization_header: str) -> dict:
    
    if authorization_header is None:
        exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="пользователь не авторизован")
        return TokenValidationResult(is_valid=False, exception=exc)
    
    elif 'Bearer ' not in authorization_header:
        exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="некорректный authorization header")
        return TokenValidationResult(is_valid=False, exception=exc)
    
    token = str(authorization_header)
    
    try:
        payload = decode(jwt=token, key=str(JWT_SECRET), algorithms=["HS256"])
    except InvalidTokenError:
        exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="токен не валиден")
        return TokenValidationResult(is_valid=False, exception=exc)
    
    return TokenValidationResult(is_valid=check_status, 
                                 data={"id": payload.get("id"), "is_admin": payload.get("is_admin")}, 
                                 exception=None)
