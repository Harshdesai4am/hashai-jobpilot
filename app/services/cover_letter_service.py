from app.ai_client import AIClient


class CoverLetterService:

    def __init__(self):
        self.ai = AIClient()

    def generate(self, resume: str, job_description: str):

        prompt = f"""
You are an expert Technical Recruiter.

Using the following Resume and Job Description, write a professional cover letter.

Rules:

- Maximum 350 words
- ATS friendly
- Professional tone
- Do not invent experience
- Highlight only skills present in the resume
- Mention why the candidate is a good fit
- End professionally

Resume:

{resume}

--------------------------------

Job Description:

{job_description}
"""

        return self.ai.ask(prompt)