import logging
from logging import FileHandler, Formatter, StreamHandler, Logger

LOGGERS = dict()

__all__ = [
    'getLogger'
]

def getLogger(name: str) -> Logger:
    if not name in LOGGERS:
        logger = logging.getLogger(name)
        logger.setLevel(logging.WARNING)
        streamHandler = StreamHandler()
        fileHandler = FileHandler('./' + name + '.log')

        formatter = Formatter('[IMGLOG] | %(asctime)s | %(name)s | %(levelname)s | %(message)s ')
        
        streamHandler.setFormatter(formatter)
        streamHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logging.DEBUG)

        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
    else:
        logger = logging.getLogger(name)

    return logger