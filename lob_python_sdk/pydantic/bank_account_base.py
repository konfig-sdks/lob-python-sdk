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
from lob_python_sdk.pydantic.resource_description import ResourceDescription

class BankAccountBase(BaseModel):
    # Must be a <a href=\"https://www.frbservices.org/index.html\" target=\"_blank\">valid US routing number</a>.
    routing_number: str = Field(alias='routing_number')

    account_number: str = Field(alias='account_number')

    # The type of entity that holds the account.
    account_type: Literal["company", "individual"] = Field(alias='account_type')

    # The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the <a href=\"https://dashboard.lob.com/#/login\" target=\"_blank\">Dashboard</a>.
    signatory: str = Field(alias='signatory')

    description: typing.Optional[ResourceDescription] = Field(None, alias='description')

    # The check template used for printing. The defualt value is `common`. If you bank with JP Morgan Chase and wish to use Positive Pay use the `jpm` template. `jpm` requires additional information to be provided.
    check_template: typing.Optional[Literal["common", "jpm"]] = Field(None, alias='check_template')

    # The fractional routing number for your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the fractional routing number associated with your home bank institution.
    fractional_routing_number: typing.Optional[str] = Field(None, alias='fractional_routing_number')

    # The city associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the city associated with your home bank institution.
    city: typing.Optional[str] = Field(None, alias='city')

    # The state associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the state associated with your home bank institution.
    state: typing.Optional[str] = Field(None, alias='state')

    # The zipcode associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the zipcode associated with your home bank institution.
    zipcode: typing.Optional[str] = Field(None, alias='zipcode')

    metadata: typing.Optional[Metadata] = Field(None, alias='metadata')
    class Config:
        arbitrary_types_allowed = True
