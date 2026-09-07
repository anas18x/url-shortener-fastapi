from datetime import datetime

from pydantic import BaseModel, HttpUrl


class CreateURLRequest(BaseModel):
    original_url: HttpUrl


class URLResponse(BaseModel):
    id: int
    original_url: HttpUrl
    short_code: str
    short_url: str
    created_at: datetime