from business.search_business import SearchBusiness

search_business = SearchBusiness()


async def search_wikipedia(keyword: str, limit: int):
    return await search_business.search_wikipedia_articles(keyword, limit)
