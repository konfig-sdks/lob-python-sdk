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

from lob_python_sdk.pydantic.ex_id import ExId
from lob_python_sdk.pydantic.upl_id import UplId

class ExportRetrieveResponse(BaseModel):
    id: ExId = Field(alias='id')

    # A timestamp in ISO 8601 format of the date the export was created
    date_created: datetime = Field(alias='dateCreated')

    # A timestamp in ISO 8601 format of the date the export was last modified
    date_modified: datetime = Field(alias='dateModified')

    # Returns as `true` if the resource has been successfully deleted.
    deleted: bool = Field(alias='deleted')

    # The URL for the generated export file.
    s3_url: str = Field(alias='s3Url')

    # The state of the export file, which can be `in_progress`, `failed` or `succeeded`.
    state: Literal["in_progress", "failed", "succeeded"] = Field(alias='state')

    # The export file type, which can be `all`, `failures` or `successes`.
    type: Literal["all", "failures", "successes"] = Field(alias='type')

    upload_id: UplId = Field(alias='uploadId')
    class Config:
        arbitrary_types_allowed = True
