import logging

from business.article_business import ArticleBusiness
from helpers.common_log import CommonLog

article_business = ArticleBusiness()
logger = logging.getLogger(__name__)


async def get_articles_controller(user_email: str):
    return await article_business.get_articles_by_email(user_email)


async def save_articles_controller(user_email: str, payload, background_tasks):
    await article_business.save_article(user_email, payload)

    title = payload.get("title")
    summary = payload.get("summary")

    tags = await article_business.generate_tags(title, summary)
    logger.info(CommonLog.AI_GENERATED_TAGS.format(tags=tags))

    if tags:
        background_tasks.add_task(
            article_business.update_tags, user_email, payload.get("page_id"), tags
        )

    return {"message": CommonLog.ARTICLE_SAVED_SUCCESSFULLY}


async def update_article_tags_controller(email: str, page_id: int, tags: list[str]):
    await article_business.update_tags(email, page_id, tags)
    return {"message": CommonLog.TAGS_UPDATED_SUCCESSFULLY}
