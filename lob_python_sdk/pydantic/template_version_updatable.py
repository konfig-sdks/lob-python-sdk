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

from lob_python_sdk.pydantic.engine import Engine
from lob_python_sdk.pydantic.resource_description import ResourceDescription
from lob_python_sdk.pydantic.template_required_vars import TemplateRequiredVars

class TemplateVersionUpdatable(BaseModel):
    description: typing.Optional[ResourceDescription] = Field(None, alias='description')

    engine: typing.Optional[Engine] = Field(None, alias='engine')

    required_vars: typing.Optional[TemplateRequiredVars] = Field(None, alias='required_vars')
    class Config:
        arbitrary_types_allowed = True
