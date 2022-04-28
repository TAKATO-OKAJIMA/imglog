from typing import List, Union

from numpy import ndarray
from PIL import Image

from .abc import AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class ArrayImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(self, baseImageLogger)

    def log(self, level: int, image: Union[ndarray, List[ndarray]]) -> None:
        if isinstance(image, ndarray):
            image = [image]

        bytesImages = list()
        imagesProperty = list()

        for img in image:
            if self._validator.valid(img):
                pillowImage = Image.fromarray(img)
                bytesImages.append(pillowImage.tobytes())
                imagesProperty.append(self._extractor.extract(pillowImage))
            else:
                invalidImage, invalidProperty = self._createInvalidImageObjectAndProperty()
                bytesImages.append(invalidImage)
                imagesProperty.append(invalidProperty)

        self._baseImageLogger.log(level, bytesImages, imagesProperty)

    def close(self) -> None:
        SurffaceImageLogger.close(self)


class ArrayImageLoggerFactory(AbstractImageLoggerFactory):

    __loggers = {}

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()

    def getLogger(self, name: str) -> ArrayImageLogger:
        if not name in ArrayImageLoggerFactory.__loggers:
            logger = ArrayImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            ArrayImageLoggerFactory.__loggers[name] = logger
        else:
            logger = ArrayImageLoggerFactory.__loggers[name]

        return logger