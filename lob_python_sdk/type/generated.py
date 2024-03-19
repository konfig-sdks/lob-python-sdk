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

from lob_python_sdk.type.address import Address
from lob_python_sdk.type.thumbnail import Thumbnail

class RequiredGenerated(TypedDict):
    to: Address

    carrier: str

class OptionalGenerated(TypedDict, total=False):
    thumbnails: typing.List[Thumbnail]

    # A date in YYYY-MM-DD format of the mailpiece's expected delivery date based on its `send_date`.
    expected_delivery_date: date

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: datetime

    # Only returned if the resource has been successfully deleted.
    deleted: bool

class Generated(RequiredGenerated, OptionalGenerated):
    pass
