from ollama import chat
from app.config import MODEL_NAME
from app.prompts.system_prompt import SYSTEM_PROMPT


class AIClient:

    def ask(self, prompt: str) -> str:

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]