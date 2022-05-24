import base64
import io
import logging
from traceback import print_stack
from typing import List, Optional, Union, Tuple

from PIL import Image

from .abc import AbstractImageLogger, AbstractImageLoggerFactory, ClassSupportImageType
from ..record import ImageLogRecord, ImageProperty
from ..handler import Handler
from ..util import _checkLevel, ImagePropertyExtractor, ImageValidator, InvalidImageCreator, LoggerName


class BaseImageLogger(AbstractImageLogger):

    def __init__(self, 
                 name: str,
                 propagate: bool = True) -> None:
        self.__name = name
        self.__propagate = propagate
        self.__parent = None
        self.__handlers = list()
        self.__level = logging.WARNING

    def log(self, level: int, image: Union[bytes, List[bytes]], imagesProperty: List[ImageProperty]) -> None:
        if isinstance(image, bytes):
            image = [image]

        if level >= self.__level:
            record = ImageLogRecord(
                                    self.__name,
                                    level,
                                    [self.__imageExchangeBase64(img) for img in image],
                                    imagesProperty
                                    )

            self.handle(record)

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

    def handle(self, record: ImageLogRecord) -> None:
        for handler in self.__handlers:
                handler.handle(record)

        if self.__propagate and not self.__parent is None:
            self.__parent.handle(record)


    def getEffectiveLevel(self) -> int:
        return self.__level
    
    def setLevel(self, level: int) -> None:
        self.__level = _checkLevel(level)

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

    @property
    def name(self) -> str:
        return self.__name

    @property
    def propagate(self) -> bool:
        return self.__propagate

    @propagate.setter
    def propagate(self, value) -> None:
        try :
            self.__propagate = bool(value)
        except TypeError as e:
            print(e)

    @property
    def parent(self) -> Optional['BaseImageLogger']:
        return self.__parent

    @parent.setter
    def parent(self, value: 'BaseImageLogger') -> None:
        if not isinstance(value, BaseImageLogger):
            raise TypeError
        if LoggerName(self.__name).parent != LoggerName(value.name):
            raise ValueError

        self.__parent = value

    def close(self) -> None:
        del self.__name
        del self.__propagate
        del self.__parent
        del self.__handlers
        del self.__level


class BaseImageLoggerFactory(AbstractImageLoggerFactory):

    def __init__(self) -> None:
        AbstractImageLoggerFactory.__init__(self)
        self.getLogger()

    def getLogger(self, name: str = 'root') -> BaseImageLogger:
        if not name in self._loggers:
            logger = BaseImageLogger(name)
            self._loggers[name] = logger

            loggerName = LoggerName(logger.name)

            if (not loggerName.isRoot) and logger.parent is None:
                logger.parent = self.getLogger(str(loggerName.parent))
        else:
            logger = self._loggers[name]

        return logger


class SurffaceImageLogger(AbstractImageLogger):

    def __init__(self, 
                 baseImageLogger: BaseImageLogger,
                 **kwargs) -> None:
        self._baseImageLogger = baseImageLogger
        self._validator = kwargs.get('validator', ImageValidator())
        self._extractor = kwargs.get('extractor', ImagePropertyExtractor())
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