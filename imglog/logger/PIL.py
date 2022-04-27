from typing import List, Union

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class PillowImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(baseImageLogger)

    def log(self, level: int, images: Union[Image.Image, List[Image.Image]]) -> None:
        if isinstance(images, Image.Image):
            images = [images]

        bytesImages = list()
        imagesProperty = list()

        for image in images:
            if self._validator.valid(image):
                bytesImages.append(image.tobytes())
                imagesProperty.append(self._extractor.extract(image))

        self._baseImageLogger.log(level, bytesImages, imagesProperty)

    def close(self) -> None:
        SurffaceImageLogger.close(self)


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