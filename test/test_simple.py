# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

import unittest

import os
from pprint import pprint
from lob_python_sdk import Lob

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        lob = Lob(
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD'
        )
        self.assertIsNotNone(lob)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
