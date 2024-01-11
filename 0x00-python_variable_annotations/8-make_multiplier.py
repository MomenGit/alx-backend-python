#!/usr/bin/env python3
"""Defines function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns the sum of the input list of float numbers"""

    def mul(num: float) -> float:
        """Returns the multiplication of num with multiplier"""
        return multiplier * num

    return mul
