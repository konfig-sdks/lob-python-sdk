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

from lob_python_sdk.pydantic.link_response import LinkResponse

class LinksResponse(BaseModel):
    # The number of results in the current response.
    count: typing.Optional[int] = Field(None, alias='count')

    # How many results to return.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # An integer that designates the offset at which to begin returning results. Defaults to 0.
    offset: typing.Optional[int] = Field(None, alias='offset')

    # list of links 
    data: typing.Optional[typing.List[LinkResponse]] = Field(None, alias='data')
    class Config:
        arbitrary_types_allowed = True
