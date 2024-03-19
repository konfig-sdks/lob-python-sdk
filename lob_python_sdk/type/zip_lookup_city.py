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

from lob_python_sdk.type.city import City
from lob_python_sdk.type.county_fips import CountyFips
from lob_python_sdk.type.state import State

class RequiredZipLookupCity(TypedDict):
    city: City

    state: State

    # County name of the address city.
    county: str

    county_fips: CountyFips

    # Indicates whether or not the city is the <a href=\"https://en.wikipedia.org/wiki/ZIP_Code#ZIP_Codes_and_previous_zoning_lines\" target=\"_blank\">USPS default city</a> (preferred city) of a ZIP code. There is only one preferred city per ZIP code, which will always be in position 0 in the array of cities. 
    preferred: bool

class OptionalZipLookupCity(TypedDict, total=False):
    pass

class ZipLookupCity(RequiredZipLookupCity, OptionalZipLookupCity):
    pass
