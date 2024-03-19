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

from lob_python_sdk.type.address_placement import AddressPlacement
from lob_python_sdk.type.buckslip_id import BuckslipId
from lob_python_sdk.type.card_id import CardId
from lob_python_sdk.type.extra_service import ExtraService
from lob_python_sdk.type.letter_add_on_types import LetterAddOnTypes
from lob_python_sdk.type.mail_type import MailType
from lob_python_sdk.type.qr_code_campaigns import QrCodeCampaigns
from lob_python_sdk.type.user_provided import UserProvided

class RequiredLetterDetailsWritable(TypedDict):
    # Set this key to `true` if you would like to print in color. Set to `false` if you would like to print in black and white.
    color: bool

class OptionalLetterDetailsWritable(TypedDict, total=False):
    address_placement: AddressPlacement

    # An array containing the types of add-ons for the Letter Creative.
    add_on_types: typing.Optional[typing.List[LetterAddOnTypes]]

    # A single-element array containing an existing buckslip id in a string format. See [buckslips](#tag/Buckslips) for more information. Note that buckslip letter campaigns require a minimum send quantity of 5,000 letters per campaign.
    buckslips: typing.Optional[typing.List[BuckslipId]]

    # A single-element array containing an existing card id in a string format. See [cards](#tag/Cards) for more information.
    cards: typing.Optional[typing.List[CardId]]

    custom_envelope: UserProvided

    # Set this attribute to `true` for double sided printing, or `false` for for single sided printing. Defaults to `true`.
    double_sided: bool

    extra_service: ExtraService

    mail_type: MailType

    qr_code: QrCodeCampaigns

class LetterDetailsWritable(RequiredLetterDetailsWritable, OptionalLetterDetailsWritable):
    pass
