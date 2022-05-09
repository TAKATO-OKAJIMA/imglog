from logging import _nameToLevel
from typing import overload


@overload
def _checkLevel(level: int) -> int:
    ...


@overload
def _checkLevel(level: str) -> int:
    ...


def _checkLevel(level):
    if isinstance(level, int):
        rv = level
    elif str(level) == level:
        if level not in _nameToLevel:
            raise ValueError("Unknown level: %r" % level)
        rv = _nameToLevel[level]
    else:
        raise TypeError("Level not an integer or a valid string: %r" % level)
    return rv