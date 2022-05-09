from pathlib import Path
from typing import Union

from .handler import Handler, FileHandler
from ..record import ImageLogRecord

MESSAGE_FORMAT = '[IMGLOG] | {record.time} | {record.levelName} | {record.id}'


class ConsoleHandler(Handler):

    def __init__(self) -> None:
        Handler.__init__(self)

    def handle(self, record: ImageLogRecord) -> None:
        print(MESSAGE_FORMAT.format(record=record))

    def close(self) -> None:
        Handler.close(self)


class LogFileHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path], 
                 encoding: str = 'utf-8',
                 terminator: str = '\n') -> None:
        self.__terminator = terminator
        FileHandler.__init__(self, filename, encoding)

    def flush(self) -> None:
        contents = [MESSAGE_FORMAT.format(record=record) + self.__terminator for record in self._records]

        with open(self._filename, 'w', encoding=self._encoding) as file:
            file.writelines(contents)
            file.flush()

        FileHandler.flush(self)

    def close(self) -> None:
        FileHandler.close(self)
        del self.__terminator