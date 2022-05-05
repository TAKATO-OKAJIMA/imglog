import io
from typing import List, Union

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory
from .base import BaseImageLogger, BaseImageLoggerFactory, SurffaceImageLogger


class PillowImageLogger(SurffaceImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        SurffaceImageLogger.__init__(self, baseImageLogger)

    def log(self, level: int, image: Union[Image.Image, List[Image.Image]]) -> None:
        if isinstance(image, Image.Image):
            image = [image]

        bytesImages = list()
        imagesProperty = list()

        for img in image:
            if self._validator.valid(img):
                inputStream = io.BytesIO()
                img.save(inputStream, format='PNG')
                bytesImages.append(inputStream.getvalue())
                imagesProperty.append(self._extractor.extract(img))
            else:
                invalidImage, invalidProperty = self._createInvalidImageObjectAndProperty()
                bytesImages.append(invalidImage)
                imagesProperty.append(invalidProperty)


        self._baseImageLogger.log(level, bytesImages, imagesProperty)

    def close(self) -> None:
        SurffaceImageLogger.close(self)


class PillowImageLoggerFactory(AbstractImageLoggerFactory):

    def __init__(self) -> None:
        self.__baseImageLoggerFactory = BaseImageLoggerFactory()
        AbstractImageLoggerFactory.__init__(self)

    def getLogger(self, name: str = 'root') -> PillowImageLogger:
        if not name in self._loggers:
            logger = PillowImageLogger(self.__baseImageLoggerFactory.getLogger(name))
            self._loggers[name] = logger
        else:
            logger = self._loggers[name]
        
        return logger