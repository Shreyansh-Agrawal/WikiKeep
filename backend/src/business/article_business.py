import json
import logging

import asyncpg
from database.database_helper import DatabaseHelper
from fastapi import HTTPException, status
from helpers.app_settings import AppSettings, LlmModels
from helpers.common_log import CommonLog
from helpers.mask_data import mask_email
from helpers.prompts import Prompts
from helpers.queries import Queries
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

logger = logging.getLogger(__name__)


class ArticleBusiness:

    def __init__(self):
        self.db_helper = DatabaseHelper()
        self.llm = ChatGoogleGenerativeAI(
            model=LlmModels.GEMINI_PRO, google_api_key=AppSettings.GEMINI_API_KEY
        )

    async def get_articles_by_email(self, email: str):
        logger.info(CommonLog.GET_SAVED_ARTICLE_REQUEST.format(email=mask_email(email)))
        return await self.db_helper.read(Queries.GET_ARTICLE_BY_EMAIL, params=(email,))

    async def save_article(self, email: str, article: dict):
        logger.info(CommonLog.SAVE_ARTICLE_REQUEST.format(email=mask_email(email)))

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

    async def generate_tags(self, title: str, summary: str):
        prompt = PromptTemplate(
            input_variables=["title", "summary"],
            template=Prompts.GENERATE_CATEGORY_TAG_PROMPT,
        )
        try:
            response = await self.llm.ainvoke(
                prompt.format(title=title, summary=(summary or "")[:200])
            )
            tags = json.loads(response.content)
            return tags
        except Exception as error:
            logger.exception(CommonLog.FAILED_TO_GENERATE_TAGS.format(error=error))
            return []

    async def update_tags(self, email: str, page_id: int, tags: list[str]):
        try:
            await self.db_helper.write(
                Queries.UPDATE_ARTICLE_TAGS,
                params=(tags, email, page_id),
            )
        except Exception as error:
            logger.exception(
                CommonLog.UPDATE_TAG_FAILED.format(
                    email=mask_email(email), page_id=page_id, error=error
                )
            )

    async def delete_article(self, email: str, page_id: int):
        logger.info(
            CommonLog.DELETE_SAVED_ARTICLE_REQUEST.format(
                email=mask_email(email), page_id=page_id
            )
        )

        await self.db_helper.write(
            Queries.DELETE_ARTICLE_BY_EMAIL_AND_PAGE_ID, params=(email, page_id)
        )
