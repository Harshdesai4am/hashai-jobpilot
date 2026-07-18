def build_ats_prompt(
    resume: str,
    job_description: str,
    score: int,
    matched: list,
    missing: list,
) -> str:

    return f"""
You are an ATS Expert.

The ATS score has already been calculated.

Do NOT calculate another score.

ATS Score:
{score}

Matched Skills:
{', '.join(matched)}

Missing Skills:
{', '.join(missing)}

Resume:

{resume}

--------------------------------

Job Description:

{job_description}

Explain:

1. Why this score was achieved.
2. Candidate strengths.
3. Missing skills.
4. Suggestions to improve the resume.
"""