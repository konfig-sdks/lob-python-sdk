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

from lob_python_sdk.pydantic.address_placement import AddressPlacement
from lob_python_sdk.pydantic.card_id import CardId
from lob_python_sdk.pydantic.editable import Editable
from lob_python_sdk.pydantic.extra_service import ExtraService
from lob_python_sdk.pydantic.input_from import InputFrom
from lob_python_sdk.pydantic.input_to import InputTo
from lob_python_sdk.pydantic.ltr_file import LtrFile
from lob_python_sdk.pydantic.ltr_size import LtrSize
from lob_python_sdk.pydantic.ltr_use_type import LtrUseType
from lob_python_sdk.pydantic.mail_type import MailType
from lob_python_sdk.pydantic.qr_code import QrCode
from lob_python_sdk.pydantic.return_envelope_user_provided import ReturnEnvelopeUserProvided
from lob_python_sdk.pydantic.user_provided import UserProvided

LetterEditable = typing.Union[InputTo,InputFrom,Editable,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
