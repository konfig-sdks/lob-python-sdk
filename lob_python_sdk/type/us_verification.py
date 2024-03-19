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

from lob_python_sdk.type.deliverability_analysis import DeliverabilityAnalysis
from lob_python_sdk.type.lob_confidence_score import LobConfidenceScore
from lob_python_sdk.type.primary_line_us import PrimaryLineUs
from lob_python_sdk.type.recipient import Recipient
from lob_python_sdk.type.secondary_line import SecondaryLine
from lob_python_sdk.type.urbanization import Urbanization
from lob_python_sdk.type.us_components import UsComponents
from lob_python_sdk.type.us_ver_id import UsVerId

class RequiredUsVerification(TypedDict):
    pass

class OptionalUsVerification(TypedDict, total=False):
    components: UsComponents

    id: UsVerId

    recipient: Recipient

    primary_line: PrimaryLineUs

    secondary_line: SecondaryLine

    urbanization: Urbanization

    # Combination of the following applicable `components`: * City (`city`) * State (`state`) * ZIP code (`zip_code`) * ZIP+4 (`zip_code_plus_4`) 
    last_line: str

    # Summarizes the deliverability of the `us_verification` object. For full details, see the `deliverability_analysis` field. Possible values are: * `deliverable` – The address is deliverable by the USPS. * `deliverable_unnecessary_unit` – The address is deliverable, but the secondary unit information is unnecessary. * `deliverable_incorrect_unit` – The address is deliverable to the building's default address but the secondary unit provided may not exist. There is a chance the mail will not reach the intended recipient. * `deliverable_missing_unit` – The address is deliverable to the building's default address but is missing secondary unit information. There is a chance the mail will not reach the intended recipient. * `undeliverable` – The address is not deliverable according to the USPS. 
    deliverability: str

    # This field indicates whether an address was found in a more comprehensive address dataset that includes sources from the USPS, open source mapping data, and our proprietary mail delivery data. This field can be interpreted as a representation of whether an address is a real location or not. Additionally a valid address may contradict the deliverability field since an address can be a real valid location but the USPS may not deliver to that address. 
    valid_address: bool

    deliverability_analysis: DeliverabilityAnalysis

    lob_confidence_score: LobConfidenceScore

    # Value is resource type.
    object: str

class UsVerification(RequiredUsVerification, OptionalUsVerification):
    pass
