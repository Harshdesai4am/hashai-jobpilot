from app.prompts.system_prompt import SYSTEM_PROMPT


def build_cover_letter_prompt(
    resume: str,
    job_description: str,
) -> str:

    return f"""
{SYSTEM_PROMPT}

Write a professional ATS-friendly cover letter.

Rules:

- Maximum 350 words
- Professional tone
- Do not invent experience
- Mention only technologies present in the resume
- Explain why the candidate is a good fit
- End professionally

Resume:

{resume}

--------------------------------------------------

Job Description:

{job_description}
"""