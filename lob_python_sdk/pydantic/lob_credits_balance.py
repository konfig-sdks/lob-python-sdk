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


class LobCreditsBalance(BaseModel):
    # Account's current balance of Lob Credits. Can be positive, negative, or zero.
    balance: typing.Union[int, float] = Field(alias='balance')
    class Config:
        arbitrary_types_allowed = True
