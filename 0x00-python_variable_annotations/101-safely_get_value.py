#!/usr/bin/env python3
"""Module for task #11"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value of a key in a mapping if it exists, else
    returns a default value.
    """
    return dct.get(key, default)
