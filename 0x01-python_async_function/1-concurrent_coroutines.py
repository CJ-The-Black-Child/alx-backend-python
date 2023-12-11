#!/usr/bin/env python3
"""
Module for Task 1
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns wait_random n times
    with the specified max_delay.
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay time in seconds.
    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*tasks)
    return sorted(wait_times)
