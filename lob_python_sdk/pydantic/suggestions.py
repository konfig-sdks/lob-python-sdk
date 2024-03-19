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
from lob_python_sdk.pydantic.state import State
from lob_python_sdk.pydantic.zip_code import ZipCode

class Suggestions(BaseModel):
    # The primary delivery line (usually the street address) of the address. Combination of the following applicable `components` (primary number & secondary information may be missing or inaccurate): * `primary_number` * `street_predirection` * `street_name` * `street_suffix` * `street_postdirection` * `secondary_designator` * `secondary_number` * `pmb_designator` * `pmb_number` 
    primary_line: str = Field(alias='primary_line')

    city: City = Field(alias='city')

    state: State = Field(alias='state')

    zip_code: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='zip_code')

    # Value is resource type.
    object: typing.Optional[Literal["us_autocompletion"]] = Field(None, alias='object')
    class Config:
        arbitrary_types_allowed = True
