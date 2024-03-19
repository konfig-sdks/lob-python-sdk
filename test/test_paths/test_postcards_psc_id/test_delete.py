# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

import unittest
from unittest.mock import patch

import urllib3

import lob_python_sdk
from lob_python_sdk.paths.postcards_psc_id import delete
from lob_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPostcardsPscId(ApiTestMixin, unittest.TestCase):
    """
    PostcardsPscId unit test stubs
        Cancel
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
