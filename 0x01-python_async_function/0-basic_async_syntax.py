#!/usr/bin/env python3
"""Defines wait_random function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it
    Args:
        max_delay(int): The max number for the random value generated for delay
    """
    delay: float = random.random()*max_delay
    await asyncio.sleep(delay)
    return delay
