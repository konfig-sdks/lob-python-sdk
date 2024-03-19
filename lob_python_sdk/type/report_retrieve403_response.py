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


class RequiredReportRetrieve403Response(TypedDict):
    pass

class OptionalReportRetrieve403Response(TypedDict, total=False):
    # The error code
    code: typing.Union[int, float]

    # Details of the error message with the feature flagged mentioned.
    message: str

class ReportRetrieve403Response(RequiredReportRetrieve403Response, OptionalReportRetrieve403Response):
    pass
