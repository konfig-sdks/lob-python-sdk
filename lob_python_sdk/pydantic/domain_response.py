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


class DomainResponse(BaseModel):
    # Unique identifier for a domain.
    id: typing.Optional[str] = Field(None, alias='id')

    # The registered domain/hostname.
    domain: typing.Optional[str] = Field(None, alias='domain')

    # Unique identifier associated with the account the domain is registered for.
    account_id: typing.Optional[str] = Field(None, alias='account_id')
    class Config:
        arbitrary_types_allowed = True
