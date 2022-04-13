from abc import ABCMeta, abstractmethod


class AbstractHandler(metaclass=ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractmethod
    def emit(self, record) -> None:
        pass

    @abstractmethod
    def flush(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass