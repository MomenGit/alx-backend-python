#!/usr/bin/env python3
"""Defines wait_n function"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Return Task wait_random) which
    waits for a random delays between 0 and max_delay
    (included and float value) seconds and eventually returns it
    Args:
        max_delay(int): The max number for the random value generated for delay
    """

    return asyncio.Task(wait_random(max_delay))
