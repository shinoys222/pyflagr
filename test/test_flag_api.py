# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flagr
from flagr.api.flag_api import FlagApi  # noqa: E501
from flagr.rest import ApiException


class TestFlagApi(unittest.TestCase):
    """FlagApi unit test stubs"""

    def setUp(self):
        self.api = flagr.api.flag_api.FlagApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_flag(self):
        """Test case for create_flag

        """
        pass

    def test_delete_flag(self):
        """Test case for delete_flag

        """
        pass

    def test_find_flags(self):
        """Test case for find_flags

        """
        pass

    def test_get_flag(self):
        """Test case for get_flag

        """
        pass

    def test_get_flag_snapshots(self):
        """Test case for get_flag_snapshots

        """
        pass

    def test_put_flag(self):
        """Test case for put_flag

        """
        pass

    def test_set_flag_enabled(self):
        """Test case for set_flag_enabled

        """
        pass


if __name__ == '__main__':
    unittest.main()
