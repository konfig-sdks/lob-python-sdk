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

from lob_python_sdk.pydantic.intl_auto_id import IntlAutoId
from lob_python_sdk.pydantic.intl_suggestions import IntlSuggestions

class IntlAutocompletions(BaseModel):
    id: typing.Optional[IntlAutoId] = Field(None, alias='id')

    # An array of objects representing suggested addresses. 
    suggestions: typing.Optional[typing.List[IntlSuggestions]] = Field(None, alias='suggestions')
    class Config:
        arbitrary_types_allowed = True
