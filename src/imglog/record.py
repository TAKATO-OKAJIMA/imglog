import uuid
import datetime
import logging
from typing import List, Union, Optional

INVALID_PROPERTY = (
    -1,
    -1,
    -1,
    'INVALID_IMAGE'
)


class ImageProperty(object):

    def __init__(self, width: int, height: int, channel: int, mode: str) -> None:
        self.__width = width
        self.__height = height
        self.__channel = channel
        self.__mode = mode

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def channel(self) -> int:
        return self.__channel

    @property
    def mode(self) -> str:
        return self.__mode

    def toDict(self) -> dict:
        properties = {
            'width': self.__width,
            'height': self.__height,
            'channel': self.__channel,
            'mode': self.__mode
        }

        return properties
    
    def toDictStringEscaped(self) -> dict:
        properties = {
            'width': str(self.__width),
            'height': str(self.__height),
            'channel': str(self.__channel),
            'mode': self.__mode
        }

        return properties

    @staticmethod
    def initializeInvalidProperty() -> 'ImageProperty':
        return ImageProperty(*INVALID_PROPERTY)


class ImageLogRecord(object):

    def __init__(self,
                 name: str,
                 level: int,
                 images: List[Union[bytes, str]], 
                 imagesProperty: List[ImageProperty], 
                 msg: Optional[str] = None) -> None:
        self.__id = uuid.uuid4().hex
        self.__name = name
        self.__time = str(datetime.datetime.now())
        self.__level = level
        self.__images = images
        self.__imagesProperty = imagesProperty
        self.__msg = msg

    @property
    def id(self) -> int:
        return self.__id

    @property
    def time(self) -> str:
        return self.__time

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def levelName(self) -> str:
        return logging.getLevelName(self.__level)

    @property
    def images(self) -> List[Union[bytes, str]]:
        return self.__images.copy()
    
    @property
    def imagesProperty(self) -> List[ImageProperty]:
        return self.__imagesProperty.copy()

    @property
    def msg(self) -> str:
        return self.__msg

    def toDict(self) -> dict:
        properties = {
            'id': self.__id,
            'name': self.__name,
            'time': self.__time,
            'level': logging.getLevelName(self.__level),
            'images': self.__images,
            'imagesProperty': [imageProperty.toDict() for imageProperty in self.__imagesProperty],
            'msg': self.__msg
        }

        return properties

