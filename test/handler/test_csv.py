from calendar import c
import unittest

from imglog.handler import CSVHandler
from imglog.record import ImageLogRecord

from .. import setting


class TestCSVHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = CSVHandler()
        self.record = ImageLogRecord()