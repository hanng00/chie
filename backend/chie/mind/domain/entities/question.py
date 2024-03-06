from pydantic import BaseModel
from datetime import datetime


class Question(BaseModel):
    """Question entity."""

    content: str
    created_at: datetime
