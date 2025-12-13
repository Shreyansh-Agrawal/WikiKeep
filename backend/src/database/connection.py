import asyncpg
from helpers.app_settings import AppSettings


async def get_connection():
    return await asyncpg.connect(AppSettings.DATABASE_URL)
