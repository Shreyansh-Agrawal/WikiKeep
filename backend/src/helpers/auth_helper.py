from datetime import datetime, timedelta, timezone

import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from helpers.app_settings import AppSettings
from helpers.common_log import CommonLog
from jose import ExpiredSignatureError, JWTError, jwt

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/api/v1/login")


class AuthHelper:

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

    @staticmethod
    def create_access_token(subject: str) -> str:
        payload = {
            "sub": subject,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=int(AppSettings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)),
        }
        return jwt.encode(
            claims=payload,
            key=AppSettings.JWT_SECRET_KEY,
            algorithm=AppSettings.JWT_ALGORITHM,
        )

    @staticmethod
    def get_jwt_claims(token: str = Depends(oauth2_bearer)):
        try:
            payload = jwt.decode(
                token,
                AppSettings.JWT_SECRET_KEY,
                algorithms=[AppSettings.JWT_ALGORITHM],
            )
            email = payload.get("sub")

            if not email:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=CommonLog.INVALID_TOKEN,
                )
            return email

        except (JWTError, ExpiredSignatureError):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=CommonLog.INVALID_TOKEN,
            )
