from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from chatbot.model.entities import MessageRequest
from chatbot.dependencies.common import get_chat_controller
from chatbot.controller.chat_controller import ChatController

router = APIRouter(tags=["chat"])


@router.post("/chat")
def chat(
    payload: MessageRequest,
    service: ChatController = Depends(get_chat_controller),
):
    # response = chatbot_response(message.text)
    # return {"response": response}
    pass


@router.options("/chat")
async def options_analyze():
    """Handle CORS preflight"""
    return JSONResponse(
        content={"message": "OK"},
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type",
        },
    )
