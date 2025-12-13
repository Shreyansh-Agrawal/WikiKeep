import logging

import asyncpg
from database.database_helper import DatabaseHelper
from fastapi import HTTPException, status
from helpers.common_log import CommonLog
from helpers.queries import Queries

logger = logging.getLogger(__name__)


class ArticleBusiness:

    def __init__(self):
        self.db_helper = DatabaseHelper()

    async def get_articles_by_email(self, email: str):
        return await self.db_helper.read(Queries.GET_ARTICLE_BY_EMAIL, params=(email,))

    async def save_article(self, email: str, article: dict):
        try:
            await self.db_helper.write(
                Queries.INSERT_ARTICLE_INFO,
                params=(
                    email,
                    article.get("page_id"),
                    article.get("title"),
                    article.get("summary"),
                    article.get("url"),
                ),
            )

        except asyncpg.exceptions.UniqueViolationError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=CommonLog.ARTICLE_ALREADY_SAVED,
            )

        except Exception as error:
            logger.error(CommonLog.UNEXPECTED_ERROR.format(error=error))
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=CommonLog.UNEXPECTED_ERROR.format(error=error),
            )
