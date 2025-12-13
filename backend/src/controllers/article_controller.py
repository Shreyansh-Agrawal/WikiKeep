from business.article_business import ArticleBusiness
from helpers.common_log import CommonLog

article_business = ArticleBusiness()


async def get_articles_controller(user_email: str):
    return await article_business.get_articles_by_email(user_email)


async def save_articles_controller(user_email: str, payload, background_tasks):
    await article_business.save_article(user_email, payload)

    background_tasks.add_task(
        article_business.update_tags,
        user_email,
        payload.get("page_id"),
        payload.get("title"),
        payload.get("summary"),
    )

    return {"message": CommonLog.ARTICLE_SAVED_SUCCESSFULLY}
