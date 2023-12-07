#!/usr/bin/env python3
"""Module for task #7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float, returns a tuple with the
    string and square of the int/float
    """
    return k, v ** 2
