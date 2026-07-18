from app.ai_client import AIClient

from app.ats.calculator import ATSCalculator
from app.ats.extractor import SkillExtractor

from app.prompts.ats_prompt import build_ats_prompt


class ATSService:

    def __init__(self):
        self.ai = AIClient()
        self.extractor = SkillExtractor()
        self.calculator = ATSCalculator()

    def compare(self, resume: str, job_description: str):

        # Extract skills
        resume_skills = self.extractor.extract(resume)
        job_skills = self.extractor.extract(job_description)

        # Calculate ATS score
        ats_result = self.calculator.calculate(
            resume_skills,
            job_skills,
        )

        # Build AI prompt
        prompt = build_ats_prompt(
            resume=resume,
            job_description=job_description,
            score=ats_result["score"],
            matched=ats_result["matched"],
            missing=ats_result["missing"],
        )

        # AI explanation
        analysis = self.ai.ask(prompt)

        return {
            "ats": ats_result,
            "analysis": analysis,
        }