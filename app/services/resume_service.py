from app.ai_client import ai_client
from app.prompts.resume_prompt import build_resume_prompt

class ResumeService:

    def analyze(self, resume: str) -> str:
        prompt = build_resume_prompt(resume)
        return ai_client.ask(prompt)