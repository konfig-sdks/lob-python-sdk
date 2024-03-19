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

from lob_python_sdk.type.merge_variables import MergeVariables
from lob_python_sdk.type.metadata import Metadata
from lob_python_sdk.type.resource_description import ResourceDescription
from lob_python_sdk.type.send_date import SendDate

class RequiredEditableNoMailtype(TypedDict):
    pass

class OptionalEditableNoMailtype(TypedDict, total=False):
    description: ResourceDescription

    metadata: Metadata

    merge_variables: MergeVariables

    send_date: SendDate

class EditableNoMailtype(RequiredEditableNoMailtype, OptionalEditableNoMailtype):
    pass
