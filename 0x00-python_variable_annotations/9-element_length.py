#!/usr/bin/env python3
"""
Returns the length of an element in a list
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns the length of an element in a list"""
    return [(i, len(i)) for i in lst]
