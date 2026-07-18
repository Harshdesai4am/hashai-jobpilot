from app.core.jobpilot import JobPilot
from app.logger.logger import logger


def main():
    logger.info("Application Started")

    try:
        jobpilot = JobPilot()

        result = jobpilot.match_resume(
            "data/resumes/resume.pdf",
            "data/jobs/react_native_jd.txt"
        )

        print("\n" + "=" * 80)
        print("🚀 JobPilot ATS Report")
        print("=" * 80)
        print(result)
        print("=" * 80)

        logger.info("Resume Matching Completed")

    except Exception as e:
        logger.exception(f"Application Error: {e}")
        print(f"\n❌ Error: {e}")

    finally:
        logger.info("Application Closed")


if __name__ == "__main__":
    main()