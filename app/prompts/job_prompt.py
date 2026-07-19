def build_job_prompt(job_description: str) -> str:
    return f"""
Analyze the following Job Description.

Return only:

## Required Skills

## Nice to Have Skills

## Experience Required

## Responsibilities

## Important Keywords

Job Description:

{job_description}
"""