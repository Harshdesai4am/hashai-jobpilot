from app.ai_client import AIClient


class ResumeService:

    def __init__(self):
        self.ai = AIClient()

    def analyze(self, resume: str):

        prompt = f"""
Analyze the following resume.

Provide:

1. Professional Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. ATS Score out of 100
6. Suggestions

Resume:

{resume}
"""

        return self.ai.ask(prompt)