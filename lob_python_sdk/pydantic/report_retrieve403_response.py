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


class ReportRetrieve403Response(BaseModel):
    # The error code
    code: typing.Optional[typing.Union[int, float]] = Field(None, alias='code')

    # Details of the error message with the feature flagged mentioned.
    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True
