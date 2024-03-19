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

from lob_python_sdk.pydantic.adr_id import AdrId
from lob_python_sdk.pydantic.bank_id_no_description import BankIdNoDescription
from lob_python_sdk.pydantic.check_base import CheckBase
from lob_python_sdk.pydantic.check_bottom import CheckBottom
from lob_python_sdk.pydantic.check_input_to import CheckInputTo
from lob_python_sdk.pydantic.chk_use_type import ChkUseType
from lob_python_sdk.pydantic.html_string import HtmlString
from lob_python_sdk.pydantic.inline_address_us import InlineAddressUs
from lob_python_sdk.pydantic.local_file_path import LocalFilePath
from lob_python_sdk.pydantic.remote_file_url import RemoteFileUrl
from lob_python_sdk.pydantic.tmpl_id import TmplId

CheckEditableProps = typing.Union[CheckBase,CheckInputTo,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
