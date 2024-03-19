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

from lob_python_sdk.pydantic.address_fields_intl import AddressFieldsIntl
from lob_python_sdk.pydantic.company import Company
from lob_python_sdk.pydantic.country_extended import CountryExtended
from lob_python_sdk.pydantic.metadata import Metadata
from lob_python_sdk.pydantic.resource_description import ResourceDescription

AddressEditableIntl = typing.Union[AddressFieldsIntl,typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None], typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
