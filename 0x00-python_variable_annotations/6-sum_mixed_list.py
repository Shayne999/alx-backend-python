#!/usr/bin/env python3
"""
Defines a function which takes a list mixed of integers and floats
and returns their sum as a float.
"""


def sum_mixed_list(mxd_lst: 'list[int, float]') -> float:
    return sum(mxd_lst)