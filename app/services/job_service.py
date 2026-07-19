from app.ai_client import ai_client
from app.prompts.job_prompt import build_job_prompt

class JobService:

    def analyze(self, job_description: str) -> str:
        prompt = build_job_prompt(job_description)
        return ai_client.ask(prompt)