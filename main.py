from app.cli.commands import create_parser
from app.core.jobpilot import JobPilot
from app.logger.logger import logger


def main():
    parser = create_parser()
    args = parser.parse_args()

    jobpilot = JobPilot()

    logger.info("Application Started")

    try:

        if args.command == "analyze-resume":

            logger.info(f"Analyzing Resume: {args.resume_path}")

            result = jobpilot.analyze_resume(
                args.resume_path
            )

            title = "🚀 Resume Analysis"

        elif args.command == "analyze-job":

            logger.info(f"Analyzing Job Description: {args.jd_path}")

            result = jobpilot.analyze_job(
                args.jd_path
            )

            title = "🚀 Job Description Analysis"

        elif args.command == "match":

            logger.info(
                f"Matching Resume: {args.resume_path} with JD: {args.jd_path}"
            )

            result = jobpilot.match_resume(
                args.resume_path,
                args.jd_path
            )

            title = "🚀 JobPilot ATS Report"

        elif args.command == "cover-letter":

            logger.info("Generating Cover Letter")

            result = jobpilot.generate_cover_letter(
                args.resume_path,
                args.jd_path
            )

            title = "🚀 Cover Letter"

        else:
            parser.print_help()
            return

        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)
        print(result)
        print("=" * 80)

        logger.info("Command executed successfully")

    except FileNotFoundError as e:
        logger.exception(e)
        print(f"\n❌ File not found: {e}")

    except Exception as e:
        logger.exception(e)
        print(f"\n❌ Unexpected Error: {e}")

    finally:
        logger.info("Application Closed")


if __name__ == "__main__":
    main()