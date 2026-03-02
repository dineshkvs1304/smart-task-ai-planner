import logging

def setup_logger():
    logger = logging.getLogger("smart-task-ai")

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler("app.log")
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger