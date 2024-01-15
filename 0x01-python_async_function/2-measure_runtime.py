#!/usr/bin/env python3
"""Defines measure_time function"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    Args:
        n(int): number of delays
        max_delay(int): The max number for the random value generated for delay
    """

    start_time = time.perf_counter()

    delays = asyncio.run(wait_n(n, max_delay))

    total_time = time.perf_counter() - start_time

    return total_time/n
