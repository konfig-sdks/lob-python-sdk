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


class AddressFieldsUs(BaseModel):
    # The primary number, street name, and directional information.
    address_line1: str = Field(alias='address_line1')

    address_city: str = Field(alias='address_city')

    # 2 letter state short-name code
    address_state: str = Field(alias='address_state')

    # Must follow the ZIP format of `12345` or ZIP+4 format of `12345-1234`. 
    address_zip: str = Field(alias='address_zip')

    # An optional field containing any information which can't fit into line 1.
    address_line2: typing.Optional[typing.Optional[str]] = Field(None, alias='address_line2')
    class Config:
        arbitrary_types_allowed = True
