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


class RequiredAddressFieldsUs(TypedDict):
    # The primary number, street name, and directional information.
    address_line1: str

    address_city: str

    # 2 letter state short-name code
    address_state: str

    # Must follow the ZIP format of `12345` or ZIP+4 format of `12345-1234`. 
    address_zip: str

class OptionalAddressFieldsUs(TypedDict, total=False):
    # An optional field containing any information which can't fit into line 1.
    address_line2: typing.Optional[str]

class AddressFieldsUs(RequiredAddressFieldsUs, OptionalAddressFieldsUs):
    pass
