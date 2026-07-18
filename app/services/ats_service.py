from app.ai_client import AIClient
from app.ats.extractor import SkillExtractor
from app.ats.calculator import ATSCalculator


class ATSService:

    def __init__(self):
        self.ai = AIClient()
        self.extractor = SkillExtractor()
        self.calculator = ATSCalculator()

    def compare(self, resume: str, job_description: str):

        resume_skills = self.extractor.extract(resume)
        jd_skills = self.extractor.extract(job_description)

        ats_result = self.calculator.calculate(
            resume_skills,
            jd_skills
        )

        prompt = f"""
You are an ATS Expert.

Below is the ATS analysis already calculated by Python.

Do NOT calculate another score.

ATS Score: {ats_result["score"]}

Matched Skills:
{", ".join(ats_result["matched"])}

Missing Skills:
{", ".join(ats_result["missing"])}

Based on this analysis provide:

# Strengths

# Weaknesses

# Suggestions
"""

        ai_response = self.ai.ask(prompt)

        return {
            "ats": ats_result,
            "analysis": ai_response
        }