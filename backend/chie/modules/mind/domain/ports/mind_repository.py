from typing import List, Protocol
from uuid import UUID

from chie.models.mind import Knowlet, Question
from chie.modules.mind.dto.question import (
    CreateKnowletProperties,
    CreateQuestionProperties,
)


class MindRepository(Protocol):
    ## Abstract Interface for interacting with a Mind Repository

    def insert_question(
        self, question_properties: CreateQuestionProperties
    ) -> Question:
        """Insert a new question."""

    def list_knowlets(self, user_id: UUID) -> List[Knowlet]:
        """List all knowlets for a user."""

    def insert_knowlets(
        self, question_id: str, knowlet: List[CreateKnowletProperties]
    ) -> List[Knowlet]:
        """Insert a new knowlet."""
