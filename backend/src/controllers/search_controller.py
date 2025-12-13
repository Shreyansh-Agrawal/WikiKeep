from business.article_search_business import search_wikipedia_articles


async def search_wikipedia(keyword: str, limit: int):
    return await search_wikipedia_articles(keyword, limit)
