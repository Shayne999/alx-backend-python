#!/usr/bin/env python3
"""Basic async syntax"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """return a random float between 0 and max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay