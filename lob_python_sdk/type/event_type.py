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

from lob_python_sdk.type.address_types import AddressTypes
from lob_python_sdk.type.bank_account_types import BankAccountTypes
from lob_python_sdk.type.check_types import CheckTypes
from lob_python_sdk.type.letter_types import LetterTypes
from lob_python_sdk.type.postcard_types import PostcardTypes
from lob_python_sdk.type.self_mailer_types import SelfMailerTypes

class RequiredEventType(TypedDict):
    id: typing.Union[PostcardTypes, SelfMailerTypes, LetterTypes, CheckTypes, AddressTypes, BankAccountTypes]

    # Value is `true` if the event type is enabled in both the test and live environments and `false` if it is only enabled in the live environment.
    enabled_for_test: bool

    resource: str

    # Value is resource type.
    object: str

class OptionalEventType(TypedDict, total=False):
    pass

class EventType(RequiredEventType, OptionalEventType):
    pass
