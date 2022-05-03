import unittest

from imglog.logger import stream


class TestStreamModuleFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.root = 'root'

    def testGetLogger(self):
        logger = stream.getLogger(self.root)

        self.assertIs(logger, stream.getLogger(self.root))