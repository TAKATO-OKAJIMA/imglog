import json
import logging
from pathlib import Path
from typing import List, Union

from .base import HTMLElement, HTMLFileNodeElement, ScriptFileElement
from ...record import ImageLogRecord
from ...resource import html as htmlResource
from ...resource import script as scriptResource


class LogItemElement(HTMLElement):

    def __init__(self, records: List[ImageLogRecord]) -> None:
        self.__records = records

    def render(self) -> str:
        items = list()
        items.append('''
        <ul class="nav flex-column">
        ''')

        for record in self.__records:
            items.append(f'''
            <li id="{record.id}" class="nav-item border" onclick="loadLog('{record.id}', this)">
                <div class="row gy-2">
                    <div class="col-md-12"></div>
                    <div class="col-md-8">
                        <h6 class="text-primary ms-2">{record.time}</h6>
                    </div>
                    <div class="col-md-4 text-end">
                        <h6 class="me-2"><span class="badge {logging.getLevelName(record.level)}">{logging.getLevelName(record.level)}</span></h6>
                    </div>
                    <h6 class="ms-2 mb-0">{record.id}</h6>
                    <h6 class="ms-2">{record.name}</h6>
                    <div class="col-md-12"></div>
                </div>
            </li>
            ''')

        items.append('</ul>')

        return '\n'.join(items)

    
class LogFileElement(HTMLFileNodeElement):

    def __init__(self, records: List[ImageLogRecord]) -> None:
        HTMLFileNodeElement.__init__(self, htmlResource.load('root.html'))

        self.addElement('navitems', LogItemElement(records))

        scirptElement = ScriptFileElement(scriptResource.load('root.js'))
        scirptElement.setParameter('recorddata', json.dumps([record.toDict() for record in records],
                                                            indent=4))
        self.addElement('script', scirptElement)
