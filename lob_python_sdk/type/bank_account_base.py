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
from lob_python_sdk.type.resource_description import ResourceDescription

class RequiredBankAccountBase(TypedDict):
    # Must be a <a href=\"https://www.frbservices.org/index.html\" target=\"_blank\">valid US routing number</a>.
    routing_number: str

    account_number: str

    # The type of entity that holds the account.
    account_type: str

    # The signatory associated with your account. This name will be printed on checks created with this bank account. If you prefer to use a custom signature image on your checks instead, please create your bank account from the <a href=\"https://dashboard.lob.com/#/login\" target=\"_blank\">Dashboard</a>.
    signatory: str

class OptionalBankAccountBase(TypedDict, total=False):
    description: ResourceDescription

    # The check template used for printing. The defualt value is `common`. If you bank with JP Morgan Chase and wish to use Positive Pay use the `jpm` template. `jpm` requires additional information to be provided.
    check_template: str

    # The fractional routing number for your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the fractional routing number associated with your home bank institution.
    fractional_routing_number: str

    # The city associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the city associated with your home bank institution.
    city: str

    # The state associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the state associated with your home bank institution.
    state: str

    # The zipcode associated with your home bank account. Required for the `jpm` check template only. Please contact a bank representative if you do not know the zipcode associated with your home bank institution.
    zipcode: str

    metadata: Metadata

class BankAccountBase(RequiredBankAccountBase, OptionalBankAccountBase):
    pass
