from imglog.record import ImageLogRecord
from .abc import AbstractHandler


class HTMLHandler(AbstractHandler):

    def __init__(self) -> None:
        self.__records = list()

    def emit(self, record: ImageLogRecord) -> None:
        self.__records.append(record)

    def flush(self) -> None:
        pass