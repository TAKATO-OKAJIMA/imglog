import atexit
from email.mime import image
import logging
from logging import _Level
from typing import List

from .abc import AbstractImageLogger
from .stream import getLogger

class BytesImageLogger(AbstractImageLogger):

    def __init__(self, name: str) -> None:
        self.__streamLogger = getLogger(name)
        self.__logRecords = list() 
        atexit.register(self.dump)

    def logs(self, level: int, images: List[bytes], msg: str) -> None:
        self.__streamLogger.log(level)

    def log(self, level: int, image: bytes, msg: str) -> None:
        self.logs(level, [image], msg)

    def debugs(self, images: List[bytes], msg: str) -> None:
        self.logs(logging.DEBUG, images, msg)

    def debug(self, image: bytes, msg: str) -> None:
        self.debugs([image], msg)

    def infos(self, images: List[bytes], msg: str) -> None:
        self.logs(images, msg)

    def info(self, image: bytes, msg: str) -> None:
        self.infos([image] , msg)

    def warnings(self, images: List[bytes], msg: str) -> None:
        self.logs(logging.WARNING, images, msg)
    
    def warning(self, image: bytes, msg: str) -> None:
        self.warnings([image], msg)

    def errors(self, images: List[bytes], msg: str) -> None:
        self.logs(logging.ERROR, images, msg)

    def error(self, image: bytes, msg: str) -> None:
        self.errors([image], msg)

    def criticals(self, images: List[bytes], msg: str) -> None:
        self.logs(logging.CRITICAL, images, msg)

    def critical(self, image: bytes, msg: str) -> None:
        self.criticals([image], msg)

    def setLevel(self, level: _Level) -> None:
        self.__streamLogger.setLevel(level)

    def dump(self) -> None:
        pass

    def dumps(self) -> str:
        pass
    
