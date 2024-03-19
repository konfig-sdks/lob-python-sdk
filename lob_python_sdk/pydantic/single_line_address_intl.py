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

from lob_python_sdk.pydantic.country_extended import CountryExtended

class SingleLineAddressIntl(BaseModel):
    # The entire address in one string (e.g., \"370 Water St C1N 1C4\"). 
    address: str = Field(alias='address')

    country: CountryExtended = Field(alias='country')
    class Config:
        arbitrary_types_allowed = True
