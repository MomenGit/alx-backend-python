#!/usr/bin/env python3
"""Defines function element_length"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing a sequence and its length"""
    return [(i, len(i)) for i in lst]
