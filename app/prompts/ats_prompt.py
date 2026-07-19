def build_ats_prompt(
    resume: str,
    job_description: str,
) -> str:
    return f"""
You are an ATS Expert.

Compare the following Resume with the Job Description.

Return ONLY in this format.

# Match Percentage

# Matching Skills

# Missing Skills

# Strengths

# Weaknesses

# Final Suggestions

Resume

{resume}

------------------------------------

Job Description

{job_description}
"""