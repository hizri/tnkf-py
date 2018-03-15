import logging
import sys
from io import StringIO

logger = logging.getLogger('test')
logger.setLevel(logging.DEBUG)

buffer_stream = StringIO()

buffer_handler = logging.StreamHandler(stream=buffer_stream)
console_handler = logging.StreamHandler(stream=sys.stdout)
buffer_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
buffer_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(buffer_handler)
