import logging

import somelib

logging.basicConfig(level=logging.ERROR)
# somelib.func()
logging.getLogger('somelib').level = logging.DEBUG
somelib.func()
