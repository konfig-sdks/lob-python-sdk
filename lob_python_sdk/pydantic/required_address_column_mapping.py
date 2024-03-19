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


class RequiredAddressColumnMapping(BaseModel):
    # The column header from the csv file that should be mapped to the required field `name`
    name: typing.Optional[str] = Field(alias='name')

    # The column header from the csv file that should be mapped to the required field `address_line1`
    address_line1: typing.Optional[str] = Field(alias='address_line1')

    # The column header from the csv file that should be mapped to the required field `address_city`
    address_city: typing.Optional[str] = Field(alias='address_city')

    # The column header from the csv file that should be mapped to the required field `address_state`
    address_state: typing.Optional[str] = Field(alias='address_state')

    # The column header from the csv file that should be mapped to the required field `address_zip`
    address_zip: typing.Optional[str] = Field(alias='address_zip')
    class Config:
        arbitrary_types_allowed = True
