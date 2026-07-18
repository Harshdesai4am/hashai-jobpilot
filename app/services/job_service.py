from app.ai_client import AIClient


class JobService:

    def __init__(self):
        self.ai = AIClient()

    def analyze(self, job_description: str):

        prompt = f"""
Analyze the following Job Description.

Return only:

## Required Skills

## Nice to Have Skills

## Experience Required

## Responsibilities

## Important Keywords

Job Description:

{job_description}
"""

        return self.ai.ask(prompt)