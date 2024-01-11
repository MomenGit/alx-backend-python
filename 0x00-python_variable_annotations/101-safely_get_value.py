#!/usr/bin/env python3
"""Defines function safely_get_value"""

from typing import Mapping, TypeVar, Union, Any

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value in a Mapping using key, otherwise returns default"""
    if key in dct:
        return dct[key]
    else:
        return default
