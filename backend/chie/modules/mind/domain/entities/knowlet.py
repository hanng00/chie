from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Knowlet(BaseModel):
    """Small learning items that populate the user's feed."""

    title: str
    content: str
    
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
