#!/usr/bin/env python3
"""Module for task #9"""
from typing import Iterable, Tuple, List, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        Takes am iterable of sequences and returns a list of
        tuples with each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
