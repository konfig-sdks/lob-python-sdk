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

from lob_python_sdk.pydantic.address_placement import AddressPlacement
from lob_python_sdk.pydantic.buckslip_id import BuckslipId
from lob_python_sdk.pydantic.card_id import CardId
from lob_python_sdk.pydantic.extra_service import ExtraService
from lob_python_sdk.pydantic.letter_add_on_types import LetterAddOnTypes
from lob_python_sdk.pydantic.mail_type import MailType
from lob_python_sdk.pydantic.qr_code_campaigns import QrCodeCampaigns
from lob_python_sdk.pydantic.user_provided import UserProvided

class LetterDetailsWritable(BaseModel):
    # Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white.
    color: bool = Field(alias='color')

    address_placement: typing.Optional[AddressPlacement] = Field(None, alias='address_placement')

    # An array containing the types of add-ons for the Letter Creative.
    add_on_types: typing.Optional[typing.Optional[typing.List[LetterAddOnTypes]]] = Field(None, alias='add_on_types')

    # A single-element array containing an existing buckslip id in a string format. See [buckslips](#tag/Buckslips) for more information. Note that buckslip letter campaigns require a minimum send quantity of 5,000 letters per campaign.
    buckslips: typing.Optional[typing.Optional[typing.List[BuckslipId]]] = Field(None, alias='buckslips')

    # A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information.
    cards: typing.Optional[typing.Optional[typing.List[CardId]]] = Field(None, alias='cards')

    custom_envelope: typing.Optional[UserProvided] = Field(None, alias='custom_envelope')

    # Set this attribute to `true` for double sided printing, or `false` for for single sided printing. Defaults to `true`.
    double_sided: typing.Optional[bool] = Field(None, alias='double_sided')

    extra_service: typing.Optional[ExtraService] = Field(None, alias='extra_service')

    mail_type: typing.Optional[MailType] = Field(None, alias='mail_type')

    qr_code: typing.Optional[QrCodeCampaigns] = Field(None, alias='qr_code')
    class Config:
        arbitrary_types_allowed = True
