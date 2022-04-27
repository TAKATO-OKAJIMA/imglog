from abc import ABCMeta, abstractmethod
import logging
from typing import Any, List, Union
from logging import _Level

from ..handler import Handler

AnyImageObject = Any


class AbstractImageLogger(metaclass=ABCMeta):

    @abstractmethod
    def log(self, level: int, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        pass

    def debug(self, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        self.log(logging.DEBUG, image)

    def info(self, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        self.log(logging.INFO, image)

    def warning(self, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        self.log(logging.WARNING, image)
 
    def error(self, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        self.log(logging.ERROR, image)

    def critical(self, image: Union[AnyImageObject, List[AnyImageObject]]) -> None:
        self.log(logging.CRITICAL, image)

    @abstractmethod
    def getEffectiveLevel(self) -> int:
        pass

    @abstractmethod
    def setLevel(self, level: _Level) -> None:
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

    def __init__(self) -> None:
        pass

    @abstractmethod
    def getLogger(self, name: str) -> AbstractImageLogger:
        pass
    