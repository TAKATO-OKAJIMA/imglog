from pathlib import Path
from typing import Union

from .handler import FileHandler


class HTMLHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8') -> None:
        FileHandler.__init__(filename, encoding)

    def flush(self) -> None:
        FileHandler.flush(self)

    @property
    def htmlString(self) -> str:
        pass

    def close(self) -> None:
        FileHandler.close(self)
