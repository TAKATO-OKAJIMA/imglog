from typing import List, Union

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class BytesImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(self, baseImageLogger)

    def log(self, level: int, image: Union[bytes, List[bytes]]) -> None:
        if isinstance(image, bytes):
            image = [image]

        imagesProperty = list()

        for img in image:
            if self._validator.valid(img):
                imagesProperty.append(self._extractor.extract(img))

        self._baseImageLogger.log(level, image, imagesProperty)

    def close(self) -> None:
        SurffaceImageLogger.close(self)


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