from business.auth_business import AuthBusiness
from helpers.common_log import CommonLog

auth_business = AuthBusiness()


async def signup_controller(email: str, password: str):
    await auth_business.signup(email, password)
    return {"message": CommonLog.SIGNUP_SUCCESS}


async def login_controller(email: str, password: str):
    token = await auth_business.login(email, password)
    return {"token": token}
