import logging
from logging import _Level
from typing import List

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory
from ..util import ImageValidator, ImagePropertyExtractor


class BytesImageLogger(AbstractImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        self.__baseImageLogger = baseImageLogger
        self.__validator = ImageValidator()
        self.__extractor = ImagePropertyExtractor()

    def logs(self, level: int, images: List[bytes]) -> None:
        imagesProperty = list()

        for image in images:
            if self.__validator.valid(image):
                imagesProperty.append(self.__extractor.extract(image))

        self.__baseImageLogger.logs(level, images, imagesProperty)

    def log(self, level: int, image: bytes) -> None:
        self.logs(level, [image])

    def debugs(self, images: List[bytes]) -> None:
        self.logs(logging.DEBUG, images)

    def debug(self, image: bytes) -> None:
        self.debugs([image])

    def infos(self, images: List[bytes]) -> None:
        self.logs(logging.INFO, images)

    def info(self, image: bytes) -> None:
        self.infos([image])

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
        self.__baseImageLogger.setLevel(level)


class BytesImageLoggerFactory(AbstractImageLoggerFactory):

    __loggers = {}

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()

    def getLogger(self, name: str) -> AbstractImageLogger:
        if not name in BytesImageLoggerFactory.__loggers:
            logger = BytesImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            BytesImageLoggerFactory.__loggers[name] = logger
        else:
            logger = BytesImageLoggerFactory.__loggers[name]

        return logger