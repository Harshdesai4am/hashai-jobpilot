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
    resume_parser.add_argument(
        "resume_path",
        help="Path to resume PDF"
    )

    # Analyze Job Description
    job_parser = subparsers.add_parser(
        "analyze-job",
        help="Analyze a job description"
    )
    job_parser.add_argument(
        "jd_path",
        help="Path to job description file"
    )

    # Match Resume
    match_parser = subparsers.add_parser(
        "match",
        help="Compare resume with job description"
    )

    match_parser.add_argument(
        "resume_path",
        help="Resume PDF"
    )

    match_parser.add_argument(
        "jd_path",
        help="Job description file"
    )

    return parser