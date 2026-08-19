from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from jwt.exceptions import InvalidTokenError
from models.auth import TokenData
from models.user import User
from pwdlib import PasswordHash

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "afbf8e8c498a091441ed002a0435a16c069b0aec2049e4a518d045f51ee82f85"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

ADMIN_USERNAME = "admin-v01"
ADMIN_EMAIL = "admin.v01@example.com"
ADMIN_FULL_NAME = "Administrator V01"
ADMIN_PASSWORD = "dumbpassword"

password_hash = PasswordHash.recommended()

admin_user = User(
    username=ADMIN_USERNAME,
    email=ADMIN_EMAIL,
    full_name=ADMIN_FULL_NAME,
    hashed_password=password_hash.hash(ADMIN_PASSWORD),
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


def verify_password(input_password: str, hashed_password: str) -> bool:
    return password_hash.verify(input_password, hashed_password)


def authenticate_user(username: str, password: str) -> User | None:
    if username != ADMIN_USERNAME:
        return None

    if not verify_password(password, admin_user.hashed_password):
        return None

    return admin_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate user credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise credentials_exception

        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception

    user = admin_user.model_copy()
    if user is None:
        raise credentials_exception

    return user
