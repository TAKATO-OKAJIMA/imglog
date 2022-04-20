import csv
import io
import os
from pathlib import Path
from typing import Union

from .abc import AbstractHandler
from ..record import ImageLogRecord


class CSVHandler(AbstractHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8') -> None:
        
        filename = os.fspath(filename)

        self.__records = list()
        self.__filename = os.path.abspath(filename)
        self.__encoding = encoding
    
    def emit(self, record: ImageLogRecord) -> None:
        self.__records.append(record)

    def flush(self) -> None:
        csvString = self.csvString

        with open(self.__filename, mode='w', encoding=self.__encoding) as file:
            file.write(csvString)
            file.flush()

        self.__records.clear()

    @property
    def csvString(self) -> str:
        file = io.StringIO()
        writer = csv.writer(file)

        writer.writerow(['id', 'time', 'level'])
        for record in self.__records:
            writer.writerow([record.id, record.time, record.level])

        recordCSV = file.getvalue()
        file.close()

        return recordCSV


    def close(self) -> None:
        del self.__records
        del self.__filename
        del self.__encoding