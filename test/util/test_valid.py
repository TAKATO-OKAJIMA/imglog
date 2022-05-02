import unittest

import numpy as np
from PIL import Image

from imglog.util.valid import ImageValidator
from .. import setting


class TestImageValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.validator = ImageValidator()
        self.image = Image.open(setting.VALID_IMAGE_PATH)
        self.arrayImage = np.array(self.image)
        self.bytesImage = self.image.tobytes()

    def testValidFromBytes(self):
        self.assertTrue(self.validator.valid(self.bytesImage))

    def testValidFromArray(self):
        self.assertTrue(self.validator.valid(self.arrayImage))

    def testValidFromPillow(self):
        self.assertTrue(self.validator.valid(True))

    def testInvalidFromArray(self):
        invalidArrayImage = self.arrayImage[-5:3, 0:-1]
        self.assertFalse(self.validator.valid(invalidArrayImage))