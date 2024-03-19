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
from lob_python_sdk.pydantic.postcard_size import PostcardSize

class Returned(BaseModel):
    mail_type: typing.Optional[MailType] = Field(None, alias='mail_type')

    size: typing.Optional[PostcardSize] = Field(None, alias='size')

    # The original URL of the `front` template.
    front_original_url: typing.Optional[str] = Field(None, alias='front_original_url')

    # The original URL of the `back` template.
    back_original_url: typing.Optional[str] = Field(None, alias='back_original_url')
    class Config:
        arbitrary_types_allowed = True
