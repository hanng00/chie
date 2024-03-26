from chie.modules.mind.domain.ports.llm_runnable import LLMRunnablePort

import os
from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.vectorstores import VectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore


class LangchainRagRunnable(LLMRunnablePort):
    def __init__(self, vectorstore: VectorStore, chat_model: BaseChatModel) -> None:
        self.vectorstore = vectorstore
        self.chat_model = chat_model

        self._runnable = self._setup_runnable()

    def invoke(self, input: str) -> str:
        output = self._runnable.invoke(input)
        return output

    def _setup_runnable(self):
        retreiver = self.vectorstore.as_retriever()
        prompt = PromptTemplate.from_template(
            """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
        Question: {question} 
        Context: {context} 
        Answer:"""
        )

        rag_chain = (
            {
                "context": retreiver | self._format_docs,
                "question": RunnablePassthrough(),
            }
            | prompt
            | self.chat_model
            | StrOutputParser()
        )
        return rag_chain

    def _format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)


def langchain_rag_runnable_factory():
    # CONSTS
    OPENAI_EMBEDDING_MODEL = "text-embedding-3-large"
    EMBEDDING_DIM = 1536
    INDEX_NAME = "chie-rag"
    NAMESPACE = "riksdagen-test"

    # Initialize a LangChain embedding object
    embeddings = OpenAIEmbeddings(
        openai_api_type=os.environ["OPENAI_API_KEY"],
        model=OPENAI_EMBEDDING_MODEL,
        dimensions=EMBEDDING_DIM,
    )

    # Initialize the LangChain vector store
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        namespace=NAMESPACE,
        embedding=embeddings,
        text_key="text",  # The original text is stored in the metadata under the key "text"
    )

    # Initialize the LangChain chat model
    chat_model = ChatOpenAI(
        api_key=os.environ["OPENAI_API_KEY"], model="gpt-3.5-turbo", temperature=0.0
    )

    return LangchainRagRunnable(vectorstore=vectorstore, chat_model=chat_model)
