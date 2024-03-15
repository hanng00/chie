import datetime
import os
from chie.mind.utils import get_current_utc_time
from fastapi import APIRouter
from chie.mind.domain.entities.question import Question
from chie.mind.domain.services.mind_service import MindService
from chie.mind.adapters.openai_llm import OpenAILLM
from chie.mind.dto.question_dto import QuestionDTO
from chie.logger import get_logger
from openai import AsyncOpenAI

logger = get_logger(__name__)

mind_router = APIRouter()


def get_mind_service():
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    llm = OpenAILLM(openai=client)

    mind_service = MindService(llm=llm)
    return mind_service


# Display an endpoint for asking a question receiveing the response
@mind_router.post("/ask")
async def ask_mind(question: QuestionDTO):
    logger.info(f"Received question: {question.question}")
    mind_service = get_mind_service()

    domain_question = Question(
        content=question.question,
        created_at=get_current_utc_time(),
    )
    knowlet = await mind_service.ask_mind(question=domain_question)
    return knowlet


@mind_router.get("/knowlets")
async def get_mind():
    """List all knowlets for a mind."""
    logger.info("Listing all knowlets for a mind.")

    mind_service = get_mind_service()
    knowlets = await mind_service.get_knowlets()
    return knowlets
