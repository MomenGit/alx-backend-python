#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import MagicMock, PropertyMock, patch
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

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mocked_org:
            payload = {"repos_url": True}
            mocked_org.return_value = payload
            org_client = client.GithubOrgClient("test")
            self.assertEqual(org_client._public_repos_url,
                             payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mocked_get):
        """
        Test that the list of repos is what you expect from the chosen payload
        """
        json_payload = [{"name": "Google"}, {"name": "YouTube"}]
        mocked_get.return_value = json_payload
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_url:
            mocked_url.return_value = ""
            org_client = client.GithubOrgClient("test")
            result = org_client.public_repos()
            check = [repo["name"] for repo in json_payload]
            self.assertEqual(result, check)
            mocked_url.assert_called_once()
            mocked_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, expected):
        """Parameterized unit-test for client.GithubOrgClient.has_license"""
        self.assertEqual(client.GithubOrgClient.has_license(
            repo, license_key), expected)


if __name__ == "__main__":
    unittest.main()
