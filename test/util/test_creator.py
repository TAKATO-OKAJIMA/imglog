import unittest

from PIL import Image

from imglog.util import InvalidImageCreator
from .. import setting

TEST_WIDTH = 400
TEST_HEIGHT = 300
TEST_SIZE = (TEST_WIDTH, TEST_HEIGHT)


class TestInvalidImageCreator(unittest.TestCase):

    def setUp(self) -> None:
        self.creator = InvalidImageCreator()

    def testCreateFromInt(self):
        invalidImage = self.creator.create(TEST_WIDTH, TEST_HEIGHT)
        self.assertIsInstance(invalidImage, bytes)
        
        self.writeImage(invalidImage, setting.OUTPUT_CREATED_IMAGE)

    def testCreateFromTuple(self):
        invalidImage = self.creator.create(TEST_SIZE)
        self.assertIsInstance(invalidImage, bytes)

        self.writeImage(invalidImage, setting.OUTPUT_CREATED_IMAGE_FROM_TUPLE)

    def testCreateFromDefaultParameters(self):
        invalidImage = self.creator.createFromDefaultParameters()
        self.assertIsInstance(invalidImage, bytes)

        self.writeImage(invalidImage, setting.OUTPUT_CREATED_IMAGE_FROM_DEFAULT_PARAMS)
       
    def writeImage(self, image: bytes, path: str):
         with open(path, 'wb') as file:
            file.write(image)

        

    