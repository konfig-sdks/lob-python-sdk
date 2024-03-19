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

from lob_python_sdk.type.cmp_id import CmpId
from lob_python_sdk.type.creative_base import CreativeBase
from lob_python_sdk.type.crv_back import CrvBack
from lob_python_sdk.type.crv_file import CrvFile
from lob_python_sdk.type.crv_front import CrvFront
from lob_python_sdk.type.crv_inside import CrvInside
from lob_python_sdk.type.crv_outside import CrvOutside
from lob_python_sdk.type.letter_details_writable import LetterDetailsWritable
from lob_python_sdk.type.self_mailer_details_writable import SelfMailerDetailsWritable
from lob_python_sdk.type.writable import Writable

CreativeWritable = typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None],typing.Union[bool, date, datetime, dict, float, int, list, str, None],typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
