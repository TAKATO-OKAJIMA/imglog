from abc import ABCMeta, abstractmethod
from typing import Any, List

AnyImageObject = Any

class AbstractImageLogger(metacalss=ABCMeta):

    @abstractmethod
    def logs(self, level: int, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def log(self, level: int, image: AnyImageObject) -> None:
        pass

    @abstractmethod
    def debugs(self, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def debug(self, image: AnyImageObject) -> None:
        pass

    @abstractmethod
    def infos(self, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def info(self, image: AnyImageObject) -> None:
        pass

    @abstractmethod
    def warnings(self, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def warning(self, image: AnyImageObject) -> None:
        pass

    @abstractmethod
    def errors(self, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def error(self, image: AnyImageObject) -> None:
        pass
    
    @abstractmethod
    def criticals(self, images: List[AnyImageObject]) -> None:
        pass

    @abstractmethod
    def critical(self, image: AnyImageObject) -> None:
        pass


class AbstractImageLoggerFactory(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def getLogger(self, name: str) -> AbstractImageLogger:
        pass
    