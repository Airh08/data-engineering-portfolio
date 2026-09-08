import os
import sys


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
sys.path = [path for path in sys.path if os.path.abspath(path or ".") != SCRIPT_DIRECTORY]

import logging


LOGGER_NAME = "portfolio.logging_example"


def configure_logger() -> logging.Logger:
    """Create a logger with levels, a handler, and a timestamp formatter."""
    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_application_events(logger: logging.Logger) -> None:
    """Log normal activity and recoverable problems at appropriate levels."""
    logger.debug("Debug details are filtered by the handler level")
    logger.info("Application started")
    logger.warning("Configuration uses the default timeout")
    logger.error("Could not connect to the optional metrics service")


def log_exception(logger: logging.Logger) -> None:
    """Log an exception with its traceback using logger.exception."""
    try:
        int("not-a-number")
    except ValueError:
        logger.exception("Could not convert the configured port to an integer")


def main() -> None:
    """Run logging examples with a consistent application logger."""
    logger = configure_logger()
    log_application_events(logger)
    log_exception(logger)
    logger.info("Application finished")


if __name__ == "__main__":
    main()