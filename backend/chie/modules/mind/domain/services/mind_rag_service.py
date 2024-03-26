from typing import List
from chie.modules.mind.domain.entities.knowlet import Knowlet
from chie.modules.mind.domain.ports.mind_repository import MindRepository
from chie.modules.mind.domain.ports.llm_runnable import LLMRunnablePort
from chie.modules.mind.dto.question import (
    CreateKnowletProperties,
    CreateQuestionProperties,
)
from chie.logger import get_logger


logger = get_logger(__name__)
N_LEARNING_STYLES = 3


class MindRagService:
    def __init__(
        self, llm_runnable: LLMRunnablePort, mind_repository: MindRepository
    ) -> None:
        self.llm_runnable = llm_runnable
        self.mind_repository = mind_repository

    async def ask_mind(
        self, question_properties: CreateQuestionProperties
    ) -> List[Knowlet]:
        question = self.mind_repository.insert_question(question_properties)

        logger.info("Invoking RAG chain.")
        rag_response = self.llm_runnable.invoke(question_properties.content)
        knowlets_properties = [
            CreateKnowletProperties(
                title="RAG Reponse",
                content=rag_response,
            )
        ]

        knowlets = self.mind_repository.insert_knowlets(
            question_id=question.id, knowlets_properties=knowlets_properties
        )

        return knowlets
