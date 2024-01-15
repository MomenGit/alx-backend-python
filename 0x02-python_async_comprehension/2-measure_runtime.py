#!/usr/bin/env python3
"""Defines function measure_runtime"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times
    in parallel using asyncio.gather
    measures the total runtime and returns it
    """
    start_time = time.perf_counter()

    await asyncio.gather(*[async_comprehension() for i in range(4)])

    total_time = time.perf_counter() - start_time

    return total_time
