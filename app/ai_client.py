from ollama import chat
from app.config import MODEL_NAME


class AIClient:

    def ask(self, prompt: str):

        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]