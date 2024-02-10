#!/usr/bin/env python3
"""Test cases for client module"""
import unittest
from unittest.mock import MagicMock, PropertyMock, patch
import client
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


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


@parameterized_class(attrs=(
    "org_payload",
    "repos_payload",
    "expected_repos",
    "apache2_repos"), input_values=TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration Test class for client.GithubOrgClient"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def setUp(self) -> None:
        """Hook method for setting up the test fixture before exercising it"""
        self.mock_get.side_effect = [
            MagicMock(json=lambda: self.org_payload),
            MagicMock(json=lambda: self.repos_payload)
        ]

    def test_public_repos(self):
        """
        Test client.GithubOrgClient.public_repos method in an integration test
        That means that we will only mock code that sends external requests
        """
        org_client = client.GithubOrgClient('test_org')
        public_repos = org_client.public_repos()
        self.assertEqual(public_repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test the public_repos with the argument license="apache-2.0"""
        org_client = client.GithubOrgClient('test_org')
        public_repos = org_client.public_repos(license="apache-2.0")
        self.assertEqual(public_repos, self.apache2_repos)


if __name__ == "__main__":
    unittest.main()
