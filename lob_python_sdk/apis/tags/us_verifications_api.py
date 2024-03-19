# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.bulk_us_verifications.post import BulkVerifyAddresses
from lob_python_sdk.paths.us_verifications.post import Verification
from lob_python_sdk.apis.tags.us_verifications_api_raw import USVerificationsApiRaw


class USVerificationsApi(
    BulkVerifyAddresses,
    Verification,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: USVerificationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = USVerificationsApiRaw(api_client)
