from app.prompts.system_prompt import SYSTEM_PROMPT


def build_email_prompt(
    resume: str,
    job_description: str,
) -> str:

    return f"""
{SYSTEM_PROMPT}

Write a professional job application email.

Requirements:

- Professional subject line
- Short introduction
- Mention relevant experience
- Mention attached resume
- Mention interest in the role
- Thank the recruiter
- Maximum 200 words

Resume:

{resume}

--------------------------------------------

Job Description:

{job_description}
"""