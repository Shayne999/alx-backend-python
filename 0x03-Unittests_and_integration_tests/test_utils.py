#!/usr/bin/env python3
"""Test utils"""
import unittest
from parameterized import parameterized
from utils import access_nested_map



class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map"""

    @parameterized.expand([
        {"nested_map": {"a": 1}, "path": ("a",), "expected": 1},
        {"nested_map": {"a": {"b": 2}}, "path": ("a",), "expected": {"b": 2}},
        {"nested_map": {"a": {"b": 2}}, "path": ("a", "b"), "expected": 2}
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
