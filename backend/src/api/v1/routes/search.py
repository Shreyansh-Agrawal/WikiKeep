from controllers.search_controller import search_wikipedia
from fastapi import APIRouter, Depends, Query
from helpers.api_paths import ApiPaths
from helpers.auth_helper import AuthHelper

router = APIRouter()


@router.get(ApiPaths.SEARCH)
async def search_articles(
    search_keyword: str = Query(..., min_length=1, description="Search Keyword"),
    limit: int = Query(default=5, ge=1, le=10, description="Number of results"),
    current_user_email=Depends(AuthHelper.get_jwt_claims),
):
    return await search_wikipedia(search_keyword, limit)
