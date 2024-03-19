# coding: utf-8

"""
    Lob

    The Lob API is organized around REST. Our API is designed to have predictable, resource-oriented URLs and uses HTTP response codes to indicate any API errors. <p> 

    The version of the OpenAPI document: 1.19.28
    Contact: lob-openapi@lob.com
    Created by: https://support.lob.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from lob_python_sdk.type.adr_id import AdrId
from lob_python_sdk.type.inline_address_us import InlineAddressUs

RequiredInputFromUs = TypedDict("RequiredInputFromUs", {
    })

OptionalInputFromUs = TypedDict("OptionalInputFromUs", {
    # *Required* if `to` address is international. Must either be an address ID or an inline object with correct address parameters. Must either be an address ID or an inline object with correct address parameters. All addresses will be standardized into uppercase without being modified by verification.
    "from": typing.Union[AdrId, InlineAddressUs],
    }, total=False)

class InputFromUs(RequiredInputFromUs, OptionalInputFromUs):
    pass
