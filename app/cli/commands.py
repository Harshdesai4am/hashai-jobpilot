import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="JobPilot",
        description="AI-powered Resume Analysis, ATS Matching, Cover Letter & Recruiter Email Generator",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    # Resume Analysis
    resume_parser = subparsers.add_parser(
        "analyze-resume",
        help="Analyze a resume PDF",
    )
    resume_parser.add_argument(
        "resume_path",
        help="Path to the resume PDF",
    )

    # Job Description Analysis
    job_parser = subparsers.add_parser(
        "analyze-job",
        help="Analyze a job description",
    )
    job_parser.add_argument(
        "jd_path",
        help="Path to the job description file",
    )

    # ATS Match
    match_parser = subparsers.add_parser(
        "match",
        help="Compare resume with a job description",
    )
    match_parser.add_argument(
        "resume_path",
        help="Path to the resume PDF",
    )
    match_parser.add_argument(
        "jd_path",
        help="Path to the job description file",
    )

    # Cover Letter
    cover_parser = subparsers.add_parser(
        "cover-letter",
        help="Generate an ATS-friendly cover letter",
    )
    cover_parser.add_argument(
        "resume_path",
        help="Path to the resume PDF",
    )
    cover_parser.add_argument(
        "jd_path",
        help="Path to the job description file",
    )

    # Recruiter Email
    email_parser = subparsers.add_parser(
        "email",
        help="Generate a professional recruiter email",
    )
    email_parser.add_argument(
        "resume_path",
        help="Path to the resume PDF",
    )
    email_parser.add_argument(
        "jd_path",
        help="Path to the job description file",
    )

    return parser