import logging

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


def func():
    log.critical('A critical Error')
    log.debug('A debug message')
