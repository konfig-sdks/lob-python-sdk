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


class RequiredAddressFieldsIntl(TypedDict):
    # The primary number, street name, and directional information.
    address_line1: str

class OptionalAddressFieldsIntl(TypedDict, total=False):
    # An optional field containing any information which can't fit into line 1.
    address_line2: typing.Optional[str]

    address_city: typing.Optional[str]

    address_state: typing.Optional[str]

    # Optional postal code.
    address_zip: typing.Optional[str]

class AddressFieldsIntl(RequiredAddressFieldsIntl, OptionalAddressFieldsIntl):
    pass
