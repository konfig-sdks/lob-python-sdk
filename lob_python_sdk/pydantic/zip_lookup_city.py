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

from lob_python_sdk.pydantic.city import City
from lob_python_sdk.pydantic.county_fips import CountyFips
from lob_python_sdk.pydantic.state import State

class ZipLookupCity(BaseModel):
    city: City = Field(alias='city')

    state: State = Field(alias='state')

    # County name of the address city.
    county: str = Field(alias='county')

    county_fips: CountyFips = Field(alias='county_fips')

    # Indicates whether or not the city is the <a href=\"https://en.wikipedia.org/wiki/ZIP_Code#ZIP_Codes_and_previous_zoning_lines\" target=\"_blank\">USPS default city</a> (preferred city) of a ZIP code. There is only one preferred city per ZIP code, which will always be in position 0 in the array of cities. 
    preferred: bool = Field(alias='preferred')
    class Config:
        arbitrary_types_allowed = True
