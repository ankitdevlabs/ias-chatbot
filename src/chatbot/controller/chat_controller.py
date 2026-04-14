"""Chatbot service"""

from fastapi.responses import JSONResponse

from chatbot.helpers.exceptions import ChatServiceError
from chatbot.model.entities import MessageRequest
from chatbot.service.chat_service import ChatService


class ChatController:

    def __init__(self, service: ChatService):
        self.service = service

    async def get_response(self, msg: MessageRequest):

        try:
            response = await self.service.get_response(msg)

            return JSONResponse(status_code=200, content={"data": response})

        except ChatServiceError as e:
            return JSONResponse(
                status_code=503, content={"success": False, "error": e.message}
            )

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"success": False, "error": "Internal server error"},
            )
