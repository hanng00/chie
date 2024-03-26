from enum import Enum
from typing import Optional
from pydantic import BaseModel


# ENUM
class ServiceEnum(str, Enum):
    riksdagen = "riksdagen"
    mind = "mind"


class QuestionInput(BaseModel):
    service: Optional[ServiceEnum] = ServiceEnum.riksdagen
    question: str
