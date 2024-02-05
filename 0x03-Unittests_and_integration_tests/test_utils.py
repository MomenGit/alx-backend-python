#!/usr/bin/env python3
""""""
from typing import Mapping, Sequence
import utils
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for utils.access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected):
        """Parameterized testing for utils.access_nested_map function"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({"a", 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence):
        """Parameterized exception testing for
        utils.access_nested_map function
        """
        self.assertRaises(KeyError)
