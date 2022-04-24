from pathlib import Path
from typing import Union

from .handler import FileHandler
from ..util import LogFileElement


class HTMLHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8') -> None:
        FileHandler.__init__(filename, encoding)

    def flush(self) -> None:
        htmlString = self.htmlString

        with open(self._filename, 'w', encoding=self._encoding) as file:
            file.write(htmlString)
            file.flush()

        FileHandler.flush(self)

    @property
    def htmlString(self) -> str:
        return LogFileElement(self._records).render()

    def close(self) -> None:
        if not self.isFileFlushed:
            self.flush()

        FileHandler.close(self)
