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

from lob_python_sdk.type.country_extended import CountryExtended

class RequiredIntlAutocompletionsWritable(TypedDict):
    # Only accepts numbers and street names in an alphanumeric format. 
    address_prefix: str

    country: CountryExtended

class OptionalIntlAutocompletionsWritable(TypedDict, total=False):
    # An optional city input used to filter suggestions. Case insensitive and does not match partial abbreviations. 
    city: str

    # An optional state input used to filter suggestions. Case insensitive and does not match partial abbreviations. 
    state: str

    # An optional Zip Code input used to filter suggestions. Matches partial entries. 
    zip_code: str

    # If `true`, sort suggestions by proximity to the IP set in the `X-Forwarded-For` header. 
    geo_ip_sort: bool

class IntlAutocompletionsWritable(RequiredIntlAutocompletionsWritable, OptionalIntlAutocompletionsWritable):
    pass
