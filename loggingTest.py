import logging

# create logger and configure it

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="D:\\Workspace\\code\\Python\\documentationPractice\\myapp.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode="w",
)

logger = logging.getLogger()

# test all message levels
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
