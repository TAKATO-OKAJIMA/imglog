import unittest

from .test_stream import TestStreamModuleFunctions
from .test_base import TestBaseImageLogger, TestBaseImageLoggerFactory
from .test_array import TestArrayImageLogger, TestArrayImageLoggerFactory
from .test_byte import TestBytesImageLogger, TestBytesImageLoggerFactory
from .test_PIL import TestPillowImageLogger, TestPillowImageLoggerFactory


testCases = [
    unittest.makeSuite(TestStreamModuleFunctions),
    unittest.makeSuite(TestBaseImageLogger),
    unittest.makeSuite(TestBaseImageLoggerFactory),
    unittest.makeSuite(TestArrayImageLogger),
    unittest.makeSuite(TestArrayImageLoggerFactory),
    unittest.makeSuite(TestBytesImageLogger),
    unittest.makeSuite(TestBytesImageLoggerFactory),
    unittest.makeSuite(TestPillowImageLogger),
    unittest.makeSuite(TestPillowImageLoggerFactory)
]