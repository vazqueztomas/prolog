from loguru import logger
from typing import Literal

LoggingLevels = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def log(message: str, level: LoggingLevels = "INFO") -> None:
    logger.log(level, message)
