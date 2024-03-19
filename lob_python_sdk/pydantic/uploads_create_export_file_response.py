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

from lob_python_sdk.pydantic.uploads_create_export_file_response_errors import UploadsCreateExportFileResponseErrors

class UploadsCreateExportFileResponse(BaseModel):
    # A conventional HTTP status code
    code: Literal[400, 404] = Field(alias='code')

    # A human-readable message with more details about the error
    message: str = Field(alias='message')

    errors: UploadsCreateExportFileResponseErrors = Field(alias='errors')
    class Config:
        arbitrary_types_allowed = True
