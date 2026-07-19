from app.ai_client import ai_client
from app.prompts.email_prompt import build_email_prompt


class EmailService:
    """
    Service responsible for generating a professional recruiter email.
    """

    def generate(
        self,
        resume: str,
        job_description: str,
    ) -> str:
        prompt = build_email_prompt(
            resume,
            job_description,
        )

        return ai_client.ask(prompt)