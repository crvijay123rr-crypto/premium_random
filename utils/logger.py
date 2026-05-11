import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logger = logging.getLogger(
    "PREMIUM_BOT"
)

# LOG INFO
def info(text):

    logger.info(text)

# LOG ERROR
def error(text):

    logger.error(text)
