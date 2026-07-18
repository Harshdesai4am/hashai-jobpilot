from app.prompts.system_prompt import SYSTEM_PROMPT


def build_ats_prompt(
    resume: str,
    job_description: str,
    score: int,
    matched: list,
    missing: list,
) -> str:

    matched_skills = ", ".join(matched) if matched else "None"
    missing_skills = ", ".join(missing) if missing else "None"

    return f"""
{SYSTEM_PROMPT}

The ATS score has already been calculated using a Python algorithm.

DO NOT calculate another ATS score.

ATS Result

Score:
{score}

Matched Skills:
{matched_skills}

Missing Skills:
{missing_skills}

Resume:

{resume}

--------------------------------------------------

Job Description:

{job_description}

Explain:

1. Why this ATS score was achieved.
2. Candidate strengths.
3. Missing skills.
4. Resume improvement suggestions.
5. Final recommendation.
"""