#!/usr/bin/env python3
"""
Type-annotated function multiplier that returns a function
that multiplies a float by multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
