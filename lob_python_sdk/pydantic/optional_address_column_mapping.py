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


class OptionalAddressColumnMapping(BaseModel):
    # The column header from the csv file that should be mapped to the optional field \"address_line2\"
    address_line2: typing.Optional[str] = Field(alias='address_line2')

    # The column header from the csv file that should be mapped to the optional field \"company\"
    company: typing.Optional[str] = Field(alias='company')

    # The column header from the csv file that should be mapped to the optional field \"address_country\"
    address_country: typing.Optional[str] = Field(alias='address_country')
    class Config:
        arbitrary_types_allowed = True
