#!/usr/bn/env python3
"""
A module for testing the utils module.
"""
import unittest
from typing import Any, Dict, Tuple
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests for the `access_nested_map` function
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
            path (tuple): The path to value in the nested dictionary.
            expected_output (Any): The expected output of the function.

        Asserts that the output of `access_nested_map` is equal to
        `expected_output`.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

        @parameterized.expand([
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"),
             KeyError),
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

            Assers that `access_nested_map` raises `expected_exception`.
            """
            with self.assertRaises(expected_exception):
                access_nested_map(nested_map, path)
