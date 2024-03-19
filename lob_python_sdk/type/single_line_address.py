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


class RequiredSingleLineAddress(TypedDict):
    # The entire address in one string (e.g., \"210 King Street 94107\"). _Does not support a recipient and will error when other payload parameters are provided._ 
    address: str

class OptionalSingleLineAddress(TypedDict, total=False):
    pass

class SingleLineAddress(RequiredSingleLineAddress, OptionalSingleLineAddress):
    pass
