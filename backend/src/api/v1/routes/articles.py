from controllers.article_controller import (
    get_articles_controller,
    save_articles_controller,
)
from fastapi import APIRouter, Depends, HTTPException, status
from helpers.api_paths import ApiPaths
from helpers.auth_helper import AuthHelper
from helpers.common_log import CommonLog
from models.article import Article

router = APIRouter()


@router.get(ApiPaths.ARTICLES_BY_EMAIL)
async def get_user_articles(
    email: str, current_user_email=Depends(AuthHelper.get_jwt_claims)
):
    if email != current_user_email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=CommonLog.ACCESS_DENIED
        )
    return await get_articles_controller(current_user_email)


@router.post(ApiPaths.ARTICLES, status_code=status.HTTP_201_CREATED)
async def save_user_article(
    payload: Article, current_user_email=Depends(AuthHelper.get_jwt_claims)
):
    return await save_articles_controller(current_user_email, payload.dict())
