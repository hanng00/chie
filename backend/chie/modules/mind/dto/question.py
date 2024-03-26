from pydantic import BaseModel, validator
from uuid import UUID


class CreateQuestionProperties(BaseModel):
    user_id: UUID
    content: str

    @validator("user_id")
    def validate_uuids(cls, value):
        if value:
            return str(value)
        return value

class CreateKnowletProperties(BaseModel):
    title: str
    content: str