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

from lob_python_sdk.pydantic.cmp_id import CmpId
from lob_python_sdk.pydantic.metadata import Metadata

class LinkResponse(BaseModel):
    # Unique identifier prefixed with `lnk_`.
    id: typing.Optional[str] = Field(None, alias='id')

    campaign_id: typing.Optional[CmpId] = Field(None, alias='campaign_id')

    # A unique identifier for the registered domain.
    domain_id: typing.Optional[str] = Field(None, alias='domain_id')

    # The unique ID of the associated resource where the link was used.
    resource_id: typing.Optional[str] = Field(None, alias='resource_id')

    # The original target URL.
    redirect_link: typing.Optional[str] = Field(None, alias='redirect_link')

    # The shortened URL for the associated original URL.
    short_link: typing.Optional[str] = Field(None, alias='short_link')

    metadata_tag: typing.Optional[Metadata] = Field(None, alias='metadata_tag')

    # An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\"#tag/Billing-Groups\">Billing Group API</a> for more information.
    billing_group_id: typing.Optional[str] = Field(None, alias='billing_group_id')
    class Config:
        arbitrary_types_allowed = True
