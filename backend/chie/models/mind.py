from typing import List
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

from chie.models.db import Base


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Define the relationship with Knowlet
    knowlets = relationship(
        "Knowlet", back_populates="question", cascade="all, delete-orphan"
    )


class Knowlet(Base):
    __tablename__ = "knowlet"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Define the foreign key to link with Question
    question_id = Column(Integer, ForeignKey("question.id"))

    # Define the relationship with Question
    question = relationship("Question", back_populates="knowlets")
