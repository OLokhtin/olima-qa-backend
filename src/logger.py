import logging
from datetime import datetime

logger = logging.getLogger()

formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler = logging.FileHandler(
    f"logs/info_{datetime.now().strftime('%Y%m%d')}.log"
)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.INFO)