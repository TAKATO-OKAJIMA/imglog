import unittest

import numpy as np
from PIL import Image

from imglog.util import ImagePropertyExtractor
from imglog.record import ImageProperty
from .. import setting


class TestImagePropertyExtractor(unittest.TestCase):

    def setUp(self) -> None:
        self.extractor = ImagePropertyExtractor()
        self.image = Image.open(setting.VALID_IMAGE_PATH)
        self.arrayImage = np.array(self.image)
        self.bytesImage = self.image.tobytes()
        self.oracleProperty = ImageProperty() 

    def testExtractFromBytes(self):
        self.assertDictEqual(self.extractor.extract(self.bytesImage).toDict(),
                             self.oracleProperty.toDict())

    def testExtractFromArray(self):
        self.assertDictEqual(self.extractor.extract(self.arrayImage).toDict(),
                             self.oracleProperty.toDict())
    
    def testExtractFromPillowImage(self):
        self.assertDictEqual(self.extractor.extract(self.image).toDict(),
                             self.oracleProperty.toDict())