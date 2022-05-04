import unittest

from .test_csv import TestCSVHandler
from .test_html import TestHTMLHandler
from .test_json import TestJSONHandler
from .test_xml import TestXMLHandler


testCases = [
    unittest.makeSuite(TestCSVHandler),
    unittest.makeSuite(TestHTMLHandler),
    unittest.makeSuite(TestJSONHandler),
    unittest.makeSuite(TestXMLHandler)
]