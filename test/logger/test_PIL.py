import logging
import unittest

from imglog.logger.PIL import PillowImageLogger, PillowImageLoggerFactory
from imglog.logger.base import BaseImageLogger

from .. import setting


class TestPillowImageLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'test'
        self.logger = PillowImageLogger(BaseImageLogger(self.name))
        self.testImage = setting.TEST_IMAGE
        self.testImages = [self.testImage for i in range(2)]

    def testLog(self):
        self.logger.log(logging.INFO, self.testImage)
        self.logger.log(logging.WARNING, self.testImages)

    def testDebug(self):
        self.logger.debug(self.testImage)
        self.logger.debug(self.testImages)

    def testINFO(self):
        self.logger.info(self.testImage)
        self.logger.info(self.testImages)

    def testWarning(self):
        self.logger.warning(self.testImage)
        self.logger.warning(self.testImages)

    def testError(self):
        self.logger.error(self.testImage)
        self.logger.error(self.testImages)

    def testCritical(self):
        self.logger.critical(self.testImage)
        self.logger.critical(self.testImages)

    def testGetEffectiveLevel(self):
        self.assertEqual(logging.NOTSET, self.logger.getEffectiveLevel())

        self.logger.setLevel(logging.INFO)
        self.assertEqual(logging.INFO, self.logger.getEffectiveLevel())
        


class TestPillowImageLoggerFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = PillowImageLoggerFactory()
        self.name = 'test'

    def testSingleton(self):
        self.assertIs(self.factory, PillowImageLoggerFactory())

    def testGetLogger(self):
        logger = self.factory.getLogger()

        self.assertIs(logger, self.factory.getLogger())
        self.assertIsNot(logger, self.factory.getLogger(self.name))