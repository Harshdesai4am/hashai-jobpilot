from app.prompts.system_prompt import SYSTEM_PROMPT


def build_cover_letter_prompt(
    resume: str,
    job_description: str,
) -> str:

    return f"""
{SYSTEM_PROMPT}

Write a professional ATS-friendly cover letter.

Requirements:
- Address the hiring manager professionally.
- Mention relevant experience.
- Highlight matching skills.
- Explain why the candidate is a good fit.
- Keep it under 300 words.

Resume:

{resume}

--------------------------------------------

Job Description:

{job_description}
"""