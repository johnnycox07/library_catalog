import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class ShowBook(BaseModel):
    """DTO для отображения книги в API ответах."""

    model_config = ConfigDict(from_attributes=True)

    book_id: uuid.UUID
    title: str
    author: str
    year: int
    genre: str
    pages: int
    available: bool
    isbn: str | None
    description: str | None
    extra: dict[str, Any] | None
    created_at: datetime
    updated_at: datetime