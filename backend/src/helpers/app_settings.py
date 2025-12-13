import os


class AppSettings:
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES")
    DATABASE_URL = os.getenv("DATABASE_URL")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


class LlmModels:
    GEMINI_PRO = "gemini-3-pro-preview"
