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

from lob_python_sdk.type.event_type import EventType

class RequiredEvents(TypedDict):
    # Unique identifier prefixed with `evt_`.
    id: str

    # The body of the associated resource as they were at the time of the event, i.e. the [postcard object](#operation/postcard_retrieve), [the letter object](#operation/letter_retrieve), [the check object](#operation/check_retrieve), [the address object](#operation/address_retrieve), or [the bank account object](#operation/bank_account_retrieve). For `.deleted` events, the body matches the response for the corresponding delete endpoint for that resource (e.g. the [postcard delete response](#operation/postcard_delete)).
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Unique identifier of the related resource for the event.
    reference_id: str

    event_type: EventType

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime

    # Value is resource type.
    object: str

class OptionalEvents(TypedDict, total=False):
    pass

class Events(RequiredEvents, OptionalEvents):
    pass
