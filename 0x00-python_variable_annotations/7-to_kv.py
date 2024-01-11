#!/usr/bin/env python3
"""Defines function to_kv"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns the sum of the input list of float numbers"""

    return (k, v*v)
