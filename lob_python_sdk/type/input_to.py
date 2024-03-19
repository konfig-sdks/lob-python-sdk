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
from lob_python_sdk.type.inline_address import InlineAddress

class RequiredInputTo(TypedDict):
    pass

class OptionalInputTo(TypedDict, total=False):
    # Must either be an address ID or an inline object with correct address parameters. If an object is used, an address will be created, corrected, and standardized for free whenever possible using our US Address Verification engine (if it is a US address), and returned back with an ID. Depending on your <a href=\"https://dashboard.lob.com/#/settings/editions\" target=\"_blank\">Print & Mail Edition</a>, US addresses may also be run through <a href=\"#tag/National-Change-of-Address\">National Change of Address Linkage(NCOALink)</a>. Non-US addresses will be standardized into uppercase only. If a US address used does not meet your account’s <a href=\"https://dashboard.lob.com/#/settings/account\" target=\"_blank\">US Mail strictness setting</a>, the request will fail. <a href=\"https://help.lob.com/print-and-mail/all-about-addresses\" target=\"_blank\">Lob Guide: Verification of Mailing Addresses</a>
    to: typing.Union[AdrId, InlineAddress]

class InputTo(RequiredInputTo, OptionalInputTo):
    pass
