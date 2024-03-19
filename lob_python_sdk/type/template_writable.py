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

from lob_python_sdk.type.engine import Engine
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.template_html import TemplateHtml
from lob_python_sdk.type.template_required_vars import TemplateRequiredVars

class RequiredTemplateWritable(TypedDict):
    html: TemplateHtml

class OptionalTemplateWritable(TypedDict, total=False):
    description: ResourceDescription

    metadata: Metadata

    engine: Engine

    required_vars: TemplateRequiredVars

class TemplateWritable(RequiredTemplateWritable, OptionalTemplateWritable):
    pass
