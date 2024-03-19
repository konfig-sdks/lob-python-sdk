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

from lob_python_sdk.pydantic.metadata import Metadata
from lob_python_sdk.pydantic.resource_description import ResourceDescription
from lob_python_sdk.pydantic.template_version import TemplateVersion
from lob_python_sdk.pydantic.tmpl_id import TmplId

class Template(BaseModel):
    id: TmplId = Field(alias='id')

    # An array of all non-deleted [version objects](#tag/Template-Versions) associated with the template.
    versions: typing.List[TemplateVersion] = Field(alias='versions')

    published_version: typing.Union[bool, date, datetime, dict, float, int, list, str, None] = Field(alias='published_version')

    description: typing.Optional[ResourceDescription] = Field(None, alias='description')

    # Value is resource type.
    object: typing.Optional[Literal["template"]] = Field(None, alias='object')

    metadata: typing.Optional[Metadata] = Field(None, alias='metadata')

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: typing.Optional[datetime] = Field(None, alias='date_created')

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: typing.Optional[datetime] = Field(None, alias='date_modified')

    # Only returned if the resource has been successfully deleted.
    deleted: typing.Optional[bool] = Field(None, alias='deleted')
    class Config:
        arbitrary_types_allowed = True
