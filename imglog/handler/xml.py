import imp
import xml.etree.ElementTree as ET
import xml.dom.minidom as md
import os
from pathlib import Path
from typing import List, Union

from .abc import AbstractHandler
from ..record import ImageLogRecord


class XMLHandler(AbstractHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8',
                 indent: str = '\t') -> None:
        
        filename = os.fspath(filename)

        self.__records: List[ImageLogRecord] = list()
        self.__filename = os.path.abspath(filename)
        self.__encoding = encoding
        self.__indent = indent

    def emit(self, record: ImageLogRecord) -> None:
        self.__records.append(record)

    def flush(self) -> None:
        xmlString = self.xmlString
        with open(self.__filename, 'w', encoding=self.__encoding) as file:
            file.write(xmlString)
            file.flush()
        
        self.__records.clear()


    @property
    def xmlString(self) -> str:
        root = ET.Element('imglog')

        for record in self.__records:
            recordElement = ET.Element('record',
                                       {
                                           'id': record.id,
                                           'time': record.time,
                                           'level': record.level
                                       })
            
            imagesElement = ET.Element('images')
            for image in record.images:
                imageElement = ET.Element('image')
                imageElement.text = image
                imagesElement.append(imageElement)

            imagesPropertyElement = ET.Element('imagesProperty')
            for imagePropery in record.imagesProperty:
                imagePropertyElement = ET.Element('imageProperty', imagePropery.toDict())
                imagesPropertyElement.append(imagePropertyElement)
            
            recordElement.append(imagesElement)
            recordElement.append(imagesPropertyElement)

            root.append(recordElement)

        etreeString = ET.tostring(root, encoding=self.__encoding).decode(self.__encoding)
        document = md.parseString(etreeString)

        return document.toprettyxml(indent=self.__indent, encoding=self.__encoding)

    def close(self) -> None:
        del self.__records
        del self.__filename
        del self.__encoding
        del self.__indent