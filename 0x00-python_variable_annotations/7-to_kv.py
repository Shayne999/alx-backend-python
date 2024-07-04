#!/usr/bin/env python3
"""Defines a function that takes a key and an
integer value and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple"""
    return (k, float(v**2))
