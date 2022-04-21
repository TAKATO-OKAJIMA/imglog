import logging
from logging import FileHandler, Formatter, StreamHandler, getLogger, Logger

LOGGERS = dict()

def getLogger(name: str) -> Logger:
    if not name in LOGGERS:
        logger = getLogger(name)
        logger.setLevel(logging.WARNING)
        streamHandler = StreamHandler()
        fileHandler = FileHandler('./' + name + '.log')

        formatter = Formatter('[IMGLOG] | %(asctime)s | %(name)s | %(levelname)s | %(message)s ')
        
        streamHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)

        logger.addHandler(streamHandler)
        logger.addHandler(fileHandler)
    else:
        logger = LOGGERS[name]

    return logger