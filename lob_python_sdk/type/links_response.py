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

from lob_python_sdk.type.link_response import LinkResponse

class RequiredLinksResponse(TypedDict):
    pass

class OptionalLinksResponse(TypedDict, total=False):
    # The number of results in the current response.
    count: int

    # How many results to return.
    limit: int

    # An integer that designates the offset at which to begin returning results. Defaults to 0.
    offset: int

    # list of links 
    data: typing.List[LinkResponse]

class LinksResponse(RequiredLinksResponse, OptionalLinksResponse):
    pass
