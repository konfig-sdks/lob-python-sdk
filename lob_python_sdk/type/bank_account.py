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

from lob_python_sdk.type.bank_account_base import BankAccountBase
from lob_python_sdk.type.bank_id import BankId
from lob_python_sdk.type.lob_base import LobBase
from lob_python_sdk.type.signed_link import SignedLink

BankAccount = typing.Union[BankAccountBase,LobBase,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
