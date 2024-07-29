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
    @patch('client.get_json', return_value={})
    def test_org(self, org_name, mock_get_json):
        """Test org"""
        client = GithubOrgClient(org_name)
        org_data = client.org

        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_name)
        )

        self.assertEqual(org_data, {})
