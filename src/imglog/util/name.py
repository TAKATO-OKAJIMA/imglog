from typing import Union, List


class LoggerName(object):

    def __init__(self, name: Union[str, List[str]]) -> None:
        if isinstance(name, str):
            self.__name = name.split('.')
        if isinstance(name, list) and isinstance(name[0], str):
            self.__name = name.copy()

    @property
    def parent(self) -> 'LoggerName':
        if len(self.__name) > 1:
            return LoggerName(self.__name[:-1].copy())
        else:
            return LoggerName('root')
    
    @property
    def isRoot(self) -> bool:
        return str(self) == 'root'

    def __eq__(self, other: 'LoggerName') -> bool:
        return str(self) == str(other)

    def __ne__(self, other: 'LoggerName') -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '.'.join(self.__name)