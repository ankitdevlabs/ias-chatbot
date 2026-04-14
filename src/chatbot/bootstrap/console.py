"""Console Commands"""

import uvicorn


class CliCommand:

    def serve(self, host: str = "127.0.0.1", port: int = 9000):
        """Server FastApi Application"""
        uvicorn.run(
            self._get_app_runner(), port=port, host=host, log_level="info", reload=True
        )

    def _get_app_runner(self) -> str:
        return "chatbot.bootstrap.main:app"
