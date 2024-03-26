import os
from chie.middleware.auth.auth_bearer import AuthBearer, get_current_user
from fastapi import APIRouter, Depends
from chie.modules.mind.adapters.langchain_runnable import langchain_rag_runnable_factory
from chie.modules.mind.domain.services.mind_rag_service import MindRagService
from chie.modules.mind.domain.services.mind_service import MindService
from chie.modules.mind.adapters.supabase_mind_repository import SupabaseMindRepository
from chie.modules.mind.adapters.openai_llm import OpenAILLM
from chie.modules.mind.dto.input import QuestionInput
from chie.logger import get_logger
from openai import AsyncOpenAI
from chie.modules.mind.dto.question import CreateQuestionProperties
from chie.modules.user.entity import UserIdentity
from chie.settings.supabase import supabase_client

logger = get_logger(__name__)

mind_router = APIRouter()


def get_mind_service():
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    llm = OpenAILLM(openai=client)

    mind_repository = SupabaseMindRepository(supabase=supabase_client)

    mind_service = MindService(llm=llm, mind_repository=mind_repository)
    return mind_service


def get_mind_rag_service():
    llm_runnable = langchain_rag_runnable_factory()
    mind_repository = SupabaseMindRepository(supabase=supabase_client)
    mind_rag_service = MindRagService(llm_runnable=llm_runnable, mind_repository=mind_repository)
    return mind_rag_service


# Display an endpoint for asking a question receiveing the response
@mind_router.post("/ask", dependencies=[Depends(AuthBearer())], tags=["Chat"])
async def ask_mind(
    question: QuestionInput, current_user: UserIdentity = Depends(get_current_user)
):
    logger.info(f"Received question: {question.question}")
    if question.service == "mind":
        mind_service = get_mind_service()
    elif question.service == "riksdagen":
        mind_service = get_mind_rag_service()
    else:
        raise ValueError(f"Invalid service '{question.service}'")

    question_properties = CreateQuestionProperties(
        user_id=current_user.id, content=question.question
    )

    knowlet = await mind_service.ask_mind(question_properties=question_properties)
    return knowlet


@mind_router.get("/knowlets", dependencies=[Depends(AuthBearer())], tags=["Chat"])
async def get_mind(current_user: UserIdentity = Depends(get_current_user)):
    """List all knowlets for a mind."""
    logger.info("Listing all knowlets for a mind.")

    mind_service = get_mind_service()
    knowlets = await mind_service.list_knowlets(user_id=current_user.id)
    return knowlets
