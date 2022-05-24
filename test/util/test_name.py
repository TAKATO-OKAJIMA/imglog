import unittest

from imglog.util import LoggerName


class TestLoggerName(unittest.TestCase):

    def setUp(self) -> None:
        self.loggerName = LoggerName('test.aaa.bbb')
        self.neLoggerName = LoggerName('test.aaa.ccc')

    def testInitialize(self):
        loggerName = LoggerName(['test', 'aaa', 'bbb'])
        self.assertEqual(self.loggerName, loggerName)

        self.assertNotEqual(self.loggerName, self.neLoggerName)

    def testParent(self):
        self.assertEqual(self.loggerName.parent, 
                         self.neLoggerName.parent)

    def testIsRoot(self):
        self.assertFalse(self.loggerName.isRoot)
        self.assertTrue(self.loggerName.parent.parent.parent.isRoot)

    