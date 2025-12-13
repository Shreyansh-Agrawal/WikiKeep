from controllers.search_controller import search_wikipedia
from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/search")
async def search_articles(
    search_keyword: str = Query(..., min_length=1, description="Search Keyword"),
    limit: int = Query(default=5, ge=1, le=10, description="Number of results"),
):
    return await search_wikipedia(search_keyword, limit)
