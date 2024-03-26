from pydantic import BaseModel
from typing import Dict, List, Optional


class DocumentMetadata(BaseModel):
    """
    Represents metadata about a document.
    """

    data: Dict[str, str]  # Additional metadata


class Document(BaseModel):
    id: str
    text: str
    metadata: Optional[DocumentMetadata] = None


class Embedding(BaseModel):
    document: Document
    embedding: List[float]
