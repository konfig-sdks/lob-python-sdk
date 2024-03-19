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

from lob_python_sdk.pydantic.report_retrieve_response_data import ReportRetrieveResponseData

class ReportRetrieveResponse(BaseModel):
    data: ReportRetrieveResponseData = Field(alias='data')

    # number of resources in a set
    count: int = Field(alias='count')

    # Indicates the total number of records. Provided when the request specifies an \"include\" query parameter
    total_count: int = Field(alias='total_count')

    # Url of next page of items in list.
    next_url: typing.Optional[typing.Optional[str]] = Field(None, alias='next_url')

    # Url of previous page of items in list.
    prev_url: typing.Optional[typing.Optional[str]] = Field(None, alias='prev_url')
    class Config:
        arbitrary_types_allowed = True
