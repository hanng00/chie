from pydantic import BaseModel


class QuestionDTO(BaseModel):
    """Question DTO."""

    question: str
