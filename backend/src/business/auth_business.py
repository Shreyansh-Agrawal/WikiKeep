from database.database_helper import DatabaseHelper
from fastapi import HTTPException, status
from helpers.common_log import CommonLog
from helpers.password_helper import PasswordHelper
from helpers.queries import Queries


class AuthBusiness:

    def __init__(self):
        self.db_helper = DatabaseHelper()

    async def signup(self, email: str, password: str):
        user_id = await self.db_helper.read(
            query=Queries.GET_USER_ID_BY_EMAIL, params=(email,), fetch_one=True
        )

        if user_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=CommonLog.USER_EXISTS
            )

        hashed_password = PasswordHelper.hash_password(password)

        await self.db_helper.write(
            query=Queries.INSERT_USER, params=(email, hashed_password)
        )

    async def login(self, email: str, password: str):
        user_credentials = await self.db_helper.read(
            query=Queries.GET_USER_CREDENTIALS_BY_EMAIL, params=(email,), fetch_one=True
        )

        if not user_credentials or not PasswordHelper.verify_password(
            password, user_credentials.get("hashed_password")
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=CommonLog.INVALID_CREDENTIALS,
            )

        return PasswordHelper.create_access_token(subject=email)
