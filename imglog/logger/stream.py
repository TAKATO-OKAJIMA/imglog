import logging
from logging import Formatter, StreamHandler, getLogger, Logger

LOGGERS = dict()

def getLogger(name: str) -> Logger:
    if not name in LOGGERS:
        logger = getLogger(name)
        logger.setLevel(logging.WARNING)
        streamHandler = StreamHandler()

        formatter = Formatter('[IMGLOG] | %(asctime)s | %(name)s | %(levelname)s | %(message)s ')
        
        streamHandler.setFormatter(formatter)

        logger.addHandler(streamHandler)
    else:
        logger = LOGGERS[name]

    return logger