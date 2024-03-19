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

from lob_python_sdk.pydantic.identity_validation_company import IdentityValidationCompany
from lob_python_sdk.pydantic.identity_validation_id import IdentityValidationId
from lob_python_sdk.pydantic.primary_line_us import PrimaryLineUs
from lob_python_sdk.pydantic.secondary_line import SecondaryLine
from lob_python_sdk.pydantic.urbanization import Urbanization

class CompanyValidation(BaseModel):
    id: typing.Optional[IdentityValidationId] = Field(None, alias='id')

    company: typing.Optional[IdentityValidationCompany] = Field(None, alias='company')

    primary_line: typing.Optional[PrimaryLineUs] = Field(None, alias='primary_line')

    secondary_line: typing.Optional[SecondaryLine] = Field(None, alias='secondary_line')

    urbanization: typing.Optional[Urbanization] = Field(None, alias='urbanization')

    # Combination of the following applicable `components`: * City (`city`) * State (`state`) * ZIP code (`zip_code`) * ZIP+4 (`zip_code_plus_4`) 
    last_line: typing.Optional[str] = Field(None, alias='last_line')

    # A numerical score between 0 and 100 that represents the likelihood the provided name is associated with a physical address. 
    score: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='score')

    # Indicates the likelihood the recipient name and address match based on our custom internal calculation. Possible values are: - `high` — Has a Lob confidence score greater than 70. - `medium` — Has a Lob confidence score between 40 and 70. - `low` — Has a Lob confidence score less than 40. - `\"\"` — No tracking data exists for this address. 
    confidence: typing.Optional[Literal["high", "medium", "low", ""]] = Field(None, alias='confidence')

    # Value is resource type.
    object: typing.Optional[Literal["id_validation"]] = Field(None, alias='object')
    class Config:
        arbitrary_types_allowed = True
