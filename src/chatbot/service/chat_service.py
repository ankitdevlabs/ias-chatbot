"""Chat service"""

from google import genai

from chatbot.configs.constants import KNOWLEDGE_BASE
from chatbot.model.entities import MessageRequest
from chatbot.helpers.exceptions import ChatServiceError


class ChatService:
    def __init__(self, settings):
        self.settings = settings
        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def get_response(self, msg: MessageRequest) -> str:
        text = msg.text.lower().strip()

        static_response = await self._get_static_response(text)
        if static_response:
            return static_response

        return await self._ask_ai(text)

    async def _get_static_response(self, text: str):
        for key, value in KNOWLEDGE_BASE.items():
            if key in text:
                return value
        return None

    async def _ask_ai(self, text: str) -> str:
        prompt = f"""
            You are a helpful AI assistant for an IT networking company.

            Be concise, professional, and helpful.

            User: {text}
            Assistant:
        """

        try:
            response = self.client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )

            if not response or not response.text:
                raise ChatServiceError("Service is Currently Not available")

            return response.text.strip()

        except Exception as e:
            raise ChatServiceError(f"AI service failed: {str(e)}")
