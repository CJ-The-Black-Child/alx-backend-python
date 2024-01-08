#!/usr/bin/env python3
"""
A module for testing the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the `GithubOrgClient` class.
    """
    @parameterized.expand(
        [
            ("google"),
            ("abc"),
        ]
    )
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """
        Tests that `GithubOrgClient.org` returns the correct value.

        Args:
            org_name (str): The name of the Github organization to test.

        Asserts that the output of `GithubOrgClient.org` is equal to
        the expected payload.
        """
        test_client = GithubOrgClient(org_name)
        self.assertEqual(test_client.org, {"payload": True})
        mock_get_json.assert_called_once()

    @parameterized.expand(
        [
            ("google", {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }
             ),
            ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
        ]
    )
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, org_name, expected_dict, mock_org):
        """
        Tests that `GithubOrgClient._public_repos_url` returns the correct
        value.

        Args:
            org_name (str): The name of the Github organization to test.
            expected_dict (dict): The expected dictionary containing
            the repos_url.

        Asserts that the output of `GithubOrgClient._public_repos_url`
        is equal to the expected repos_url.
        """
        mock_org.return_value = expected_dict
        test_client = GithubOrgClient(org_name)
        self.assertEqual(
            test_client._public_repos_url, expected_dict["repos_url"]
        )

    @patch(
        "client.GithubOrgClient._public_repos_url", new_callable=PropertyMock
    )
    @patch("client.get_json")
    def test_public_repos(
        self,
        mock_get_json,
        mock_public_repos_url
    ):
        """
        Tests that `GithubOrgClient.public_repos` returns the correct value.

        Args:
            mock_get_json (MagicMock): A mock of `get_json`.
            mock_public_repos_url (PropertyMock): A mock of
            `_public_repos_url`.

        Asserts that the output of `GithubOrgClient.public_repos` is equal
        to the expected list of repo names.
        """
        test_org_name = "google"
        expected_repos = ["repo1", "repo2"]
        mock_get_json.return_value = [
            {"name": repo_name} for repo_name in expected_repos
        ]
        mock_public_repos_url.return_value = (
            f"https://api.github.com/orgs/{test_org_name}/repos"
        )

        test_client = GithubOrgClient(test_org_name)
        self.assertEqual(test_client.public_repos, expected_repos)
        mock_get_json.assert_called_once_with(
            mock_public_repos_url.return_value
        )

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, key, expected):
        """
        Tests that `GithubOrgClient.has_license` returns the correct value.

        Args:
            repo (dict): The repo dictionary containing a license key.
            key (str): The license key to check for.
            expected (bool): The expected result.

        Asserts that the output of `GithubOrgClient.has_license` is equal
        to `expected`.
        """
        test_client = GithubOrgClient("org_name")
        self.assertEqual(test_client.has_license(repo, key), expected)


@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3],
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Performs integration tests for the `GithubOrgClient` class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up class fixtures before running tests.
        """
        route_payload = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """
        Tests that `GithubOrgClient.public_repos` returns the correct value.

        Asserts that the output of `GithubOrgClient.public_repos` is equal
        to the expected list of repo names.
        """
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.public_repos, self.expected_repos)
        self.get_patcher.assert_called_once()

    @classmethod
    def tearDownClass(cls):
        """
        Removes the class fixtures after running all tests.
        """
        cls.get_patcher.stop()
