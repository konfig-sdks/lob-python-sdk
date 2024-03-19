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

from lob_python_sdk.type.cmp_id import CmpId
from lob_python_sdk.type.metadata import Metadata

class RequiredLinkResponse(TypedDict):
    pass

class OptionalLinkResponse(TypedDict, total=False):
    # Unique identifier prefixed with `lnk_`.
    id: str

    campaign_id: CmpId

    # A unique identifier for the registered domain.
    domain_id: str

    # The unique ID of the associated resource where the link was used.
    resource_id: str

    # The original target URL.
    redirect_link: str

    # The shortened URL for the associated original URL.
    short_link: str

    metadata_tag: Metadata

    # An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\"#tag/Billing-Groups\">Billing Group API</a> for more information.
    billing_group_id: str

class LinkResponse(RequiredLinkResponse, OptionalLinkResponse):
    pass
