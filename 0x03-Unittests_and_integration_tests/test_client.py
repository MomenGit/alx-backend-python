#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import MagicMock, patch
import client
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for client.GithubOrgClient class"""

    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_org(self, org, expected, mocked_get):
        """Test cases for client.GithubOrgClient.org function"""
        mock_response = MagicMock()
        mock_response.json.return_value = expected
        mocked_get.return_value = mock_response

        org_client = client.GithubOrgClient(org)
        org1 = org_client.org
        org2 = org_client.org
        mocked_get.assert_called_once()
        self.assertEqual(org1, org2)


if __name__ == "__main__":
    unittest.main()
