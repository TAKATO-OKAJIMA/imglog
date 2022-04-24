import os
from pathlib import Path
from typing import Union, Dict, List


def getReplaceTargetString(replace: str) -> str:
    return '{' + replace + '}'


class HTMLElement():

    def __init__(self) -> None:
        pass

    def render(self) -> str:
        raise NotImplementedError


class HTMLNodeElement(HTMLElement):

    def __init__(self, document: str) -> None:
        self.__document = document
        self.__elements = dict()

    def addElement(self, name: str, element: 'HTMLElement') -> None:
        self.__elements[name] = element

    def render(self) -> str:
        document = self.__document

        for name, element in self.__elements.items():
            document = document.replace(getReplaceTargetString(name), element.render())

        return document

    
class HTMLStringNodeElement(HTMLNodeElement):

    def __init__(self, document: str = None) -> None:
        if document:
            HTMLNodeElement.__init__(self, document)


class HTMLFileNodeElement(HTMLNodeElement):
    
    def __init__(self, document: Union[str, Path]) -> None:
        document = os.fspath(document)

        with open(os.path.abspath(document), 'r', encoding='utf-8') as file:
            HTMLNodeElement.__init__(self, document)

        
class ScriptElement(HTMLElement):

    def __init__(self, script: str) -> None:
        self.__script = script
        self.__params = dict()

    def setParameter(self, parameterName: str, parameterValue: str) -> None:
        self.__params[parameterName] = parameterValue

    def render(self) -> str:
        script = self.__script

        for parameterName, parameterValue in self.__params.items():
            script = script.replace(getReplaceTargetString(parameterName), parameterValue)

        return f'''
        <script type="text/javascript">
            {script}
        <script>
        '''


class ScriptStringElement(ScriptElement):

    def __init__(self, script: str = None) -> None:
        if script:
            ScriptElement.__init__(self, script)


class ScriptFileElement(ScriptElement):

    def __init__(self, script: Union[str, Path]) -> None:
        script = os.fspath(script)

        with open(os.path.abspath(script), 'r', encoding='utf-8') as file:
            ScriptElement.__init__(self, file.read())


class StyleElement(HTMLElement):

    def __init__(self, style: str) -> None:
        self.__style = style
    
    def render(self) -> str:
        return f'''
        <style>
            {self.__style}
        </style>
        '''


class StyleStringElement(StyleElement):

    def __init__(self, style: str = None) -> None:
        if style:
            StyleElement.__init__(self, style)


class StyleFileElement(StyleElement):

    def __init__(self, style: str) -> None:
        style = os.fspath(style)

        with open(os.path.abspath(style), 'r', encoding='utf-8') as file:
            StyleElement.__init__(self, file.read())


class StyleEditableElement(StyleElement):

    def __init__(self) -> None:
        self.__rules = dict()

    def addStyleRule(self, selector: str, rules: Dict[str, str]) -> None:
        self.__rules[selector] = rules

    def render(self) -> str:
        styles = list()

        for selector, rule in self.__rules.items():
            style = list()

            for property, value in rule.items():
                style.append(f'{property}:{value};')

            styles.append('''
            {selector} {
                {style}
            }
            '''.format(selector=selector, style='\n'.join(style)))

        return f'''
        <style>
            {'\n'.join(styles)}
        </style>
        '''