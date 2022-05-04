import unittest

from .test_creator import TestInvalidImageCreator
from .test_extract import TestImagePropertyExtractor
from .test_valid import TestImageValidator

testCases = [
    unittest.makeSuite(TestImagePropertyExtractor),
    unittest.makeSuite(TestImageValidator),
    unittest.makeSuite(TestInvalidImageCreator)
]