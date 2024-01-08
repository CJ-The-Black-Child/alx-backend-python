#!/usr/bin/env python3
"""
A module for testing the utils module.
"""
import unittest
from typing import Any, Dict, Tuple
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests for the `access_nested_map` function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str], expected_output: Any
    ) -> None:
        """
        Tests `that access_nested_map` returns the correct output.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the value in the nested dictionary.
            expected_output (Any): The expected output of the function.

        Asserts that the output of `access_nested_map` is equal to
        `expected_output`.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b")),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict[str, Any],
        path: Tuple[str],
        expected_exception: Exception
    ) -> None:
        """
        Tests that `access_nested_map` raises the correct exception.
        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path to the value in the nested dictionary.
            expected_exception (Exception): The expected exception.

        Asserts that `access_nested_map` raises `expected_exception`
        with the correct message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(expected_exception))


class TestGetJson(unittest.TestCase):
    """
    Tests for the `get_json` function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Tests that `get_json` returns the expected result.

        Args:
            test_url (str): The URL to get JSON from.
            test_payload (dict): The expected payload of the JSON response.

        Asserts that the output of `get_json` is equal to `test_payload`.
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_get.assert_called_once_with(test_url)
