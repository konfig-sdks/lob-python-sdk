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

from lob_python_sdk.type.zip_code_plus4 import ZipCodePlus4

class RequiredComponents(TypedDict):
    # The 5-digit ZIP code
    zip_code: str

    zip_code_plus_4: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalComponents(TypedDict, total=False):
    pass

class Components(RequiredComponents, OptionalComponents):
    pass
