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

from lob_python_sdk.type.adr_id import AdrId
from lob_python_sdk.type.inline_address_us_chk import InlineAddressUsChk

class RequiredCheckInputTo(TypedDict):
    pass

class OptionalCheckInputTo(TypedDict, total=False):
    # Must either be an address ID or an inline object with correct address parameters. Checks cannot be sent internationally (`address_country` must be `US`). The total string of the sum of `address_line1` and `address_line2` must be no longer than 50 characters combined. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine, and returned back with an ID. Depending on your <a href=\"https://dashboard.lob.com/#/settings/editions\" target=\"_blank\">Print & Mail Edition</a>, addresses may also be run through [National Change of Address (NCOALink)](#tag/National-Change-of-Address). If an address used does not meet your account’s <a href=\"https://dashboard.lob.com/#/settings/account\" target=\"_blank\">US Mail Strictness Setting</a>, the request will fail. <a href=\"https://help.lob.com/print-and-mail/all-about-addresses\" target=\"_blank\">More about verification of mailing addresses</a>
    to: typing.Union[AdrId, InlineAddressUsChk]

class CheckInputTo(RequiredCheckInputTo, OptionalCheckInputTo):
    pass
