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

from lob_python_sdk.type.ex_id import ExId
from lob_python_sdk.type.upl_id import UplId

class RequiredExportRetrieveResponse(TypedDict):
    id: ExId

    # A timestamp in ISO 8601 format of the date the export was created
    dateCreated: datetime

    # A timestamp in ISO 8601 format of the date the export was last modified
    dateModified: datetime

    # Returns as `true` if the resource has been successfully deleted.
    deleted: bool

    # The URL for the generated export file.
    s3Url: str

    # The state of the export file, which can be `in_progress`, `failed` or `succeeded`.
    state: str

    # The export file type, which can be `all`, `failures` or `successes`.
    type: str

    uploadId: UplId

class OptionalExportRetrieveResponse(TypedDict, total=False):
    pass

class ExportRetrieveResponse(RequiredExportRetrieveResponse, OptionalExportRetrieveResponse):
    pass
