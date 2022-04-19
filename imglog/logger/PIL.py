import logging
from logging import _Level
from typing import List

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory
from ..util import ImageValidator, ImagePropertyExtractor


class PillowImageLogger(AbstractImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        self.__baseImageLogger = baseImageLogger
        self.__validator = ImageValidator()
        self.__extractor = ImagePropertyExtractor()

    def logs(self, level: int, images: List[Image.Image]) -> None:
        bytesImages = list()
        imagesProperty = list()

        for image in images:
            if self.__validator.valid(image):
                bytesImages.append(image.tobytes())
                imagesProperty.append(self.__extractor.extract(image))

        self.__baseImageLogger.logs(level, bytesImages, imagesProperty)

    def log(self, level: int, image: Image.Image) -> None:
        self.logs(level, [image])

    def debugs(self, images: List[Image.Image]) -> None:
        self.logs(logging.DEBUG, images)

    def debug(self, image: Image.Image) -> None:
        self.debugs([image])

    def infos(self, images: List[Image.Image]) -> None:
        self.logs(logging.INFO, images)

    def info(self, image: Image.Image) -> None:
        self.infos([image] )

    def warnings(self, images: List[Image.Image]) -> None:
        self.logs(logging.WARNING, images)

    def warning(self, image: Image.Image) -> None:
        self.warnings([image])

    def errors(self, images: List[Image.Image]) -> None:
        self.logs(logging.ERROR, images)

    def error(self, image: Image.Image) -> None:
        self.errors([image])

    def criticals(self, images: List[Image.Image]) -> None:
        self.logs(logging.CRITICAL, images)

    def critical(self, image: Image.Image) -> None:
        self.criticals([image])

    def setLevel(self, level: _Level) -> None:
        self.__baseImageLogger.setLevel(level)


class PillowImageLoggerFactory(AbstractImageLoggerFactory):

    __loggers = {}

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()

    def getLogger(self, name: str) -> AbstractImageLogger:
        if not name in PillowImageLoggerFactory.__loggers:
            logger = PillowImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            PillowImageLoggerFactory.__loggers[name] = logger
        else:
            logger = PillowImageLoggerFactory.__loggers[name]
        
        return logger