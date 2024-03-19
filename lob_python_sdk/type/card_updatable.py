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

from lob_python_sdk.type.card_description import CardDescription

class RequiredCardUpdatable(TypedDict):
    pass

class OptionalCardUpdatable(TypedDict, total=False):
    description: CardDescription

    # Allows for auto reordering
    auto_reorder: bool

    # The quantity of items to be reordered (only required when auto_reorder is true).
    reorder_quantity: typing.Union[int, float]

class CardUpdatable(RequiredCardUpdatable, OptionalCardUpdatable):
    pass
