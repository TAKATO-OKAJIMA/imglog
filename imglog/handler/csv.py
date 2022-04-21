import csv
import io
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
        writer = csv.writer(file)

        writer.writerow(['id', 'time', 'level'])
        for record in self._records:
            writer.writerow([record.id, record.time, record.level])

        recordCSV = file.getvalue()
        file.close()

        return recordCSV

    def close(self) -> None:
        FileHandler.close(self)