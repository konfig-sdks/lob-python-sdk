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

from lob_python_sdk.pydantic.failure_reason_error import FailureReasonError

class FailureReason(BaseModel):
    # Instructions on how to resolve the error
    remediation: typing.Optional[str] = Field(None, alias='remediation')

    # Reason failure occurred
    failure_reason: typing.Optional[str] = Field(None, alias='failure_reason')

    errors: typing.Optional[typing.Optional[typing.List[FailureReasonError]]] = Field(None, alias='errors')
    class Config:
        arbitrary_types_allowed = True
