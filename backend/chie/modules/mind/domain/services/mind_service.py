import random
from typing import Dict, List
import asyncio
from chie.modules.mind.domain.entities.knowlet import Knowlet
from chie.modules.mind.domain.entities.question import Question
from chie.modules.mind.domain.ports.llm import LLMPort
from chie.modules.mind.domain.ports.mind_repository import MindRepository
from chie.modules.mind.domain.services.templates import LEARNING_STYLES, PROMPT
from chie.modules.mind.dto.question import (
    CreateKnowletProperties,
    CreateQuestionProperties,
)
from chie.modules.mind.utils import get_current_utc_time
from chie.logger import get_logger
from uuid import UUID


MOCK_LIST_KNOWLETS = [
    {
        "title": "Narrative Learning",
        "content": """## Reading through the topic of narrative learning""",
    },
    {
        "title": "Socratic Dialogues",
        "content": """## Understanding Computational Neuroscience Through Real-World Problems

Imagine designing a brain-computer interface for paralyzed patients to control robotic limbs. 
1. Identify the neural circuitry involved.
2. Research how neural signals can be decoded into movement commands.
3. Collaborate to refine algorithms for real-time processing.
4. Apply computational neuroscience principles to improve accuracy and responsiveness.
5. Test and troubleshoot the system in simulated and real-world scenarios.
6. Reflect on the ethical implications and societal impact of your work.""",
    },
]

logger = get_logger(__name__)
N_LEARNING_STYLES = 3


class MindService:
    def __init__(self, llm: LLMPort, mind_repository: MindRepository) -> None:
        self.llm = llm
        self.mind_repository = mind_repository

        self.learning_style = LEARNING_STYLES
        self.prompt = PROMPT

    async def ask_mind(
        self, question_properties: CreateQuestionProperties
    ) -> List[Knowlet]:
        question = self.mind_repository.insert_question(question_properties)

        random_learning_styles = random.sample(self.learning_style, N_LEARNING_STYLES)
        logger.info(random_learning_styles)

        async_tasks = []
        for ls in random_learning_styles:
            name, instruction = ls["name"], ls["instruction"]
            instruction_prompt = self.prompt(instruction, 500)
            async_task = self._process_learning_style(
                name, instruction_prompt, question
            )
            async_tasks.append(async_task)

        knowlets_properties = await asyncio.gather(*async_tasks)
        knowlets = self.mind_repository.insert_knowlets(
            question_id=question.id, knowlets_properties=knowlets_properties
        )

        return knowlets

    async def list_knowlets(self, user_id: UUID) -> List[Knowlet]:
        knowlets = self.mind_repository.list_knowlets(user_id)

        return knowlets

    async def _process_learning_style(
        self, name: str, instruction_prompt: str, question: Question
    ) -> CreateKnowletProperties:
        completion = await self.llm.completion(
            instruction=instruction_prompt, prompt=question.content
        )
        return CreateKnowletProperties(
            title=name,
            content=completion,
        )
