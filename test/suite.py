import unittest

from test.test_record import *
from test import util, handler, logger


def getSuite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    testCases = [
        unittest.makeSuite(TestImageProperty),
        unittest.makeSuite(TestImageLogRecord),
    ]

    suite.addTests(testCases)
    suite.addTests(util.testCases)
    suite.addTests(handler.testCases)
    suite.addTests(logger.testCases)

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = getSuite()

    runner.run(suite)