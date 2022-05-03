import unittest
import logging

from imglog.logger.base import BaseImageLogger, BaseImageLoggerFactory
from imglog.record import ImageProperty

from .. import setting


class TestBaseImageLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.name = 'base_test'
        self.logger = BaseImageLogger(self.name)
        self.testImage = setting.TEST_IMAGE.tobytes()
        self.testImages = [self.testImage for i in range(2)]

        self.testProperty = ImageProperty(0, 0, 0, 'RGB')
        self.testProperties = [self.testProperty for i in range(2)]

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