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


class FailureReasonError(BaseModel):
    # Failed URL of asset
    url: typing.Optional[typing.Optional[str]] = Field(None, alias='url')

    # URL host
    host: typing.Optional[typing.Optional[str]] = Field(None, alias='host')

    # URL path
    path: typing.Optional[typing.Optional[str]] = Field(None, alias='path')

    # Network protocol
    protocol: typing.Optional[typing.Optional[str]] = Field(None, alias='protocol')

    # Instructions on how to resolve the error
    remediation: typing.Optional[typing.Optional[str]] = Field(None, alias='remediation')

    # HTTP response status code message or service defined error
    error_type: typing.Optional[typing.Optional[str]] = Field(None, alias='error_type')

    # HTTP response status codes if the error is asset related
    status_code: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='status_code')
    class Config:
        arbitrary_types_allowed = True
