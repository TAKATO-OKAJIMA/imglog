import unittest
import logging

from imglog.handler import CSVHandler
from imglog.record import ImageLogRecord
from imglog.util import ImagePropertyExtractor

from .. import setting


class TestCSVHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = CSVHandler(setting.OUTPUT_CSV)
        self.extractor = ImagePropertyExtractor()

        self.properties = [self.extractor.extract(image)
                           for image in setting.HANDLER_TEST_IMAGE]

        self.infoRecord = ImageLogRecord(
                                        setting.NAME,
                                        logging.INFO,
                                        setting.HANDLER_TEST_BASE64_IMAGE,
                                        self.properties)

        self.waningRecord = ImageLogRecord(
                                           setting.NAME,
                                           logging.WARNING,
                                           setting.HANDLER_TEST_BASE64_IMAGE,
                                           self.properties)

    def testHandle(self):
        self.handler.handle(self.infoRecord)
        self.assertTrue(True)

    def testEmit(self):
        self.handler.emit(self.infoRecord)
        self.assertTrue(True)
        
    def testFlush(self):
        self.handler.handle(self.infoRecord)
        self.handler.handle(self.waningRecord)

        self.handler.flush()
        self.assertTrue(True)
        self.assertTrue(self.handler.isFileFlushed)

    def testFilename(self):
        self.assertEqual(self.handler.filename, setting.OUTPUT_CSV)

    