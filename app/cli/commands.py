import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="JobPilot",
        description="AI-powered Resume Analysis and ATS Matching Tool"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Analyze Resume
    resume_parser = subparsers.add_parser(
        "analyze-resume",
        help="Analyze a resume PDF"
    )
    resume_parser.add_argument("resume_path")

    # Analyze Job
    job_parser = subparsers.add_parser(
        "analyze-job",
        help="Analyze a job description"
    )
    job_parser.add_argument("jd_path")

    # Match
    match_parser = subparsers.add_parser(
        "match",
        help="Compare resume with job description"
    )
    match_parser.add_argument("resume_path")
    match_parser.add_argument("jd_path")

    # Cover Letter
    cover_parser = subparsers.add_parser(
        "cover-letter",
        help="Generate cover letter"
    )
    cover_parser.add_argument("resume_path")
    cover_parser.add_argument("jd_path")

    return parser