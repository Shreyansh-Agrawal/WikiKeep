from typing import Optional

from pydantic import BaseModel


class Article(BaseModel):
    page_id: int
    title: str
    summary: Optional[str] = None
    url: Optional[str] = None
