#!/usr/bin/env python3
"""
A module for testing the client module.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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

    @parameterized.expand(
        [
            (
                "google", {
                    "repos_url": "https://api.github.com/orgs/google/repos"
                }
            ),
            ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"}),
        ]
    )
    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    @patch("client.get_json", return_value=[
        {"name": "repo1"}, {"name": "repo2"}
        ]
    )
    def test_public_repos(
        self,
        org_name,
        expected_dict,
        mock_org,
        mock_get_json
    ):
        """
        Tests that `GithubOrgClient.public_repos` returns the correct value.

        Args:
            org_name (str): The name of the Github organization to test.
            expected_dict (dict): The expected dictionary containing
            the repos_url.

        Asserts that the output of `GithubOrgClient.public_repos` is equal
        to the expected list of repo names.
        """
        mock_org.return_value = expected_dict
        test_client = GithubOrgClient(org_name)
        self.assertEqual(test_client.public_repos, ["repo1", "repo2"])
        mock_get_json.assert_called_once_with(expected_dict["repos_url"])

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
