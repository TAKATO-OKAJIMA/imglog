import io 
from typing import overload, Union

from numpy import ndarray
from PIL import Image

from ..record import ImageProperty

INVALID_PROPERTY = (
    -1,
    -1,
    -1,
    'TOINS'
)


class ImagePropertyExtractor(object):

    def __init__(self) -> None:
        pass

    @overload
    def extract(self, image: bytes) -> ImageProperty:
        ...
    
    @overload
    def extract(self, image: ndarray) -> ImageProperty:
        ...

    @overload
    def extract(self, image: Image.Image) -> ImageProperty:
        ...

    def extract(self, image: Union[bytes, ndarray, Image.Image]) -> ImageProperty:
        if isinstance(image, bytes):
            return self.__extractFromBytes(image)
        elif isinstance(image, ndarray):
            return self.__extractFromArray(image)
        elif isinstance(image, Image.Image):
            return self.__extractFromPillowImage(image)
        else:
            return ImageProperty(*INVALID_PROPERTY)

    def __extractFromBytes(self, image: bytes) -> ImageProperty:
        pillowImage = Image.open(io.BytesIO(image))
        return self.__extractFromPillowImage(pillowImage) 
    
    def __extractFromArray(self, image: ndarray) -> ImageProperty:
        pillowImage = Image.fromarray(ndarray)
        return self.__extractFromPillowImage(pillowImage)

    def __extractFromPillowImage(self, image: Image.Image) -> ImageProperty:
        width, height = image.size
        channel = len(image.getbands())
        mode = image.mode

        imagePropety = ImageProperty(width, height, channel, mode)

        return imagePropety