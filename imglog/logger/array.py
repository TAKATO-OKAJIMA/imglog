from typing import List

from numpy import ndarray

from .abc import AbstractImageLogger


class ArrayImageLogger(AbstractImageLogger):

    def __init__(self) -> None:
        pass

    def logs(self, level: int, images: List[ndarray], msg: str) -> None:
        pass

    def log(self, level: int, image: ndarray, msg: str) -> None:
        pass

    def debugs(self, images: List[ndarray], msg: str) -> None:
        pass

    def debug(self, image: ndarray, msg: str) -> None:
        pass

    def infos(self, images: List[ndarray], msg: str) -> None:
        pass

    def info(self, image: ndarray, msg: str) -> None:
        pass

    def warnings(self, images: List[ndarray], msg: str) -> None:
        pass

    def warning(self, image: ndarray, msg: str) -> None:
        pass

    def errors(self, images: List[ndarray], msg: str) -> None:
        pass

    def error(self, image: ndarray, msg: str) -> None:
        pass

    def criticals(self, images: List[ndarray], msg: str) -> None:
        pass

    def critical(self, image: ndarray, msg: str) -> None:
        pass