import uuid
import datetime
from typing import List

class ImageProperty(object):

    def __init__(self, width: int, height: int, channel: int) -> None:
        self.__width = width
        self.__height = height
        self.__channel = channel

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def channel(self) -> int:
        return self.__channel

    def toDict(self) -> dict:
        properties = {
            'width': self.__width,
            'height': self.__height,
            'channel': self.__channel
        }

        return properties


class ImageLogRecord(object):

    def __init__(self, 
                 level: int,
                 images: List[bytes], 
                 imagesProperty: List[ImageProperty], 
                 msg: str = None) -> None:
        self.__id = uuid.uuid4().hex
        self.__time = str(datetime.datetime.now())
        self.__level = level
        self.__images = images
        self.__imagesPropery = imagesProperty
        self.__msg = msg

    @property
    def id(self) -> int:
        return self.__id

    @property
    def time(self) -> str:
        return self.__time

    @property
    def level(self) -> int:
        return self.__level

    @property
    def images(self) -> List[bytes]:
        return self.__images.copy()
    
    @property
    def imagesProperty(self) -> List[ImageProperty]:
        return self.__imagesPropery.copy()

    @property
    def msg(self) -> str:
        return self.__msg

    def toDict(self) -> dict:
        properties = {
            'id': self.__id,
            'time': self.__time,
            'level': self.__level,
            'images': self.__images,
            'imagesPropery': [imageProperty.toDict() for imageProperty in self.__imagesPropery],
            'msg': self.__msg
        }

        return properties