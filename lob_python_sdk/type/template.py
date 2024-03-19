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

from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.template_version import TemplateVersion
from lob_python_sdk.type.tmpl_id import TmplId

class RequiredTemplate(TypedDict):
    id: TmplId

    # An array of all non-deleted [version objects](#tag/Template-Versions) associated with the template.
    versions: typing.List[TemplateVersion]

    published_version: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class OptionalTemplate(TypedDict, total=False):
    description: ResourceDescription

    # Value is resource type.
    object: str

    metadata: Metadata

    # A timestamp in ISO 8601 format of the date the resource was created.
    date_created: datetime

    # A timestamp in ISO 8601 format of the date the resource was last modified.
    date_modified: datetime

    # Only returned if the resource has been successfully deleted.
    deleted: bool

class Template(RequiredTemplate, OptionalTemplate):
    pass
