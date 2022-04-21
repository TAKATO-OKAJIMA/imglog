import logging
import os
from pathlib import Path
from typing import Union
from logging import _Level

from ..record import ImageLogRecord


class Handler(object):

    def __init__(self,
                 level: Union[int, str] = logging.NOTSET) -> None:
        self._level = level

    def emit(self, record: ImageLogRecord) -> None:
        pass

    def flush(self) -> None:
        pass

    def close(self) -> None:
        del self._level

    def setLevel(self, level: _Level) -> None:
        self._level = level


class FileHandler(Handler):

    def __init__(self, 
                 filename: Union[str, Path],
                 encoding: str = 'utf-8',) -> None:
        filename = os.fspath(filename)

        self._records = list()
        self._filename = os.path.abspath(filename)
        self._encoding = encoding
        
        FileHandler.__init__(self)

    def emit(self, record: ImageLogRecord) -> None:
        if record.level >= self._level:
            self.__records.append(record)

    def close(self) -> None:
        del self._records
        del self._filename
        del self._encoding

        FileHandler.close(self)
