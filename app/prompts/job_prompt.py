from app.prompts.system_prompt import SYSTEM_PROMPT


def build_job_prompt(job_description: str) -> str:
    return f"""
{SYSTEM_PROMPT}

Analyze the following Job Description.

Provide:

1. Required Skills
2. Preferred Skills
3. Responsibilities
4. Experience Required
5. Important Keywords

Job Description:

{job_description}
"""