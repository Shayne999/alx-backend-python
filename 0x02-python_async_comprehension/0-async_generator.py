#!/usr/bin/env python3
"""Yields a random number in the range of 0 to 10"""


import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
