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

from lob_python_sdk.pydantic.address import Address
from lob_python_sdk.pydantic.thumbnail import Thumbnail

class Generated(BaseModel):
    to: Address = Field(alias='to')

    carrier: Literal["USPS"] = Field(alias='carrier')

    thumbnails: typing.Optional[typing.List[Thumbnail]] = Field(None, alias='thumbnails')

    # A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`.
    expected_delivery_date: typing.Optional[date] = Field(None, alias='expected_delivery_date')

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: typing.Optional[datetime] = Field(None, alias='date_created')

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: typing.Optional[datetime] = Field(None, alias='date_modified')

    # Only returned if the resource has been successfully deleted.
    deleted: typing.Optional[bool] = Field(None, alias='deleted')
    class Config:
        arbitrary_types_allowed = True
