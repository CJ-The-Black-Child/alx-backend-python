#!/usr/bin/env python3
""" Module for Task 1"""

from typing import List
from importlib import import_module
# Use import module to mport the async_generator function
async_generator = import_module("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async
    comprehension over async_generator
    """
    return [i async for i in async_generator()]
