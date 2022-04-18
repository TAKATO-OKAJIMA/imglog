from io import BytesIO
from typing import overload, Union

from numpy import ndarray
from PIL import Image


MIN_IMAGE_SIZE = 0

class ImageValidator(object):

    def __init__(self) -> None:
        pass

    @overload
    def valid(self, image: bytes) -> bool:
        ...

    @overload
    def valid(self, image: ndarray) -> bool:
        ...

    @overload
    def valid(self, image: Image.Image) -> bool:
        ...

    def valid(self, image: Union[bytes, ndarray, Image.Image]) -> bool:
        if isinstance(image, bytes):
            return self.__validFromBytes(image)
        elif isinstance(image, ndarray):
            return self.__validFromArray(image)
        elif isinstance(image, Image.Image):
            return self.__validFromPillowImage
        else:
            return False

    def __validFromBytes(self, image: bytes) -> bool:
        pillowImage = Image.open(BytesIO(image))
        return self.__validFromPillowImage(pillowImage)

    def __validFromArray(self, image: ndarray) -> bool:
        height, width = image.shape[:2]
        if width > MIN_IMAGE_SIZE and height > MIN_IMAGE_SIZE:
            return True
        else:
            return False

    def __validFromPillowImage(self, image: Image.Image) -> bool:
        width, height = image.size
        if width > MIN_IMAGE_SIZE and height > MIN_IMAGE_SIZE:
            return True
        else:
            return False