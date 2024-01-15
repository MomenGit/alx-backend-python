#!/usr/bin/env python3
"""Defines wait_n function"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    waits for a random delays between 0 and max_delay
    (included and float value) seconds and eventually returns it
    Args:
        n(int): number of delays
        max_delay(int): The max number for the random value generated for delay
    """

    delays: List[float] = [await wait_random(max_delay) for _ in range(n)]

    return sorted(delays)
