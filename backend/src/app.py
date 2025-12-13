import logging

from api.v1.routes.articles import router as article_router
from api.v1.routes.auth import router as auth_router
from api.v1.routes.health import router as health_router
from api.v1.routes.search import router as search_router
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


app = FastAPI(
    title="WikiKeep",
    summary="""
        A FastApi based wikipedia bookmark application
    """,
    version="v1",
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
app.include_router(search_router, prefix="/api/v1", tags=["Search"])
app.include_router(article_router, prefix="/api/v1", tags=["Articles"])
