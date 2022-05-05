import unittest
import os, sys

try:
    from test_record import *
except ModuleNotFoundError:
    from test.test_record import *
try:
    from test import util, handler, logger
except ImportError:
    import util, handler, logger

path = os.path.join(os.path.dirname(__file__), '../')
sys.path.append(path)


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