import base64
import io
import logging
from typing import List, Union, Tuple

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory, ClassSupportImageType
from .stream import getLogger
from ..record import ImageLogRecord, ImageProperty
from ..handler import Handler
from ..util import _checkLevel, ImagePropertyExtractor, ImageValidator, InvalidImageCreator


class BaseImageLogger(AbstractImageLogger):

    def __init__(self, name: str) -> None:
        self.__name = name
        # self.__streamLogger = getLogger(name)
        self.__handlers = list()
        self.__level = logging.WARNING

    def log(self, level: int, image: Union[bytes, List[bytes]], imagesProperty: List[ImageProperty]) -> None:
        if isinstance(image, bytes):
            image = [image]

        if level >= self.__level:
            record = ImageLogRecord(level,
                                    [self.__imageExchangeBase64(img) for img in image],
                                    imagesProperty
                                    )
            
            # self.__streamLogger.log(level, record.id)

            for handler in self.__handlers:
                handler.emit(record)

    def debug(self, 
              image: Union[ClassSupportImageType, List[ClassSupportImageType]],
              imagesProperty: List[ImageProperty]) -> None:
        return self.log(logging.DEBUG, image, imagesProperty)

    def info(self, 
             image: Union[ClassSupportImageType, List[ClassSupportImageType]],
             imagesProperty: List[ImageProperty]) -> None:
        return self.log(logging.INFO, image, imagesProperty)

    def warning(self, 
                image: Union[ClassSupportImageType, List[ClassSupportImageType]],
                imagesProperty: List[ImageProperty]) -> None:
        return self.log(logging.WARNING, image, imagesProperty)

    def error(self, 
              image: Union[ClassSupportImageType, List[ClassSupportImageType]],
              imagesProperty: List[ImageProperty]) -> None:
        return self.log(logging.ERROR, image, imagesProperty)

    def critical(self, 
                 image: Union[ClassSupportImageType, List[ClassSupportImageType]],
                 imagesProperty: List[ImageProperty]) -> None:
        return self.log(logging.CRITICAL, image, imagesProperty)

    def getEffectiveLevel(self) -> int:
        return self.__level
    
    def setLevel(self, level: int) -> None:
        self.__level = _checkLevel(level)
        # self.__streamLogger.setLevel(self.__level)

    def addHandler(self, handler: Handler) -> None:
        if not handler in self.__handlers:
            self.__handlers.append(handler)

    def removeHandler(self, handler: Handler) -> None:
        if handler in self.__handlers:
            self.__handlers.remove(handler)

    def __imageExchangeBase64(self, image: bytes, format: str = 'PNG') -> str:
        inputStream = io.BytesIO(image)
        pillowImage = Image.open(inputStream)

        outputStream = io.BytesIO()
        pillowImage.save(outputStream, format=format)

        imageDecodedString = base64.b64encode(outputStream.getvalue()).decode('ascii')
        return imageDecodedString

    def close(self) -> None:
        # del self.__streamLogger
        del self.__handlers
        del self.__level


class BaseImageLoggerFactory(AbstractImageLoggerFactory):

    def __init__(self) -> None:
        AbstractImageLoggerFactory.__init__(self)

    def getLogger(self, name: str = 'root') -> BaseImageLogger:
        if not name in self._loggers:
            logger = BaseImageLogger(name)
            self._loggers[name] = logger
        else:
            logger = self._loggers[name]

        return logger


class SurffaceImageLogger(AbstractImageLogger):

    def __init__(self, baseImageLogger: BaseImageLogger) -> None:
        self._baseImageLogger = baseImageLogger
        self._validator = ImageValidator()
        self._extractor = ImagePropertyExtractor()
        self._creator = InvalidImageCreator()

    def getEffectiveLevel(self) -> int:
        return self._baseImageLogger.getEffectiveLevel()

    def setLevel(self, level: int) -> None:
        self._baseImageLogger.setLevel(level)

    def addHandler(self, handler: Handler) -> None:
        self._baseImageLogger.addHandler(handler)

    def removeHandler(self, handler: Handler) -> None:
        self._baseImageLogger.removeHandler(handler)

    def _createInvalidImageObjectAndProperty(self) -> Tuple[bytes, ImageProperty]:
        imageObject = self._creator.createFromDefaultParameters()
        imageProperty = ImageProperty.initializeInvalidProperty()

        return imageObject, imageProperty

    def close(self) -> None:
        del self._validator
        del self._extractor
        del self._creator