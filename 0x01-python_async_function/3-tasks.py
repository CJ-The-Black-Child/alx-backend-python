#!/usr/bin/env python3
"""
Module for Task 3
"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns a asyncio.Task.
    Args:
        max_delay (int): Maximum delay time in seconds.
    Returns:
        asyncio.Task: Task object created from wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
