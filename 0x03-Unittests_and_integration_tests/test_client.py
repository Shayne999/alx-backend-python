#!/usr/bin/env python3
"""Test client"""
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test github org client"""

    @parameterized.expand([
        ("google",)
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
