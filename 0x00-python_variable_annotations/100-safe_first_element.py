#!/usr/bin/env python3
"""Defines function safe_first_element"""

# The types of the elements of the input are not know


from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a sequence, otherwise returns None"""
    if lst:
        return lst[0]
    else:
        return None
