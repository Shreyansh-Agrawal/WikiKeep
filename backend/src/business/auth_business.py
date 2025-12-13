import logging

from database.database_helper import DatabaseHelper
from fastapi import HTTPException, status
from helpers.auth_helper import AuthHelper
from helpers.common_log import CommonLog
from helpers.mask_data import mask_email
from helpers.queries import Queries

logger = logging.getLogger(__name__)


class AuthBusiness:

    def __init__(self):
        self.db_helper = DatabaseHelper()

    async def signup(self, email: str, password: str):
        logger.info(CommonLog.SIGNUP_REQUEST.format(email=mask_email(email)))

        user_id = await self.db_helper.read(
            query=Queries.GET_USER_ID_BY_EMAIL, params=(email,), fetch_one=True
        )

        if user_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail=CommonLog.USER_EXISTS
            )

        hashed_password = AuthHelper.hash_password(password)

        await self.db_helper.write(
            query=Queries.INSERT_USER, params=(email, hashed_password)
        )

    async def login(self, email: str, password: str):
        logger.info(CommonLog.LOGIN_REQUEST.format(email=mask_email(email)))

        user_credentials = await self.db_helper.read(
            query=Queries.GET_USER_PASSWORD_BY_EMAIL, params=(email,), fetch_one=True
        )

        if not user_credentials or not AuthHelper.verify_password(
            password, user_credentials.get("hashed_password")
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=CommonLog.INVALID_CREDENTIALS,
            )

        return AuthHelper.create_access_token(subject=email)
