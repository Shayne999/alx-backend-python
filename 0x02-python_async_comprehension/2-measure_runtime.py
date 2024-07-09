#!/usr/bin/env python3
"""Measures and returns the total runtime of async_comprehension()"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of async_comprehension()"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
