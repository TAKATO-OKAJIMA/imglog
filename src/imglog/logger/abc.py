import logging
import threading
from abc import ABCMeta, abstractmethod
from typing import Any, List, Union
# from logging import _Level, Ll

from ..handler import Handler

ClassSupportImageType = Any


class AbstractImageLogger(metaclass=ABCMeta):

    @abstractmethod
    def log(self, level: int, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        pass

    def debug(self, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        self.log(logging.DEBUG, image)

    def info(self, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        self.log(logging.INFO, image)

    def warning(self, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        self.log(logging.WARNING, image)
 
    def error(self, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        self.log(logging.ERROR, image)

    def critical(self, image: Union[ClassSupportImageType, List[ClassSupportImageType]]) -> None:
        self.log(logging.CRITICAL, image)

    @abstractmethod
    def getEffectiveLevel(self) -> int:
        pass

    @abstractmethod
    def setLevel(self, level: int) -> None:
        pass

    @abstractmethod
    def addHandler(self, handler: Handler) -> None:
        pass

    @abstractmethod
    def removeHandler(self, handler: Handler) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class AbstractImageLoggerFactory(metaclass=ABCMeta):
    __instance = None
    __lock = threading.Lock()

    def __init__(self) -> None:
        self._loggers = dict()

    @abstractmethod
    def getLogger(self, name: str = 'root') -> AbstractImageLogger:
        pass

    def close(self) -> None:
        [logger.close() for logger in self._loggers.values()]
        del self._loggers
    
    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)

        return cls.__instance