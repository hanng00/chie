import logging
from logging.handlers import RotatingFileHandler


def get_logger(logger_name, log_level=logging.INFO, log_file="application.log"):
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.propagate = False  # Prevent log propagation to avoid double logging

    console_handler = logging.StreamHandler()

    if not logger.handlers:
        logger.addHandler(console_handler)

    return logger
