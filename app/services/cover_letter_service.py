from app.ai_client import ai_client
from app.prompts.cover_letter_prompt import build_cover_letter_prompt

class CoverLetterService:

    def generate(
        self,
        resume: str,
        job_description: str,
    ) -> str:
        prompt = build_cover_letter_prompt(
            resume,
            job_description,
        )

        return ai_client.ask(prompt)