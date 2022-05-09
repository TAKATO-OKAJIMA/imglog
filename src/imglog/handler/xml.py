import logging
import xml.etree.ElementTree as ET
import xml.dom.minidom as md
from pathlib import Path
from typing import Union

from .handler import FileHandler


class XMLHandler(FileHandler):

    def __init__(self,
                 filename: Union[str, Path],
                 encoding: str = 'utf-8',
                 indent: str = '\t') -> None:

        self.__indent = indent

        FileHandler.__init__(self, filename, encoding)

    def flush(self) -> None:
        xmlString = self.xmlString
        with open(self._filename, 'w', encoding=self._encoding) as file:
            file.write(xmlString)
            file.flush()
        
        self._records.clear()

        FileHandler.flush(self)


    @property
    def xmlString(self) -> str:
        root = ET.Element('imglog')

        for record in self._records:
            recordElement = ET.Element('record',
                                       {
                                           'id': record.id,
                                           'time': record.time,
                                           'level': logging.getLevelName(record.level)
                                       })
            
            imagesElement = ET.Element('images')
            for image in record.images:
                imageElement = ET.Element('image')
                imageElement.text = image
                imagesElement.append(imageElement)

            imagesPropertyElement = ET.Element('imagesProperty')
            for imageProperty in record.imagesProperty:
                imagePropertyElement = ET.Element('imageProperty', imageProperty.toDictStringEscaped())
                imagesPropertyElement.append(imagePropertyElement)
            
            recordElement.append(imagesElement)
            recordElement.append(imagesPropertyElement)

            root.append(recordElement)

        etreeString = ET.tostring(root, encoding=self._encoding).decode(self._encoding)
        document = md.parseString(etreeString)

        return document.toprettyxml(indent=self.__indent, encoding=self._encoding).decode(self._encoding)

    def close(self) -> None:
        FileHandler.close(self)
        del self.__indent