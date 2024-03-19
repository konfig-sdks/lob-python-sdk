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


class RequiredLobBase(TypedDict):
    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: datetime

    # Value is resource type.
    object: str

class OptionalLobBase(TypedDict, total=False):
    # Only returned if the resource has been successfully deleted.
    deleted: bool

class LobBase(RequiredLobBase, OptionalLobBase):
    pass
