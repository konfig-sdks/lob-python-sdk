# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.checks_chk_id.delete import Cancel
from lob_python_sdk.paths.checks.post import Create
from lob_python_sdk.paths.checks.get import List
from lob_python_sdk.paths.checks_chk_id.get import Retrieve
from lob_python_sdk.apis.tags.checks_api_raw import ChecksApiRaw


class ChecksApi(
    Cancel,
    Create,
    List,
    Retrieve,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ChecksApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ChecksApiRaw(api_client)