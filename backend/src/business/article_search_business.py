import logging
from urllib.parse import quote

import httpx
from helpers.common_log import CommonLog

WIKI_SEARCH_URL = "https://en.wikipedia.org/w/api.php"
WIKI_SUMMARY_URL = "https://en.wikipedia.org/api/rest_v1/page/summary"

HEADERS = {
    "User-Agent": "WikiKeep/1.0 (https://github.com/Shreyansh-Agrawal/WikiKeep)",
    "Accept": "application/json",
}

logger = logging.getLogger(__name__)


async def search_wikipedia_articles(keyword: str, limit: int):

    logger.info(CommonLog.SEARCH_REQUEST.format(keyword=keyword))

    async with httpx.AsyncClient(headers=HEADERS, timeout=10) as client:
        search_params = {
            "action": "query",
            "list": "search",
            "srsearch": keyword,
            "srlimit": limit,
            "utf8": 1,
            "format": "json",
        }

        search_response = await client.get(WIKI_SEARCH_URL, params=search_params)
        search_response.raise_for_status()
        search_data = search_response.json()

        results = []

        for item in search_data.get("query", {}).get("search", []):
            title = item["title"]
            pageid = item["pageid"]

            encoded_title = quote(title.replace(" ", "_"))
            summary_response = await client.get(f"{WIKI_SUMMARY_URL}/{encoded_title}")

            if summary_response.status_code != 200:
                continue

            summary_data = summary_response.json()

            results.append(
                {
                    "pageid": pageid,
                    "title": title,
                    "summary": summary_data.get("extract"),
                    "url": summary_data.get("content_urls", {})
                    .get("desktop", {})
                    .get("page"),
                }
            )

        return results
