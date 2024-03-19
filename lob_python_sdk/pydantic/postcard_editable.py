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

from lob_python_sdk.pydantic.input_from_us import InputFromUs
from lob_python_sdk.pydantic.input_to import InputTo
from lob_python_sdk.pydantic.postcard_base import PostcardBase
from lob_python_sdk.pydantic.psc_back import PscBack
from lob_python_sdk.pydantic.psc_front import PscFront
from lob_python_sdk.pydantic.psc_use_type import PscUseType
from lob_python_sdk.pydantic.qr_code import QrCode

PostcardEditable = typing.Union[PostcardBase,InputTo,InputFromUs,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
