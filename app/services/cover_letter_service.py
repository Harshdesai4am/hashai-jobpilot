from app.ai_client import AIClient
from app.prompts.cover_letter_prompt import build_cover_letter_prompt


class CoverLetterService:

    def __init__(self):
        self.ai = AIClient()

    def generate(
        self,
        resume: str,
        job_description: str,
    ):

        prompt = build_cover_letter_prompt(
            resume,
            job_description,
        )

        return self.ai.ask(prompt)