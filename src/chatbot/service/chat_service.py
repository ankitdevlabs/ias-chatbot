from chatbot.model.entities import MessageRequest


class ChatService:
    def __init__(self, settings):
        self.settings = settings

    async def build_static_response(self, msg: MessageRequest) -> str:
        if "service" in msg.text:
            return "We provide IT networking, security, and infrastructure solutions."

        elif "contact" in msg.text:
            return "You can contact us through the contact page on our website."

        elif "location" in msg.text:
            return "Please check our website for our office location details."

        elif "hello" in msg.text or "hi" in msg.text:
            return "Hey! How can I assist you today?"

        else:
            return "I'm not sure about that yet, but I can help with services and contact info!"
