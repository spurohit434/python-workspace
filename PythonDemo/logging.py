import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("test_logger")

logger.info("info log")
logger.warn("warn log")
print(logger)