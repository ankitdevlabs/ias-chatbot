"""Chatbot service"""

from chatbot.service.chat_service import ChatService
from chatbot.model.entities import MessageRequest


class ChatController:

    def __init__(self, service: ChatService):
        self.service = service

    async def chat_response(self, msg: MessageRequest):

        await self.service.build_static_response(msg)
