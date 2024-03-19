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

from lob_python_sdk.type.uploads_create_export_file_response_errors import UploadsCreateExportFileResponseErrors

class RequiredUploadsCreateExportFileResponse(TypedDict):
    # A conventional HTTP status code
    code: typing.Union[int, float]

    # A human-readable message with more details about the error
    message: str

    errors: UploadsCreateExportFileResponseErrors

class OptionalUploadsCreateExportFileResponse(TypedDict, total=False):
    pass

class UploadsCreateExportFileResponse(RequiredUploadsCreateExportFileResponse, OptionalUploadsCreateExportFileResponse):
    pass
