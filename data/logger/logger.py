import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "jobpilot.log")

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name: str = "JobPilot"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File Handler
        file_handler = logging.FileHandler(LOG_FILE)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


logger = get_logger()