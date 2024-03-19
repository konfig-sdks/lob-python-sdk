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


class RequiredFailureReasonError(TypedDict):
    pass

class OptionalFailureReasonError(TypedDict, total=False):
    # Failed URL of asset
    url: typing.Optional[str]

    # URL host
    host: typing.Optional[str]

    # URL path
    path: typing.Optional[str]

    # Network protocol
    protocol: typing.Optional[str]

    # Instructions on how to resolve the error
    remediation: typing.Optional[str]

    # HTTP response status code message or service defined error
    error_type: typing.Optional[str]

    # HTTP response status codes if the error is asset related
    status_code: typing.Optional[typing.Union[int, float]]

class FailureReasonError(RequiredFailureReasonError, OptionalFailureReasonError):
    pass
