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

from lob_python_sdk.pydantic.primary_line import PrimaryLine
from lob_python_sdk.pydantic.recipient import Recipient
from lob_python_sdk.pydantic.secondary_line import SecondaryLine

class IntlVerificationBase(BaseModel):
    recipient: typing.Optional[Recipient] = Field(None, alias='recipient')

    primary_line: typing.Optional[PrimaryLine] = Field(None, alias='primary_line')

    secondary_line: typing.Optional[SecondaryLine] = Field(None, alias='secondary_line')
    class Config:
        arbitrary_types_allowed = True
