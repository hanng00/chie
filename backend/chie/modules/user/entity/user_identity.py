from typing import Optional
from uuid import UUID

from pydantic import BaseModel, validator


class UserIdentity(BaseModel):
    id: UUID
    email: Optional[str] = None

    @validator("id")
    def validate_id(cls, value):
        if isinstance(value, str):
            return UUID(value)
        return value
