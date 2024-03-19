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

from lob_python_sdk.type.components import Components
from lob_python_sdk.type.location_analysis import LocationAnalysis

class RequiredAddresses(TypedDict):
    pass

class OptionalAddresses(TypedDict, total=False):
    components: Components

    location_analysis: LocationAnalysis

class Addresses(RequiredAddresses, OptionalAddresses):
    pass
