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


class UsAutocompletionsWritable(BaseModel):
    # Only accepts numbers and street names in an alphanumeric format. 
    address_prefix: str = Field(alias='address_prefix')

    # An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. 
    city: typing.Optional[str] = Field(None, alias='city')

    # An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. 
    state: typing.Optional[str] = Field(None, alias='state')

    # An optional ZIP Code input used to filter suggestions. Matches partial entries. 
    zip_code: typing.Optional[str] = Field(None, alias='zip_code')

    # If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. 
    geo_ip_sort: typing.Optional[bool] = Field(None, alias='geo_ip_sort')
    class Config:
        arbitrary_types_allowed = True
