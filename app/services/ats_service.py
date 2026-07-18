from app.ai_client import AIClient


class ATSService:

    def __init__(self):
        self.ai = AIClient()

    def compare(self, resume: str, job_description: str):

        prompt = f"""
You are an ATS Expert.

Compare the following Resume with the Job Description.

Return ONLY in this format.

# Match Percentage

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Final Suggestions

Resume

{resume}

------------------------------------

Job Description

{job_description}
"""

        return self.ai.ask(prompt)