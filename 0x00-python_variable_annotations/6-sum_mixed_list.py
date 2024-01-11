#!/usr/bin/env python3
"""Defines function sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the input mixed list of float or int numbers"""

    sum: float = 0.0

    for num in mxd_lst:
        sum += num

    return sum
