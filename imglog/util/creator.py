from typing import Tuple, overload

from PIL import Image, ImageDraw

DEFAULT_SIZE = (400, 300)
DEFAULT_IMAGE_COLOR = (0, 0, 0)
DEFAULT_TEXT_COLOR = (255, 255, 255)
DEFAULT_TEXT = 'This image is invalid'


class InvalidImageCreator(object):

    def __init__(self) -> None:
        pass

    @overload
    def create(self, 
               width: int, 
               height: int, 
               imageColor: Tuple[int, int, int] = ...,
               textColor: Tuple[int, int, int] = ...,
               text: str = ...) -> bytes:
        pass

    @overload
    def create(self, 
               size: Tuple[int, int],
               imageColor: Tuple[int, int, int] = ...,
               textColor: Tuple[int, int, int] = ...,
               text: str = ...) -> bytes:
        pass

    def create(self, 
               *args, 
               imageColor: Tuple[int, int, int] = DEFAULT_IMAGE_COLOR,
               textColor: Tuple[int, int, int] = DEFAULT_TEXT_COLOR, 
               text: str = DEFAULT_TEXT) -> bytes:
        if isinstance(args[0], int):
            size = (args[0], args[1])
        else:
            size = args[0]

        return self.__createFromTuple(size, imageColor, textColor, text)

    def createFromDefaultParameters(self) -> bytes:
        return self.create(DEFAULT_SIZE)

    def __createFromTuple(self, 
                          size: Tuple[int, int], 
                          imageColor: Tuple[int, int, int],
                          textColor: Tuple[int, int, int], 
                          text: str) -> bytes:
        image = Image.new('RGB', size, imageColor)

        draw = ImageDraw.Draw(image)

        draw.text(
            (size[0] / 2, size[1] / 2),
            text,
            fill=textColor,
            anchor='mm'
            )
        
        result = image.tobytes()

        return result
        