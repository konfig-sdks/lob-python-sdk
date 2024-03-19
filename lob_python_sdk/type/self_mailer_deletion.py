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

from lob_python_sdk.type.sfm_id import SfmId

class RequiredSelfMailerDeletion(TypedDict):
    pass

class OptionalSelfMailerDeletion(TypedDict, total=False):
    id: SfmId

    # Only returned if the resource has been successfully deleted.
    deleted: bool

class SelfMailerDeletion(RequiredSelfMailerDeletion, OptionalSelfMailerDeletion):
    pass
