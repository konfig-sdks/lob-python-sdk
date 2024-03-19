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
from lob_python_sdk.type.country_extended import CountryExtended
from lob_python_sdk.type.postal_code import PostalCode
from lob_python_sdk.type.state import State

class RequiredIntlSuggestions(TypedDict):
    # The primary number range of the address that identifies a building at street level. 
    primary_number_range: str

    # The primary delivery line (usually the street address) of the address. Combination of the following applicable `components` (primary number & secondary information may be missing or inaccurate): * `primary_number` * `street_predirection` * `street_name` * `street_suffix` * `street_postdirection` * `secondary_designator` * `secondary_number` * `pmb_designator` * `pmb_number` 
    primary_line: str

    city: City

    country: CountryExtended

    state: State

    zip_code: PostalCode

class OptionalIntlSuggestions(TypedDict, total=False):
    pass

class IntlSuggestions(RequiredIntlSuggestions, OptionalIntlSuggestions):
    pass
