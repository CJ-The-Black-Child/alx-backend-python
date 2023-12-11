#!/usr/bin/env python3
"""
Module for Task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds and returns it.
    Args:
        max_delay (int): Maximum delay time in seconds. Defaults to 10.
    Returns:
        float: Random delay time.
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
