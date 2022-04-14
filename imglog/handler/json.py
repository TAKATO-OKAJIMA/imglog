import imp
import json
from textwrap import indent

from .abc import AbstractHandler
from ..record import ImageLogRecord

class JSONHandler(AbstractHandler):

    def __init__(self,
                 filename: str,
                 encoding: str = 'utf-8',
                 indent: int = 4) -> None:
        self.__records = list()
        self.__filename = filename
        self.__encoding = encoding
        self.__indent = indent

    def emit(self, record: ImageLogRecord) -> None:
        self.__records.append(record)

    def flush(self) -> None:
        jsonString = self.jsonString
        
        with open(self.__filename, mode='w', encoding=self.__encoding) as file:
            file.write(jsonString)

        self.__records.clear()

    @property
    def jsonString(self) -> str:
        '''
        This property obtains the JSON String of the record held by the Handler.
        Caution: the records are not flushed.
        '''
        recordDict = [record.toDict() for record in self.__records]
        return json.dumps(recordDict, indent=self.__indent)

    def close(self) -> None:
        del self.__records
        del self.__filename
        del self.__encoding