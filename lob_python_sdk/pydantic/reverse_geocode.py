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
from pydantic import BaseModel, Field, RootModel

from lob_python_sdk.pydantic.addresses import Addresses
from lob_python_sdk.pydantic.reverse_geocode_id import ReverseGeocodeId

class ReverseGeocode(BaseModel):
    id: typing.Optional[ReverseGeocodeId] = Field(None, alias='id')

    # list of addresses 
    addresses: typing.Optional[typing.List[Addresses]] = Field(None, alias='addresses')

    # Value is resource type.
    object: typing.Optional[Literal["us_reverse_geocode_lookup"]] = Field(None, alias='object')
    class Config:
        arbitrary_types_allowed = True
