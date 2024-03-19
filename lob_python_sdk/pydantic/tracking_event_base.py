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

from lob_python_sdk.pydantic.evnt_id import EvntId

class TrackingEventBase(BaseModel):
    id: EvntId = Field(alias='id')

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime = Field(alias='date_created')

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: datetime = Field(alias='date_modified')

    object: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='object')

    # A timestamp in ISO 8601 format of the date USPS registered the event.
    time: typing.Optional[datetime] = Field(None, alias='time')
    class Config:
        arbitrary_types_allowed = True
