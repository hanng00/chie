from typing import List
from chie.logger import get_logger
from chie.modules.mind.domain.ports.mind_repository import MindRepository
from chie.modules.mind.dto.question import (
    CreateKnowletProperties,
    CreateQuestionProperties,
)
from chie.modules.mind.domain.entities.question import Question
from chie.modules.mind.domain.entities.knowlet import Knowlet

from supabase import Client

logger = get_logger(__name__)


class SupabaseMindRepository(MindRepository):
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def insert_question(
        self, question_properties: CreateQuestionProperties
    ) -> Question:
        insert_data = {
            "user_id": str(question_properties.user_id),
            "content": question_properties.content,
        }
        data = (self.supabase.table("question").insert(insert_data).execute()).data

        return Question(**data[0])

    def list_knowlets(self, user_id: str) -> Knowlet:
        # Only list the user's knowlets
        data = (
            self.supabase.table("knowlet")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        ).data

        return [Knowlet(**d) for d in data]

    def insert_knowlets(
        self, question_id: int, knowlets_properties: List[CreateKnowletProperties]
    ) -> List[Knowlet]:
        insert_data = [
            {
                "question_id": question_id,
                "title": knowlet.title,
                "content": knowlet.content,
            }
            for knowlet in knowlets_properties
        ]
        data = (self.supabase.table("knowlet").insert(insert_data).execute()).data
        return [Knowlet(**d) for d in data]
