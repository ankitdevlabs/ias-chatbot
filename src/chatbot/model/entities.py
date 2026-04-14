"""Models for the chatbot application."""

from pydantic import BaseModel


class MessageRequest(BaseModel):
    text: str
