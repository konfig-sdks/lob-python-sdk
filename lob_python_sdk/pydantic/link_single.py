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

from lob_python_sdk.pydantic.metadata import Metadata

class LinkSingle(BaseModel):
    # The original target URL.
    redirect_link: str = Field(alias='redirect_link')

    # The registered domain to be used for the short URL.
    domain: typing.Optional[str] = Field(None, alias='domain')

    # The unique path for the shortened URL, if empty a unique path will be used.
    slug: typing.Optional[str] = Field(None, alias='slug')

    metadata_tag: typing.Optional[Metadata] = Field(None, alias='metadata_tag')

    # An optional string with the billing group ID to tag your usage with. Is used for billing purposes. Requires special activation to use. See <a href=\"#tag/Billing-Groups\">Billing Group API</a> for more information.
    billing_group_id: typing.Optional[str] = Field(None, alias='billing_group_id')
    class Config:
        arbitrary_types_allowed = True
