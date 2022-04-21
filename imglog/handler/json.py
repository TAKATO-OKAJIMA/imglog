import json
from pathlib import Path
from typing import Union

from .handler import FileHandler


class JSONHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8',
                 indent: int = 4) -> None:
        self.__indent = indent
        
        FileHandler.__init__(self, filename, encoding)

    def flush(self) -> None:
        jsonString = self.jsonString
        
        with open(self._filename, mode='w', encoding=self._encoding) as file:
            file.write(jsonString)
            file.flush()
        
        self._records.clear()

        FileHandler.flush(self)

    @property
    def jsonString(self) -> str:
        '''
        This property obtains the JSON String of the record held by this JSONHandler.
        Caution: the records are not flushed.
        '''
        recordDict = [record.toDict() for record in self._records]
        return json.dumps(recordDict, indent=self.__indent)

    def close(self) -> None:
        del self.__indent

        FileHandler.close(self)