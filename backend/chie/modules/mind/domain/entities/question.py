from typing import Optional
from uuid import UUID
from pydantic import BaseModel, validator
from datetime import datetime


class Question(BaseModel):
    """Question entity."""

    id: int
    user_id: UUID
    content: str

    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator("user_id")
    def validate_uuids(cls, value):
        if value:
            return str(value)
        return value
