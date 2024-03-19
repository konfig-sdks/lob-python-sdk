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

from lob_python_sdk.type.addresses import Addresses
from lob_python_sdk.type.reverse_geocode_id import ReverseGeocodeId

class RequiredReverseGeocode(TypedDict):
    pass

class OptionalReverseGeocode(TypedDict, total=False):
    id: ReverseGeocodeId

    # list of addresses 
    addresses: typing.List[Addresses]

    # Value is resource type.
    object: str

class ReverseGeocode(RequiredReverseGeocode, OptionalReverseGeocode):
    pass
