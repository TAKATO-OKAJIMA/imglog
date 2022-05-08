import io
import unittest
import logging

from imglog.logger.base import BaseImageLogger, BaseImageLoggerFactory
from imglog.record import ImageProperty
from imglog.handler import HTMLHandler, XMLHandler, CSVHandler, JSONHandler, LogFileHandler, ConsoleHandler

from .. import setting



class TestBaseImageLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'test'
        self.logger = BaseImageLogger(self.name)
        self.testImage = setting.TEST_BYTE_IMAGE
        self.testImages = [self.testImage for i in range(2)]

        self.testProperty = ImageProperty(0, 0, 0, 'RGB')
        self.testProperties = [self.testProperty for i in range(2)]
        self.testProperty = [self.testProperty]

        consoleHandler = ConsoleHandler()
        htmlHandler = HTMLHandler(setting.OUTPUT_HTML)
        jsonHandler = JSONHandler(setting.OUTPUT_JSON)
        xmlHandler = XMLHandler(setting.OUTPUT_XML)
        csvHandler = CSVHandler(setting.OUTPUT_CSV)
        logFileHandler = LogFileHandler(setting.OUTPUT_LOG)

        self.logger.addHandler(consoleHandler)
        self.logger.addHandler(htmlHandler)
        self.logger.addHandler(jsonHandler)
        self.logger.addHandler(xmlHandler)
        self.logger.addHandler(csvHandler)
        self.logger.addHandler(logFileHandler)

        self.logger.setLevel(logging.DEBUG)

    def testLog(self):
        self.logger.log(logging.INFO, self.testImage, self.testProperty)
        self.logger.log(logging.WARNING, self.testImages, self.testProperties)

    def testDebug(self):
        self.logger.debug(self.testImage, self.testProperty)
        self.logger.debug(self.testImages, self.testProperties)

    def testINFO(self):
        self.logger.info(self.testImage, self.testProperty)
        self.logger.info(self.testImages, self.testProperties)

    def testWarning(self):
        self.logger.warning(self.testImage, self.testProperty)
        self.logger.warning(self.testImages, self.testProperties)

    def testError(self):
        self.logger.error(self.testImage, self.testProperty)
        self.logger.error(self.testImages, self.testProperties)

    def testCritical(self):
        self.logger.critical(self.testImage, self.testProperty)
        self.logger.critical(self.testImages, self.testProperties)

    def testGetEffectiveLevel(self):
        self.assertEqual(logging.DEBUG, self.logger.getEffectiveLevel())

        self.logger.setLevel(logging.INFO)
        self.assertEqual(logging.INFO, self.logger.getEffectiveLevel())


class TestBaseImageLoggerFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = BaseImageLoggerFactory()
        self.name = 'test'
    
    def testSingleton(self):
        self.assertIs(self.factory, BaseImageLoggerFactory())

    def testGetLogger(self):
        logger = self.factory.getLogger()

        self.assertIs(logger, self.factory.getLogger())
        self.assertIsNot(logger, self.factory.getLogger(self.name))