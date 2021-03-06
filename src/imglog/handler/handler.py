import logging
import os
from pathlib import Path
from typing import Union
# from logging import _Level

from ..record import ImageLogRecord
from ..util import _checkLevel

handlers = list()

def addHandlers(handler) -> None:
    if not handler in handlers:
        handlers.append(handler)


def close() -> None:
    [handler.close() for handler in handlers]


class Handler(object):

    def __init__(self,
                 level: Union[int, str] = logging.NOTSET) -> None:
        self._level = _checkLevel(level)
        
        handlers.append(self)

    def handle(self, record: ImageLogRecord) -> None:
        raise NotImplementedError

    def emit(self, record: ImageLogRecord) -> None:
        raise NotImplementedError

    def flush(self) -> None:
        raise NotImplementedError

    def close(self) -> None:
        del self._level

    def setLevel(self, level: int) -> None:
        self._level = _checkLevel(level)


class FileHandler(Handler):

    def __init__(self, 
                 filename: Union[str, Path],
                 encoding: str = 'utf-8',) -> None:
        filename = os.fspath(filename)

        self._records = list()
        self._filename = os.path.abspath(filename)
        self._encoding = encoding
        self._isFileFlushed = False
        
        Handler.__init__(self)

    def handle(self, record: ImageLogRecord) -> None:
        if record.level >= self._level:
            self.emit(record)

    def emit(self, record: ImageLogRecord) -> None:
        self._records.append(record)

    def flush(self) -> None:
        self._isFileFlushed = True

    @property
    def filename(self) -> str:
        return self._filename

    @filename.setter
    def filename(self, filename: Union[str, Path]) -> None:
        filename = os.fspath(filename)
        self._filename = os.path.abspath(filename)

    @property
    def isFileFlushed(self) -> bool:
        return self._isFileFlushed

    def close(self) -> None:
        if not self.isFileFlushed:
            self.flush()

        del self._records
        del self._filename
        del self._encoding

        Handler.close(self)