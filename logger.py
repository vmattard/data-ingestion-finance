import logging

from src import file_utils


class ConsoleFormatter(logging.Formatter):
    light_blue = "\x1b[1;36m"
    purple = "\x1b[1;35m"
    blue = "\x1b[1;34m"
    green = "\x1b[1;32m"
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: blue + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        return logging.Formatter(self.FORMATS.get(record.levelno)).format(record)


def setup_logging() -> logging.Logger:
    level = logging.DEBUG

    logger = logging.getLogger(name="finance-app")
    logger.setLevel(level=level)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")

    # Log to console (INFO and above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(ConsoleFormatter())

    # Log to a file (ERROR and above)
    file_handler = logging.FileHandler(file_utils.get_logs_folder() / "finance-app.log")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger


LOGGER = setup_logging()
