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


class RequiredRequiredAddressColumnMapping(TypedDict):
    # The column header from the csv file that should be mapped to the required field `name`
    name: typing.Optional[str]

    # The column header from the csv file that should be mapped to the required field `address_line1`
    address_line1: typing.Optional[str]

    # The column header from the csv file that should be mapped to the required field `address_city`
    address_city: typing.Optional[str]

    # The column header from the csv file that should be mapped to the required field `address_state`
    address_state: typing.Optional[str]

    # The column header from the csv file that should be mapped to the required field `address_zip`
    address_zip: typing.Optional[str]

class OptionalRequiredAddressColumnMapping(TypedDict, total=False):
    pass

class RequiredAddressColumnMapping(RequiredRequiredAddressColumnMapping, OptionalRequiredAddressColumnMapping):
    pass
