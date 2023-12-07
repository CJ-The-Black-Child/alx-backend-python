#!/usr/bin/env python3
""" Module for task #10 """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, else returns None.
    """
    return lst[0] if lst else None
