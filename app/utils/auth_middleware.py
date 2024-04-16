from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Depends
from jwt import PyJWTError

from app.utils.constants import SECRET_KEY, ALGORITHM

from fastapi.security import OAuth2PasswordBearer

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth")


def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encode_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        staff_id = payload.get("id")
        role = payload.get("role")
        if staff_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"id": staff_id, "role": role}
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_staff(token: str = Depends(oauth2_schema)):
    staff = decode_access_token(token)
    if not staff:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"id": staff["id"], "role": staff["role"]}
