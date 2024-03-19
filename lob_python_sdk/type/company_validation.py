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

from lob_python_sdk.type.identity_validation_company import IdentityValidationCompany
from lob_python_sdk.type.identity_validation_id import IdentityValidationId
from lob_python_sdk.type.primary_line_us import PrimaryLineUs
from lob_python_sdk.type.secondary_line import SecondaryLine
from lob_python_sdk.type.urbanization import Urbanization

class RequiredCompanyValidation(TypedDict):
    pass

class OptionalCompanyValidation(TypedDict, total=False):
    id: IdentityValidationId

    company: IdentityValidationCompany

    primary_line: PrimaryLineUs

    secondary_line: SecondaryLine

    urbanization: Urbanization

    # Combination of the following applicable `components`: * City (`city`) * State (`state`) * ZIP code (`zip_code`) * ZIP+4 (`zip_code_plus_4`) 
    last_line: str

    # A numerical score between 0 and 100 that represents the likelihood the provided name is associated with a physical address. 
    score: typing.Optional[typing.Union[int, float]]

    # Indicates the likelihood the recipient name and address match based on our custom internal calculation. Possible values are: - `high` — Has a Lob confidence score greater than 70. - `medium` — Has a Lob confidence score between 40 and 70. - `low` — Has a Lob confidence score less than 40. - `\"\"` — No tracking data exists for this address. 
    confidence: str

    # Value is resource type.
    object: str

class CompanyValidation(RequiredCompanyValidation, OptionalCompanyValidation):
    pass
