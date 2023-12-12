#!/usr/bin/env python3
"""Module for Task 2"""

import asyncio
import time
from importlib import import_module
# Use the impoty_module to impoty the async_comprehension function
async_comprehension = import_module(
    "1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes async_comprehension four times in parallel
    using asyncio.gather
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
