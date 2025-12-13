from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt

from helpers.app_settings import AppSettings


class PasswordHelper:

    @staticmethod
    def hash_password(password: str) -> str:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_bytes, salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    @staticmethod
    def create_access_token(subject: str) -> str:
        payload = {
            "sub": subject,
            "iat": datetime.now(timezone.utc),
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=int(AppSettings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
        }
        return jwt.encode(
            claims=payload,
            key=AppSettings.JWT_SECRET_KEY,
            algorithm=AppSettings.JWT_ALGORITHM,
        )
