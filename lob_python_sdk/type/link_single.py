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

class RequiredLinkSingle(TypedDict):
    # The original target URL.
    redirect_link: str

class OptionalLinkSingle(TypedDict, total=False):
    # The registered domain to be used for the short URL.
    domain: str

    # The unique path for the shortened URL, if empty a unique path will be used.
    slug: str

    metadata_tag: Metadata

    # An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\"#tag/Billing-Groups\">Billing Group API</a> for more information.
    billing_group_id: str

class LinkSingle(RequiredLinkSingle, OptionalLinkSingle):
    pass
