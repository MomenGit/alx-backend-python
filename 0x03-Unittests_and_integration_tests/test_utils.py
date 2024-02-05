#!/usr/bin/env python3
"""Test cases for the Utils module"""
from typing import Mapping, Sequence
from unittest import result

from defer import return_value
import utils
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock


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


class TestGetJson(unittest.TestCase):
    """Test cases for utils.get_json function"""

    @parameterized.expand(
        [("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False})])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """Mock testing for utils.get_json function"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = utils.get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test cases for utils.memoize function"""

    def test_memoize(self):
        """Mock test utils.memoize function"""
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", autospec=True) as mocked_a:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mocked_a.assert_called_once()
