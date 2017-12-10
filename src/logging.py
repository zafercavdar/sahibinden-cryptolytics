import sys
import logging
from .config import LOG_LEVEL


def setup_logging():
    logger = logging.getLogger()
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
    handler.setFormatter(formatter)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    logger.addHandler(handler)

    # silence the java gateway
    logging.getLogger('py4j.java_gateway').setLevel(getattr(logging, 'WARN'))
