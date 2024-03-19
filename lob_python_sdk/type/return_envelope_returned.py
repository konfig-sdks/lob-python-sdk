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


class RequiredReturnEnvelopeReturned(TypedDict):
    pass

class OptionalReturnEnvelopeReturned(TypedDict, total=False):
    # The unique ID of the Return Envelope.
    id: str

    # A quick reference name for the Return Envelope.
    alias: str

    # The url of the return envelope.
    url: str

    # Value is resource type.
    object: str

class ReturnEnvelopeReturned(RequiredReturnEnvelopeReturned, OptionalReturnEnvelopeReturned):
    pass
ReturnEnvelopeReturned = typing.Union[bool,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
