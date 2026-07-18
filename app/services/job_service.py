from app.ai_client import AIClient
from app.prompts.job_prompt import build_job_prompt


class JobService:

    def __init__(self):
        self.ai = AIClient()

    def analyze(self, job_description: str):

        prompt = build_job_prompt(job_description)

        return self.ai.ask(prompt)