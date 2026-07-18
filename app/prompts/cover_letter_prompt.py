def build_cover_letter_prompt(
    resume: str,
    job_description: str,
) -> str:

    return f"""
You are an expert Technical Recruiter.

Write a professional ATS-friendly cover letter.

Rules:

- Maximum 350 words
- Professional tone
- Do not invent experience
- Highlight only skills from the resume
- Mention why the candidate is a good fit
- End professionally

Resume:

{resume}

--------------------------------

Job Description:

{job_description}
"""