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

from lob_python_sdk.type.cents import Cents

class RequiredBankAccountVerify(TypedDict):
    # In live mode, an array containing the two micro deposits (in cents) placed in the bank account. In test mode, no micro deposits will be placed, so any two integers between `1` and `100` will work.
    amounts: typing.List[Cents]

class OptionalBankAccountVerify(TypedDict, total=False):
    pass

class BankAccountVerify(RequiredBankAccountVerify, OptionalBankAccountVerify):
    pass
