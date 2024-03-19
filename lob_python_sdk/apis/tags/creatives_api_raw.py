# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from lob_python_sdk.paths.creatives.post import CreateRaw
from lob_python_sdk.paths.creatives_crv_id.get import RetrieveRaw
from lob_python_sdk.paths.creatives_crv_id.patch import UpdateRaw


class CreativesApiRaw(
    CreateRaw,
    RetrieveRaw,
    UpdateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
