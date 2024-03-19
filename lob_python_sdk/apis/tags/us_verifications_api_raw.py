# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.bulk_us_verifications.post import BulkVerifyAddressesRaw
from lob_python_sdk.paths.us_verifications.post import VerificationRaw


class USVerificationsApiRaw(
    BulkVerifyAddressesRaw,
    VerificationRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
