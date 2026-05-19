import logging
import sys
import os

os.makedirs("logs", exist_ok=True)

def setup_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    ))

    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(logging.Formatter(
        '{"time": "%(asctime)s", "level": "%(levelname)s", '
        '"logger": "%(name)s", "message": "%(message)s"}'
    ))

    logger.addHandler(console)
    logger.addHandler(file_handler)
    return logger