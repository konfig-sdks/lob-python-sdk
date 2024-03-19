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

from lob_python_sdk.pydantic.address_types import AddressTypes
from lob_python_sdk.pydantic.bank_account_types import BankAccountTypes
from lob_python_sdk.pydantic.check_types import CheckTypes
from lob_python_sdk.pydantic.letter_types import LetterTypes
from lob_python_sdk.pydantic.postcard_types import PostcardTypes
from lob_python_sdk.pydantic.self_mailer_types import SelfMailerTypes

class EventType(BaseModel):
    id: typing.Union[PostcardTypes, SelfMailerTypes, LetterTypes, CheckTypes, AddressTypes, BankAccountTypes] = Field(alias='id')

    # Value is `true` if the event type is enabled in both the test and live environments and `false` if it is only enabled in the live environment.
    enabled_for_test: bool = Field(alias='enabled_for_test')

    resource: Literal["postcards", "self mailers", "letters", "checks", "addresses", "bank accounts"] = Field(alias='resource')

    # Value is resource type.
    object: Literal["event_type"] = Field(alias='object')
    class Config:
        arbitrary_types_allowed = True
