from app.prompts.system_prompt import SYSTEM_PROMPT


def build_resume_prompt(resume: str) -> str:
    return f"""
{SYSTEM_PROMPT}

Analyze the following resume.

Provide:

1. Professional Summary
2. Technical Skills
3. Strengths
4. Weaknesses
5. Missing Skills
6. ATS Improvement Suggestions

Resume:

{resume}
"""