import re
import time
from typing import Any

try:
    from ollama import chat as ollama_chat
except ImportError:  # pragma: no cover
    ollama_chat = None

from app.config import (
    MODEL_NAME,
    TEMPERATURE,
    MAX_TOKENS,
)
from app.logger.logger import get_logger
from app.prompts.system_prompt import SYSTEM_PROMPT

logger = get_logger()


class AIClient:
    """
    Central AI Client for JobPilot.

    Features
    --------
    • Singleton Instance
    • Automatic Retry
    • Compatible with old & new Ollama Python SDK
    • Response Validation
    • Structured Logging
    • Graceful Fallback
    """

    MAX_RETRIES = 3
    RETRY_DELAY = 2

    def ask(self, prompt: str) -> str:
        """
        Send prompt to Ollama and return AI response.
        """

        if ollama_chat is None:
            logger.error("Ollama Python package is not installed.")
            return self._fallback_response(prompt)

        for attempt in range(1, self.MAX_RETRIES + 1):
            try:
                logger.info(
                    f"Calling model '{MODEL_NAME}' "
                    f"(Attempt {attempt}/{self.MAX_RETRIES})"
                )

                response = ollama_chat(
                    model=MODEL_NAME,
                    messages=self._build_messages(prompt),
                    options={
                        "temperature": TEMPERATURE,
                        "num_predict": MAX_TOKENS,
                    },
                )

                logger.info(f"Response Type : {type(response)}")

                content = self._extract_response(response)

                if content:
                    logger.info("AI response generated successfully.")
                    return content

                logger.warning("Received empty response from AI.")

            except Exception:
                logger.exception(
                    f"Attempt {attempt} failed while calling Ollama."
                )

            if attempt < self.MAX_RETRIES:
                time.sleep(self.RETRY_DELAY)

        logger.error("All retry attempts failed.")

        return self._fallback_response(prompt)

    @staticmethod
    def _build_messages(prompt: str) -> list[dict[str, str]]:
        """
        Build chat payload.
        """

        return [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ]

    @staticmethod
    def _extract_response(response: Any) -> str | None:
        """
        Supports both older dict responses and newer ChatResponse objects.
        """

        try:
            # Latest Ollama SDK
            if hasattr(response, "message"):
                content = response.message.content
                if content:
                    return content.strip()

            # Older SDK
            if isinstance(response, dict):
                content = (
                    response.get("message", {})
                    .get("content", "")
                    .strip()
                )

                if content:
                    return content

        except Exception:
            logger.exception("Unable to extract AI response.")

        return None

    @staticmethod
    def _fallback_response(prompt: str) -> str:
        """
        Generate a basic fallback response.
        """

        keywords = re.findall(
            r"\b[A-Za-z]{3,}\b",
            prompt,
        )

        detected_keywords = ", ".join(
            sorted(set(keywords[:20]))
        )

        if not detected_keywords:
            detected_keywords = "No keywords detected"

        return f"""
⚠️ AI backend is currently unavailable.

A fallback response has been generated.

Detected Keywords
-----------------
{detected_keywords}

Please verify:

• Ollama is installed
• Ollama service is running
• Model '{MODEL_NAME}' exists locally
• Configuration is correct
• Retry the command
""".strip()


# ==================================================
# Singleton Instance
# ==================================================

ai_client = AIClient()