"""Common"""

from fastapi import Depends, Request

from chatbot.controller.chat_controller import ChatController
from chatbot.service.chat_service import ChatService


def get_settings(request: Request):
    return request.app.state.settings


def get_chat_controller(settings=Depends(get_settings)) -> ChatController:
    service = ChatService(settings)
    return ChatController(service)
