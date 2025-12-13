from datetime import datetime, timedelta, timezone

from helpers.app_settings import AppSettings
from jose import jwt
from passlib.context import CryptContext

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordHelper:

    @staticmethod
    def hash_password(password: str):
        return PASSWORD_CONTEXT.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str):
        return PASSWORD_CONTEXT.verify(password, hashed_password)

    @staticmethod
    def create_access_token(subject: str):
        payload = {
            "sub": subject,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=AppSettings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
        }
        return jwt.encode(
            claims=payload,
            key=AppSettings.JWT_SECRET_KEY,
            algorithm=AppSettings.JWT_ALGORITHM,
        )
