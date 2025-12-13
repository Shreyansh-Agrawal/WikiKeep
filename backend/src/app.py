from dotenv import load_dotenv

load_dotenv()

import logging

from api.v1.routes.articles import router as article_router
from api.v1.routes.auth import router as auth_router
from api.v1.routes.health import router as health_router
from api.v1.routes.search import router as search_router
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from helpers.common_log import CommonLog

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


app = FastAPI(
    title="WikiKeep",
    summary="""
        A FastApi based wikipedia bookmark application
    """,
    version="v1",
)


@app.exception_handler(Exception)
async def handle_interal_server_exception(request: Request, exc: Exception):
    logger.exception(
        CommonLog.UNEXPECTED_ERROR_FOR_ENDPOINT.format(
            method=request.method, path=request.url.path
        )
    )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": CommonLog.INTERNAL_SERVER_ERROR},
    )


app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(auth_router, prefix="/api/v1", tags=["Auth"])
app.include_router(search_router, prefix="/api/v1", tags=["Search"])
app.include_router(article_router, prefix="/api/v1", tags=["Articles"])
