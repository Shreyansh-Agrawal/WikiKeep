from controllers.article_controller import (
    delete_saved_article_controller,
    get_articles_controller,
    save_articles_controller,
    update_article_tags_controller,
)
from fastapi import APIRouter, BackgroundTasks, Depends, status
from helpers.api_paths import ApiPaths
from helpers.auth_helper import AuthHelper
from models.article import Article
from models.tags import Tags

router = APIRouter()


@router.get(ApiPaths.ARTICLES)
async def get_user_articles(current_user_email=Depends(AuthHelper.get_jwt_claims)):
    return await get_articles_controller(current_user_email)


@router.post(ApiPaths.ARTICLES, status_code=status.HTTP_201_CREATED)
async def save_user_article(
    payload: Article,
    background_tasks: BackgroundTasks,
    current_user_email=Depends(AuthHelper.get_jwt_claims),
):
    return await save_articles_controller(
        current_user_email, payload.dict(), background_tasks
    )


@router.patch(ApiPaths.ARTICLE_TAGS, status_code=status.HTTP_200_OK)
async def update_article_tags(
    page_id: int, payload: Tags, current_user_email=Depends(AuthHelper.get_jwt_claims)
):
    return await update_article_tags_controller(
        current_user_email, page_id, payload.tags
    )


@router.delete(ApiPaths.ARTICLE_BY_ID, status_code=status.HTTP_204_NO_CONTENT)
async def delete_saved_article(
    page_id: int, current_user_email=Depends(AuthHelper.get_jwt_claims)
):
    await delete_saved_article_controller(current_user_email, page_id)
    return None
