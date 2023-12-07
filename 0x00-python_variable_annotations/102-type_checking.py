#!/usr/bin/env python3
"""Module for task #12"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns a list with each element of a tuple repeated 'factor' times."""
    return [item for item in lst for _ in range(factor)]
