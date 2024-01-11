#!/usr/bin/env python3
"""Defines function sum_list"""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of the input list of float numbers"""

    sum: float = 0.0

    for num in input_list:
        sum += num

    return sum
