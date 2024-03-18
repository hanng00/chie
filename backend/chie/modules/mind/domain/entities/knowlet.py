from datetime import datetime
from pydantic import BaseModel

from chie.modules.mind.domain.entities.question import Question


class Knowlet(BaseModel):
    """Small learning items that populate the user's feed."""

    title: str
    content: str
    question: Question
    created_at: datetime
