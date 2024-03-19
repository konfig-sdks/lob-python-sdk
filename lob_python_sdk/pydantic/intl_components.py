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
from lob_python_sdk.pydantic.postal_code import PostalCode
from lob_python_sdk.pydantic.state import State

class IntlComponents(BaseModel):
    # The numeric or alphanumeric part of an address preceding the street name. Often the house, building, or PO Box number.
    primary_number: typing.Optional[str] = Field(None, alias='primary_number')

    # The name of the street.
    street_name: typing.Optional[str] = Field(None, alias='street_name')

    city: typing.Optional[City] = Field(None, alias='city')

    state: typing.Optional[State] = Field(None, alias='state')

    postal_code: typing.Optional[PostalCode] = Field(None, alias='postal_code')
    class Config:
        arbitrary_types_allowed = True
