import csv
import io
import logging
from pathlib import Path
from typing import Union

from .handler import FileHandler


class CSVHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8') -> None:
        
        FileHandler.__init__(self, filename, encoding)

    def flush(self) -> None:
        csvString = self.csvString

        with open(self._filename, mode='w', encoding=self._encoding) as file:
            file.write(csvString)
            file.flush()

        self._records.clear()
        FileHandler.flush(self)


    @property
    def csvString(self) -> str:
        file = io.StringIO()
        writer = csv.writer(file, lineterminator='\n')

        writer.writerow(['id', 'name', 'time', 'level'])
        for record in self._records:
            writer.writerow([record.id, record.name, record.time, logging._levelToName[record.level]])

        recordCSV = file.getvalue()
        file.close()

        return recordCSV

    def close(self) -> None:
        FileHandler.close(self)