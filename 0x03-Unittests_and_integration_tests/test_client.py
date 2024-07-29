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

    @patch('client.GithubOrgClient.org',
           new_callable=unittest.mock.PropertyMock)
    def test_public_repos(self, mock_org):
        """Test public repos"""
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = mock_payload

        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public repos"""

        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
        ]

        mock_get_json.return_value = mock_repos_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("test_org")
            repos = client.public_repos()

            expected_repos = ["repo1", "repo2"]
            self.assertEqual(repos, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")