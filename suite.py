import unittest
import os, sys

path = os.path.join(os.path.dirname(__file__), './src')
sys.path.append(path)

try:
    from test_record import *
except ModuleNotFoundError:
    from test.test_record import *
try:
    from test import util, handler, logger
except ImportError:
    import util, handler, logger


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
    with open('./output/test_result.log', 'w', encoding='utf-8') as file: 
        runner = unittest.TextTestRunner(verbosity=2)
        suite = getSuite()
        runner.run(suite)