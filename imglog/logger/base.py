import base64
import io
import logging
from logging import _Level
from typing import List

from numpy import byte, record
from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .stream import getLogger
from ..record import ImageLogRecord, ImageProperty
from ..handler.abc import AbstractHandler


class BaseImageLogger(AbstractImageLogger):

    def __init__(self, name: str) -> None:
        self.__streamLogger = getLogger(name)
        self.__handlers = list()
        self.__level = logging.WARNING
 

    def logs(self, level: int, images: List[bytes], imagesProperty: List[ImageProperty]) -> None:
        if level >= self.__level:
            record = ImageLogRecord(level,
                                    [self.__imageExchangeBase64(image) for image in images],
                                    imagesProperty
                                    )
            
            self.__streamLogger.log(level, record.id)

            for handler in self.__handlers:
                handler.emit(record)
        

    def log(self, level: int, image: bytes) -> None:
        self.logs(level, [image])

    def debugs(self, images: List[bytes]) -> None:
        self.logs(logging.DEBUG, images)

    def debug(self, image: bytes) -> None:
        self.debugs([image])

    def infos(self, images: List[bytes]) -> None:
        self.logs(logging.INFO, images)

    def info(self, image: bytes) -> None:
        self.infos([image] )

    def warnings(self, images: List[bytes]) -> None:
        self.logs(logging.WARNING, images)
    
    def warning(self, image: bytes) -> None:
        self.warnings([image])

    def errors(self, images: List[bytes]) -> None:
        self.logs(logging.ERROR, images)

    def error(self, image: bytes) -> None:
        self.errors([image])

    def criticals(self, images: List[bytes]) -> None:
        self.logs(logging.CRITICAL, images)

    def critical(self, image: bytes) -> None:
        self.criticals([image])

    def setLevel(self, level: _Level) -> None:
        self.__level = level
        self.__streamLogger.setLevel(level)

    def addHandler(self, handler: AbstractHandler) -> None:
        self.__handlers.append(handler)

    def removeHandler(self, handler: AbstractHandler) -> None:
        self.__handlers.remove(handler)

    def __imageExchangeBase64(self, image: bytes, format: str = 'PNG') -> str:
        inputStream = io.BytesIO(image)
        pillowImage = Image.open(inputStream)

        outputStream = io.BytesIO()
        pillowImage.save(outputStream, format=format)

        imageDecodedString = base64.b64encode(outputStream.getvalue()).decode('ascii')
        return imageDecodedString



class BaseImageLoggerFactory(AbstractImageLoggerFactory):

    __loggers = {}

    def __init__(self) -> None:
        pass

    def getLogger(self, name: str) -> AbstractImageLogger:
        if not name in BaseImageLoggerFactory.__loggers:
            logger = BaseImageLogger(name)
            BaseImageLoggerFactory.__loggers[name] = logger
        else:
            logger = BaseImageLoggerFactory[name]

        return logger