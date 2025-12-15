from typing import List

from pydantic import BaseModel, Field


class Tags(BaseModel):
    tags: List[str] = Field(
        ...,
        min_items=1,
        max_items=10,
        description="List of tags for the article",
    )
