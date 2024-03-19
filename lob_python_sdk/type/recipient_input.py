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

from lob_python_sdk.type.city_no_description import CityNoDescription
from lob_python_sdk.type.primary_line_us import PrimaryLineUs
from lob_python_sdk.type.recipient import Recipient
from lob_python_sdk.type.secondary_line import SecondaryLine
from lob_python_sdk.type.urbanization import Urbanization
from lob_python_sdk.type.zip_code import ZipCode

RecipientInput = typing.Union[typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], typing.Union[bool, date, datetime, dict, float, int, list, str, None]],typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
