import logging
from logging import _Level
from typing import List

from numpy import ndarray
from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory
from ..util import ImageValidator, ImagePropertyExtractor

class ArrayImageLogger(AbstractImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        self.__baseImageLogger = baseImageLogger
        self.__validator = ImageValidator()
        self.__extractor = ImagePropertyExtractor()

    def logs(self, level: int, images: List[ndarray]) -> None:
        bytesImages = list()
        imagesProperty = list()

        for image in images:
            if self.__validator.valid(image):
                pillowImage = Image.fromarray(image)
                bytesImages.append(pillowImage.tobytes())
                imagesProperty.append(self.__extractor.extract(pillowImage))

        self.__baseImageLogger.logs(level, bytesImages, imagesProperty)

    def log(self, level: int, image: ndarray) -> None:
        self.logs(level, [image])

    def debugs(self, images: List[ndarray]) -> None:
        self.logs(logging.DEBUG, images)

    def debug(self, image: ndarray) -> None:
        self.debugs([image])

    def infos(self, images: List[ndarray]) -> None:
        self.logs(logging.INFO, images)

    def info(self, image: ndarray) -> None:
        self.infos([image] )

    def warnings(self, images: List[ndarray]) -> None:
        self.logs(logging.WARNING, images)

    def warning(self, image: ndarray) -> None:
        self.warnings([image])

    def errors(self, images: List[ndarray]) -> None:
        self.logs(logging.ERROR, images)

    def error(self, image: ndarray) -> None:
        self.errors([image])

    def criticals(self, images: List[ndarray]) -> None:
        self.logs(logging.CRITICAL, images)

    def critical(self, image: ndarray) -> None:
        self.criticals([image])

    def setLevel(self, level: _Level) -> None:
        self.__baseImageLogger.setLevel(level)


class ArrayImageLoggerFactory(AbstractImageLoggerFactory):

    __loggers = {}

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()

    def getLogger(self, name: str) -> AbstractImageLogger:
        if not name in ArrayImageLoggerFactory.__loggers:
            logger = ArrayImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            ArrayImageLoggerFactory.__loggers[name] = logger
        else:
            logger = ArrayImageLoggerFactory.__loggers[name]

        return logger