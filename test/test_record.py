import logging
from turtle import width
import unittest

from imglog.record import ImageProperty, ImageLogRecord, INVALID_PROPERTY

TEST_WIDTH = 5
TEST_HEIGHT = 5
TEST_CHANNEL = 3
TEST_MODE = 3

__all__ = [
    'TestImageProperty',
    'TestImageLogRecord'
]


class TestImageProperty(unittest.TestCase):

    def setUp(self) -> None:
        self.imageProperty = ImageProperty(TEST_WIDTH, TEST_HEIGHT, TEST_CHANNEL, TEST_MODE)

    def testWidth(self):
        self.assertEqual(TEST_WIDTH, self.imageProperty.width)
    
    def testHeight(self):
        self.assertEqual(TEST_HEIGHT, self.imageProperty.height)

    def testChannel(self):
        self.assertEqual(TEST_CHANNEL, self.imageProperty.channel)

    def testMode(self):
        self.assertEqual(TEST_MODE, self.imageProperty.mode)

    def testToDict(self):
        d = {
            'width': TEST_WIDTH,
            'height': TEST_HEIGHT,
            'channel': TEST_CHANNEL,
            'mode': TEST_MODE
        }

        self.assertDictEqual(d, self.imageProperty.toDict())
    
    def textInitializedInvalidProperty(self):
        invalidPropertyDictionary = {key:value 
                                     for key, value 
                                     in zip(
                                            self.imageProperty.toDict().keys(), 
                                            INVALID_PROPERTY
                                            )
                                    }

        invalidProperty = ImageProperty.initializeInvalidProperty()

        self.assertDictEqual(invalidPropertyDictionary, invalidProperty.toDict())


class TestImageLogRecord(unittest.TestCase):

    def setUp(self) -> None:
        self.image = ['aaa', 'bbb']
        self.property = [ImageProperty(TEST_WIDTH, TEST_HEIGHT, TEST_CHANNEL, TEST_MODE)]

        self.record = ImageLogRecord(logging.INFO, self.image, self.property)

    def testId(self):
        self.assertIsInstance(self.record.id, str)

    def testTime(self):
        self.assertIsInstance(self.record.time, str)

    def testLevel(self):
        self.assertEqual(logging.INFO, self.record.level)

    def testImages(self):
        self.assertListEqual(self.image, self.record.images)

    def testImagesProperty(self):
        self.assertListEqual(self.property, self.record.imagesProperty)

    def testToDict(self):
        self.assertIsInstance(self.record.toDict(), dict)

