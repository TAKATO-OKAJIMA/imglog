import atexit

import handler
from .handler import Handler, CSVHandler, HTMLHandler, XMLHandler, JSONHandler
from .logger import *


def shutdown() -> None:
    BytesImageLoggerFactory().close()
    ArrayImageLoggerFactory().close()
    PillowImageLoggerFactory().close()
    BaseImageLoggerFactory().close()
    handler.close()

    del BytesImageLoggerFactory()
    del ArrayImageLoggerFactory()
    del PillowImageLoggerFactory()
    del BaseImageLoggerFactory()


atexit.register(shutdown)