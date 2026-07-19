def build_resume_prompt(resume: str) -> str:
    return f"""
Analyze the following resume.

Provide:

1. Professional Summary
2. Strengths
3. Weaknesses
4. Missing Skills
5. ATS Score out of 100
6. Suggestions

Resume:

{resume}
"""