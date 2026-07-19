from app.cli.commands import create_parser
from app.core.jobpilot import JobPilot
from app.logger.logger import get_logger


def print_result(title: str, content: str):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
    print(content)
    print("=" * 80)


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    logger = get_logger()
    jobpilot = JobPilot()

    if args.command == "analyze-resume":
        logger.info("Analyzing Resume...")
        result = jobpilot.analyze_resume(args.resume_path)
        title = "📄 Resume Analysis"

    elif args.command == "analyze-job":
        logger.info("Analyzing Job Description...")
        result = jobpilot.analyze_job(args.jd_path)
        title = "💼 Job Analysis"

    elif args.command == "match":
        logger.info("Matching Resume with Job Description...")
        result = jobpilot.match_resume(
            args.resume_path,
            args.jd_path,
        )
        title = "🎯 ATS Match"

    elif args.command == "cover-letter":
        logger.info("Generating Cover Letter...")
        result = jobpilot.generate_cover_letter(
            args.resume_path,
            args.jd_path,
        )
        title = "📄 Cover Letter"

    elif args.command == "email":
        logger.info("Generating Recruiter Email...")
        result = jobpilot.generate_email(
            args.resume_path,
            args.jd_path,
        )
        title = "📧 Recruiter Email"

    else:
        parser.print_help()
        return

    print_result(title, result)


if __name__ == "__main__":
    main()