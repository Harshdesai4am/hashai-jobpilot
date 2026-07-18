from app.ai_client import AIClient
from app.prompts.resume_prompt import build_resume_prompt


class ResumeService:

    def __init__(self):
        self.ai = AIClient()

    def analyze(self, resume: str):

        prompt = build_resume_prompt(resume)

        return self.ai.ask(prompt)