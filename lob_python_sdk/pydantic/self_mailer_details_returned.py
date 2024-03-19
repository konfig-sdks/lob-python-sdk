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

from lob_python_sdk.pydantic.mail_type import MailType
from lob_python_sdk.pydantic.self_mailer_size import SelfMailerSize

class SelfMailerDetailsReturned(BaseModel):
    mail_type: typing.Optional[MailType] = Field(None, alias='mail_type')

    size: typing.Optional[SelfMailerSize] = Field(None, alias='size')

    # The original URL of the `inside` template.
    inside_original_url: typing.Optional[str] = Field(None, alias='inside_original_url')

    # The original URL of the `outside` template.
    outside_original_url: typing.Optional[str] = Field(None, alias='outside_original_url')
    class Config:
        arbitrary_types_allowed = True
