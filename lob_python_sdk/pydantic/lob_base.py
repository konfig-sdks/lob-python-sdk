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


class LobBase(BaseModel):
    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime = Field(alias='date_created')

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: datetime = Field(alias='date_modified')

    # Value is resource type.
    object: str = Field(alias='object')

    # Only returned if the resource has been successfully deleted.
    deleted: typing.Optional[bool] = Field(None, alias='deleted')
    class Config:
        arbitrary_types_allowed = True
