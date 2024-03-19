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


class ReturnEnvelopeReturned(BaseModel):
    # The unique ID of the Return Envelope.
    id: typing.Optional[str] = Field(None, alias='id')

    # A quick reference name for the Return Envelope.
    alias: typing.Optional[str] = Field(None, alias='alias')

    # The url of the return envelope.
    url: typing.Optional[str] = Field(None, alias='url')

    # Value is resource type.
    object: typing.Optional[str] = Field(None, alias='object')
    class Config:
        arbitrary_types_allowed = True
ReturnEnvelopeReturned = typing.Union[bool,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
