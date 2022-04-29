from typing import List, Union

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class BytesImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(self, baseImageLogger)

    def log(self, level: int, image: Union[bytes, List[bytes]]) -> None:
        if isinstance(image, bytes):
            image = [image]

        inputImages = list()
        imagesProperty = list()

        for img in image:
            if self._validator.valid(img):
                inputImages.append(img)
                imagesProperty.append(self._extractor.extract(img))
            else:
                invalidImage, invalidProperty = self._createInvalidImageObjectAndProperty()
                inputImages.append(invalidImage)
                imagesProperty.append(invalidProperty)

        self._baseImageLogger.log(level, inputImages, imagesProperty)

    def close(self) -> None:
        SurffaceImageLogger.close(self)


class BytesImageLoggerFactory(AbstractImageLoggerFactory):

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()
        AbstractImageLoggerFactory.__init__(self)

    def getLogger(self, name: str) -> BytesImageLogger:
        if not name in self._loggers:
            logger = BytesImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            self._loggers[name] = logger
        else:
            logger = self._loggers[name]

        return logger