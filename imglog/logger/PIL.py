from typing import List, Union

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class PillowImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(baseImageLogger)

    def log(self, level: int, image: Union[Image.Image, List[Image.Image]]) -> None:
        if isinstance(image, Image.Image):
            image = [image]

        bytesImages = list()
        imagesProperty = list()

        for img in image:
            if self._validator.valid(img):
                bytesImages.append(img.tobytes())
                imagesProperty.append(self._extractor.extract(img))
            else:
                invalidImage, invalidProperty = self._createInvalidImageObjectAndProperty()
                bytesImages.append(invalidImage)
                imagesProperty.append(invalidProperty)


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